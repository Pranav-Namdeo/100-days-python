from requests import *


API_KEY = "ac9e259bb9ea9da4e6d86d55c114d6d4"
LAT = "51.507351"
LON = "-0.127758"

API_URL = "https://api.openweathermap.org/data/2.5/forecast?q=Jabalpur,MP,India&APPID=ac9e259bb9ea9da4e6d86d55c114d6d4"

paramters = {
    "lat" : 23.181467,
    "lon" : 79.986404,
    "appid" : API_KEY,
    "cnt" : 4,
}

response = get(url="https://api.openweathermap.org/data/2.5/forecast", params=paramters)
response.raise_for_status()
weather_data = response.json()
#print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella")
