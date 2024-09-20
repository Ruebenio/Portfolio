# importing librairies
import urllib.request
import json
import os
# Defining the get_weather function to get the weather details
def get_weather(lat,lon):
  wkey = os.environ['WKEY']
  url=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={wkey}'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  return result
