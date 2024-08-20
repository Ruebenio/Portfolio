# importing librairies
import urllib.request
import json

# Defining the get_weather function to get the weather details
def get_weather(lat,lon):
  key='6f1ace88d9c1f54facc6e6493a8ee390'
  url=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  return result
