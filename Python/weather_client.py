import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
import time
from requests.exceptions import RequestException
import tkinter as tk
from tkinter import messagebox

"""
The code to connect and load the data is from Open_Meteo:
https://open-meteo.com/en/docs

I have added the part to throw an exception in case of an error.
"""

class WeatherClient:
    def __init__(self):
        # Initialize weather data storage
        self.weather_data = {
            "current": None,
            "hourly": None,
            "daily": None
        }

        self.error_code = 0

        try:
            # Setup the Open-Meteo API client with cache
            cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
            self.openmeteo = openmeteo_requests.Client(session=cache_session)
        except RequestException as e:
            self.show_error(f"Error Code 1: Failed to connect to the API: {e}")
            self.error_code = 1
        except Exception as e:
            self.show_error(f"Error Code 2: An unexpected error occurred: {e}")
            self.error_code = 2

    # Method to show error in a pop-up window
    def show_error(self, message):
        root = tk.Tk()
        root.withdraw()  # Hide the main Tkinter window
        messagebox.showerror("Error", message)
        root.destroy()    
    
    def fetch_weather_data(self):
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": 43.7001,
            "longitude": -79.4163,
            "current": ["temperature_2m", "relative_humidity_2m", "precipitation", "rain"],
            "hourly": ["temperature_2m", "relative_humidity_2m", "precipitation_probability", "snowfall", "soil_temperature_6cm", "soil_moisture_3_to_9cm", "uv_index"],
            "daily": ["sunrise", "sunset", "daylight_duration", "sunshine_duration", "uv_index_max"],
            "timezone": "America/New_York"
        }
        responses = self.openmeteo.weather_api(url, params=params)
        response = responses[0]
        
        # Process current values
        current = response.Current()
        self.weather_data["current"] = {
            "temperature_2m": current.Variables(0).Value(),
            "relative_humidity_2m": current.Variables(1).Value(),
            "precipitation": current.Variables(2).Value(),
            "rain": current.Variables(3).Value()
        }
        
        # Process hourly data
        hourly = response.Hourly()
        hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
        hourly_data = {
            "date": pd.date_range(
                start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
                end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
                freq=pd.Timedelta(seconds=hourly.Interval()),
                inclusive="left"
            ),
            "temperature_2m": hourly_temperature_2m,
            "relative_humidity_2m": hourly.Variables(1).ValuesAsNumpy(),
            "precipitation_probability": hourly.Variables(2).ValuesAsNumpy(),
            "snowfall": hourly.Variables(3).ValuesAsNumpy(),
            "soil_temperature_6cm": hourly.Variables(4).ValuesAsNumpy(),
            "soil_moisture_3_to_9cm": hourly.Variables(5).ValuesAsNumpy(),
            "uv_index": hourly.Variables(6).ValuesAsNumpy()
        }
        self.weather_data["hourly"] = pd.DataFrame(data=hourly_data)
        
        # Process daily data
        daily = response.Daily()
        daily_data = {
            "date": pd.date_range(
                start=pd.to_datetime(daily.Time(), unit="s", utc=True),
                end=pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
                freq=pd.Timedelta(seconds=daily.Interval()),
                inclusive="left"
            ),
            "sunrise": daily.Variables(0).ValuesAsNumpy(),
            "sunset": daily.Variables(1).ValuesAsNumpy(),
            "daylight_duration": daily.Variables(2).ValuesAsNumpy(),
            "sunshine_duration": daily.Variables(3).ValuesAsNumpy(),
            "uv_index_max": daily.Variables(4).ValuesAsNumpy()
        }
        self.weather_data["daily"] = pd.DataFrame(data=daily_data)

    def get_weather_data(self):
        return self.weather_data

# Example of how to use the WeatherClient class
if __name__ == "__main__":
    client = WeatherClient()
    client.fetch_weather_data()
    time.sleep(10)  # Wait for a short period to allow fetching to start
    data = client.get_weather_data()
    print(data["current"])  # Print current weather data
