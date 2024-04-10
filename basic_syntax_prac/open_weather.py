
# use url: https://openweathermap.org/api
# plz link to url and sign-in to get api key

import requests

_city = "Taipei"
_api_key = "(Replace here)plz link to url and sign-in to get api key"


_url = f"https://api.openweathermap.org/data/2.5/weather?q={_city}&appid={_api_key}"

_weather_data = requests.get(_url).json()
print(f"{int(_weather_data['main']['temp'])} K")
print(f"{int(_weather_data['main']['temp'] - 273.15)} C")

