# importing librairies
import urllib.request
import json

# Defining the country function to get the country details
def country(name):
  url=f'https://restcountries.com/v3.1/alpha/{name}'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  return result 
