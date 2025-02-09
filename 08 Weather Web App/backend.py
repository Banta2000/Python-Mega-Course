import requests as req


# API_KEY = "b0e17c4f73cca5dbdea2a47c03a83274"
API_KEY = "3f3638b5fdc0547e151f629e489fb3b6"
lat = 33.44
lon = -94.04
exclude = "minutely,hourly,alerts"
city_name = "Zurich"

# url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={API_KEY}"
# url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}"
url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={API_KEY}"
response = req.get(url)
data = response.json()

print(data)
