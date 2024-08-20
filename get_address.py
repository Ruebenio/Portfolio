# importing librairies
import urllib.request
import json

# defining the address function using the reverse geolocation API
def address(lat,lon):
  key='bdc_5a5c1ca777334342b5e596fa84aa1784'
  url=f'https://api-bdc.net/data/reverse-geocode?latitude={lat}&longitude={lon}&localityLanguage=en&key={key}'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  return result
