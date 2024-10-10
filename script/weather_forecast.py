import requests
from datetime import datetime

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 63.107244,
    "longitude": 21.591357,
    "hourly": "precipitation,weather_code,cloud_cover,visibility,wind_speed_10m",
    "daily": "weather_code,sunrise,sunset,daylight_duration,sunshine_duration",
    "timezone": "auto"
}

response = requests.get(url, params=params)
data = response.json()

time = data["hourly"]["time"]
cloud_coverage = data["hourly"]["cloud_cover"]

daily_time = data["daily"]["time"]
sunrise = data["daily"]["sunrise"]
sunset = data["daily"]["sunset"]

current_time = datetime.now()
next_hour = current_time.replace(minute=0, second=0, microsecond=0).hour + 1
next_hour_str = current_time.replace(minute=0, second=0, microsecond=0).strftime('%Y-%m-%dT%H:00:00')
next_hour_date_str = current_time.strftime('%Y-%m-%d')

def find_sunrise_sunset(next_hour_date_str, daily_time, sunrise, sunset):
    for index, day in enumerate(daily_time):
        if next_hour_date_str == day:
            return sunrise[index], sunset[index]
    return None, None

sunrise_time, sunset_time = find_sunrise_sunset(next_hour_date_str, daily_time, sunrise, sunset)

def is_daytime(next_hour_str, sunrise_time, sunset_time):
 
    if sunrise_time <= next_hour_str <= sunset_time:
        return True  # Daytime
    return False  # Nighttime

def get_weather_forecast():
    next_hour_str1 = current_time.replace(minute=0, second=0, microsecond=0).strftime('%Y-%m-%dT%H:%M')
    if next_hour_str1 in time:
        next_hour_index = time.index(next_hour_str1)
        next_hour_cloud_cover = cloud_coverage[next_hour_index]

        if sunrise_time and sunset_time:
            if is_daytime(next_hour_str1, sunrise_time, sunset_time):
                if next_hour_cloud_cover > 40:
                    return "cloudy"
                else:
                    return "sunny"
            else:
                return "night"
        else:
            return "Sunrise and sunset times not found for the day of the next hour."
    else:
        return "Next hour data not found in the weather forecast."
