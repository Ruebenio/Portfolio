import urllib.request
import json
import os

# Function to get the weather from OpenWeatherMap API and calculate the temperature in Celcius
def temp(city):

  city='Tema'
  key = os.environ['WKEY'] # put your api key

  url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'

  request= urllib.request.urlopen(url)
  result = json.loads(request.read())
  temp= round(result["main"]["temp"]-273.15,2)
  return temp

