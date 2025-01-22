import os
import json
import boto3
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class WeatherDashboard:
    def __init__(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        self.bucket_name = os.getenv("AWS_BUCKET_NAME")
        self.s3_client = boto3.client("s3")
    
    def create_bucket(self):
        try:
            self.s3_client.create_bucket(Bucket=self.bucket_name)
            print(f"Bucket {self.bucket_name} created successfully")
        except self.s3_client.exceptions.BucketAlreadyExists:
            print(f"Bucket {self.bucket_name} already exists")
        except Exception as e:
            print(f"Error in create_bucket: {e}")
            raise

    def fetch_weather(self, city):
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error in fetch_weather: {e}")
            return None
    
    def save_to_s3(self, data, city):
        if not data:
            return False
        
        timestamp = datetime.now().strftime("%d%m%Y-%H%M%S")
        file_name = f"weather-data/{city}-{timestamp}.json"

        try:
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=file_name,
                Body=json.dumps(data),
                ContentType="application/json"
            )

            print(f"Data saved successfully to {file_name}")
            return True
        except Exception as e:
            print(f"Error in save_to_s3: {e}")
            return False

def main():
    try:
        weather_dashboard = WeatherDashboard()
        weather_dashboard.create_bucket()

        cities = ["New York", "San Francisco", "Seattle"]

        for city in cities:
            print(f"Getting weather data for {city}")
            weather_data = weather_dashboard.fetch_weather(city)
            if weather_data:
                weather_dashboard.save_to_s3(weather_data, city)
                print(f"Data saved successfully for {city}")
            else:
                print(f"Failed to get weather data for {city}")
    except Exception as e:
        print(f"Error in main: {e}")

if __name__ == "__main__":
    main()