import requests

OMW_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "565d4c3bd18c1f21d36997e2a1cd9617"

weather_params = {
    "lat": 10.729669,
    "lon": 106.702890,
    "appid": api_key,
}

response = requests.get(OMW_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)