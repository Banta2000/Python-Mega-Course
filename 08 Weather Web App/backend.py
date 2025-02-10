import requests as req
import json
from datetime import datetime


API_KEY = "3f3638b5fdc0547e151f629e489fb3b6"
# # url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}"


def get_city_coordinates(city_name):
    API_KEY = "3f3638b5fdc0547e151f629e489fb3b6"
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={API_KEY}"
    response = req.get(url)
    data = response.json()
    lat = data[0]["lat"]
    lon = data[0]["lon"]
    return lat, lon


def get_location_data(lat, lon):
    exclude = "minutely,hourly,alerts"
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={API_KEY}&units=metric"
    response = req.get(url)
    data = response.json()
    data = data["daily"]
    dates = [x["dt"] for x in data]
    temperatures = [x["temp"] for x in data]
    temperatures = [x["day"] for x in temperatures]
    weather = [x["weather"][0]["main"] for x in data]
    return dates, temperatures, weather


def get_data(days, location):
    lat, lon = get_city_coordinates(location)
    print(lat, lon)
    dates, temperatures, weather = get_location_data(lat, lon)
    dates = dates[:days]
    dates = [datetime.utcfromtimestamp(date).strftime("%Y-%m-%d") for date in dates]
    temperatures = temperatures[:days]
    weather = weather[:days]
    return dates, temperatures, weather



# get_data(5, "asdasdas")
