import requests

OWM_Endpoint = "http://api.openweathermap.org/data/2.5/forecast?"
api_key = "9c2d9eb61b5426b630ef17174da1f8df"

weather_params = {
    "appid": api_key,
    "lon": 10.99,
    "lat": 44.34,
    "cnt": 4
}

will_rain = False
response = requests.get(OWM_Endpoint, params=weather_params)
w_data = response.json()
for hour_data in w_data["list"]:
    cond_code = hour_data["weather"][0]["id"]
    if int(cond_code) < 700:
        will_rain = True

if will_rain == True:
    print("Bring Umbrella")