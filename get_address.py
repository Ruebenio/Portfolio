# importing librairies
import urllib.request
import json
import os

# defining the address function using the reverse geolocation API
def address(lat,lon):
  gkey = os.environ['AD_KEY']
  url=f'https://api-bdc.net/data/reverse-geocode?latitude={lat}&longitude={lon}&localityLanguage=en&key={gkey}'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  return result
