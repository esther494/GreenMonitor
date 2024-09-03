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
    'error_code': 0,  # No error initially
    'time': "",
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
    'weather_data': None,
    'sensor_data': "0.00,0.00,0.00,0.00",
}

# Lock for thread-safe access to shared data
data_lock = threading.Lock()

def fetch_weather_data():
    """
    Fetches weather data from Open-Meteo using their free API.

    - Updates `message['error_code']` based on success or failure.
    - Safely updates `shared_data['weather_data']` with fetched data using `data_lock`.
    """
    weather_client = WeatherClient()
    while True:
        weather_client.fetch_weather_data()
        with data_lock:
            shared_data['weather_data'] = weather_client.weather_data
        with message_lock:
            message['error_code'] = weather_client.error_code
        time.sleep(600)  # Fetch data every 10 minutes

def fetch_server_data():
    """
    Fetches sensor data wirelessly from the ESP32.

    - Sends and receives data using server_client.
    - Updates `shared_data['sensor_data']` with valid sensor readings.
    - Updates `message['error_code']` with server_client's error information.
    """
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
        time.sleep(3)  # Fetch data every 3 seconds

def hourly_predictions():
    """
    Processes the fetched weather data and generates user suggestions based on the information.

    - Ensures weather data is available and in DataFrame format.
    - Updates `message` with user suggestions based on processed data.
    """
    time.sleep(10)  # Allow other threads to load data

    high_temperature_threshold = 30
    low_temperature_threshold = 10
    humidity_threshold = 80
    uv_threshold = 8
    
    while True:
        if (shared_data['weather_data'] is not None and 
            isinstance(shared_data['weather_data']['hourly'], pd.DataFrame)):

            df = shared_data['weather_data']['hourly']
            current_datetime = datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0)
            
            df["date"] = pd.to_datetime(df["date"], utc=True)
            current_datetime = pd.to_datetime(current_datetime)
            
            matching_index = df.index[df["date"] == current_datetime].tolist()
            
            if matching_index:
                first_match_idx = matching_index[0]
                result_rows = df.iloc[first_match_idx:first_match_idx + 3]

                temperature_check_high = (result_rows["temperature_2m"] > high_temperature_threshold).any()
                temperature_check_low = (result_rows["temperature_2m"] < low_temperature_threshold).any()
                humidity_check = (result_rows["relative_humidity_2m"] > humidity_threshold).any()
                uv_check = (result_rows["uv_index"] > uv_threshold).any()
                
                update_message(result_rows)

            else:
                print("No matching row found.")
        else:
            print("Weather data is not available or not in DataFrame format.")

        time.sleep(5)  # Run every 5 seconds

def update_message(result_rows):
    """
    Updates the message dictionary with formatted weather and sensor data.

    - Uses `data_lock` to safely access `shared_data`.
    - Updates `message` with temperature, humidity, UV index, and soil moisture summaries.
    """
    with data_lock:
        data_list = shared_data['sensor_data'].split(',')

    with message_lock:
        message.update({
            'temperature': "",
            'humidity': "",
            'uv_index': "",
            'moisture': "",
            'time': f"From {datetime.now().strftime('%H:%M')} to {(datetime.now() + timedelta(hours=3)).strftime('%H:%M')}"
        })
        
        def create_summary(data_label, current_value, forecast_values, unit):
            summary = [f"Current {data_label}: {current_value}{unit}"]
            forecast = ' '.join([f"{round(value)}{unit}" for value in forecast_values])
            summary.append("Next three hours:")
            summary.append(forecast)
            return "\n".join(summary)

        message['temperature'] = create_summary(
            "Temperature", 
            data_list[0], 
            result_rows["temperature_2m"], 
            "*C"
        )

        message['humidity'] = create_summary(
            "Humidity", 
            data_list[1], 
            result_rows["relative_humidity_2m"], 
            "%"
        )

        message['uv_index'] = create_summary(
            "UV index", 
            data_list[2], 
            result_rows["uv_index"], 
            ""
        )

        message['moisture'] = create_summary(
            "Soil Moisture Level", 
            data_list[3], 
            result_rows["soil_moisture_3_to_9cm"], 
            ""
        )

        # Print summaries for debugging
        # print(message['temperature'])
        # print(message['humidity'])
        # print(message['uv_index'])
        # print(message['moisture'])

# Start background threads
weather_thread = threading.Thread(target=fetch_weather_data)
weather_thread.daemon = True
weather_thread.start()

server_thread = threading.Thread(target=fetch_server_data)
server_thread.daemon = True
server_thread.start()

hourly_predictions_thread = threading.Thread(target=hourly_predictions)
hourly_predictions_thread.daemon = True
hourly_predictions_thread.start()

# Main program stays alive
while True:
    time.sleep(60)  # Main thread stays alive
