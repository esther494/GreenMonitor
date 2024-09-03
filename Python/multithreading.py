import threading
import time
from datetime import datetime, timezone, timedelta
import pandas as pd
from retry_requests import retry
from weather_client import WeatherClient
from server_client import ServerClient
import json

# Message to send to ESP32
message = {
    'error_code': 0, # No error initially
    'time':"",
    'temperature': "",
    'humidity': "",
    'uv_index': "",
    'moisture': "",
    'general': ""
}

# Lock for thread-safe access to shared message
message_lock = threading.Lock()

# Shared data directory
shared_data = {
    'weather_data' : None,
    'sensor_data' : "0.00,0.00,0.00,0.00",
}

# Lock for thread-safe access to shared data
data_lock = threading.Lock()

"""
Fetches weather data from Open-Meteo using their free API. 

- The function updates `self.error_code` to 0 if the operation is successful. 
- It acquires `data_lock` to safely update the `shared_data` with the fetched weather information.
- It acquires `message_lock` to handle and update any potential error messages.

Returns:
    None: Updates internal states and locks as needed.
Error Codes:
    Error Code 1: Failed to connect to the API, Error Code 2: An unexpected error occurred
"""
def fetch_weather_data():
    weather_client = WeatherClient()
    while True:
        weather_client.fetch_weather_data()
        with data_lock:
            shared_data['weather_data'] = weather_client.weather_data
        with message_lock:
            message['error_code'] = weather_client.error_code
        time.sleep(1) # Every 10 minutes

"""
Fetches sensor data wirelessly from the ESP32.

- Returns error codes if an error occurs during server connection or data retrieval.
- Processes the received data to validate its integrity.
- Uses `data_lock` to safely update the `shared_data` with valid sensor readings.
- Uses `message_lock` to update the `shared_message` with any error information.

Returns:
    None: Updates internal states and locks as needed.
Error Codes:
    Error Code 3: Socket error, Error Code 4: An unexpected error occurred,
    Error Code 5: Error processing data
"""
def fetch_server_data():
    server_client = ServerClient()
    while True:
        message_json = json.dumps(message)
        data = server_client.client_socket.recv(1024)
        server_client.client_socket.sendall(message_json.encode('utf-8'))
        if not data:
            print("Client Disconnected.")
        
        server_client.process_data(data)
        
        with data_lock:
            shared_data['previous_sensor_data'] = shared_data['sensor_data']
            shared_data['sensor_data'] = server_client.last_received_data
        
        with message_lock:
            message['error_code'] = server_client.error_code
        
        print(server_client.last_received_data)
        time.sleep(3) # Every 3 seconds

"""
Processes the fetched weather data and generates user suggestions based on the information.

- Utilizes `data_lock` to safely access the weather data.
- Uses `message_lock` to update the user suggestions based on the processed data.
- Returns an error code if the weather data is missing or invalid.

Returns:
    None: Updates internal states and locks as needed.
Error Codes:
    Error Code 6: Data does not exist
"""
def hourly_predictions():
    time.sleep(10) # Let the other thread load the data first
    high_temperature_threshold = 30
    low_temperature_threshold = 10
    humidity_threshold = 80
    uv_threshold = 8
    
    while True:
        # This if checks that the data has been loaded in
        if shared_data['weather_data'] is not None and isinstance(shared_data['weather_data']['hourly'], pd.DataFrame):
            df = shared_data['weather_data']['hourly']
            current_datetime = datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0)
            
            # Ensure that both the DataFrame and current time are timezone-aware
            df["date"] = pd.to_datetime(df["date"], utc=True)
            current_datetime = pd.to_datetime(current_datetime)
            
            # Find the index of the matching row
            matching_index = df.index[df["date"] == current_datetime].tolist()
            
            if matching_index:
                # Get the index of the first matching row
                first_match_idx = matching_index[0]

                # Get the next two rows, including the matching row
                result_rows = df.iloc[first_match_idx:first_match_idx + 3]  # Adjust the slice as needed

                # Check conditions
                temperature_check_high = (result_rows["temperature_2m"] > high_temperature_threshold).any()
                temperature_check_low = (result_rows["temperature_2m"] < low_temperature_threshold).any()
                humidity_check = (result_rows["relative_humidity_2m"] > humidity_threshold).any()
                uv_check = (result_rows["uv_index"] > uv_threshold).any()
                
                update_message(result_rows)

            else:
                print("No matching row found.")
        else:
            print("Weather data is not available or not in DataFrame format.")

        time.sleep(5)

def update_message(result_rows):
    with data_lock:
        data_list = shared_data['sensor_data'].split(',')

    with message_lock:
        # Initialize message dictionary
        message.update({
            'temperature': "",
            'humidity': "",
            'uv_index': "",
            'moisture': "",
            'time': f"From {datetime.now().strftime('%H:%M')} to {(datetime.now() + timedelta(hours=3)).strftime('%H:%M')}"
        })
        
        def create_summary(data_label, current_value, forecast_values, unit):
            summary = [f"Current {data_label}:+{current_value}{unit}"]
            forecast = ' '.join([f"{round(value)}{unit}" for value in forecast_values])
            summary.append("Next three hours:")
            summary.append(forecast)
            return "+".join(summary)

        # Temperature Summary
        message['temperature'] = create_summary(
            "Temperature", 
            f"{data_list[0]}", 
            result_rows["temperature_2m"], 
            "*C"
        )

        # Humidity Summary
        message['humidity'] = create_summary(
            "Humidity", 
            f"{data_list[1]}", 
            result_rows["relative_humidity_2m"], 
            "%"
        )

        # UV Index Summary
        message['uv_index'] = create_summary(
            "UV index", 
            data_list[2], 
            result_rows["uv_index"], 
            ""
        )

        # Soil Moisture Summary
        message['moisture'] = create_summary(
            "Soil Moisture Level", 
            data_list[3], 
            result_rows["soil_moisture_3_to_9cm"], 
            ""
        )

        # Print summaries for debugging
        #print(message['temperature'])
        #print(message['humidity'])
        #print(message['uv_index'])
        #print(message['moisture'])

# Start the weather data fetching in a background thread
weather_thread = threading.Thread(target=fetch_weather_data)
weather_thread.daemon = True
weather_thread.start()

# Start the weather data fetching in a background thread
server_thread = threading.Thread(target=fetch_server_data)
server_thread.daemon = True
server_thread.start()

hourly_predictions_thread = threading.Thread(target=hourly_predictions)
hourly_predictions_thread.daemon = True
hourly_predictions_thread.start()



# Main program could continue doing other tasks or just sleep
while True:

    #time.sleep(3)
    time.sleep(60)  # Main thread stays alive
