import requests

url="https://api.open-meteo.com/v1/forecast"

#daily=weather_code,sunrise,sunset,daylight_duration,sunshine_duration&timezone=auto
params={
    "latitude":63.107244 ,
    "longitude":21.591357 ,
    "hourly":"precipitation,weather_code,cloud_cover,visibility,wind_speed_10m" ,
    "daily":"weather_code,sunrise,sunset,daylight_duration,sunshine_duration",
   " timezone":"auto" 
}
response=requests.get(url,params=params)
data = response.json()

time = data["hourly"]["time"]
weather = data["hourly"]["weather_code"]
cloud_coverage = data["hourly"]["cloud_cover"]
visibility_status = data["hourly"]["visibility"]
wind_speed = data["hourly"]["wind_speed_10m"]

with open("output_hourly.text","a") as f:
    for index,item in enumerate(time):
            f.write(f"{item}, {weather[index]} , {cloud_coverage[index]},{visibility_status[index]},{wind_speed[index]}\n")

daily=data["daily"]["time"]
weather_daily=data["daily"]["weather_code"]
sunrise=data["daily"]["sunrise"]
sunset=data["daily"]["sunset"]
daylight_duration=data["daily"]["daylight_duration"]
sunshine_duration=data["daily"]["sunshine_duration"]

with open("output_daily.text","a") as f:
    for index,item in enumerate(time):
            f.write(f"{item}, {weather_daily[index]} , {sunrise[index]},{sunset[index]},{daylight_duration[index]},{sunshine_duration[index]}\n")



