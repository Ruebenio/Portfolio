# importing librairies
import urllib.request
import json

# Defining the iss_loc function to get the ISS location
def iss_loc():
  url='http://api.open-notify.org/iss-now.json'

  request = urllib.request.urlopen(url)
  result = json.loads(request.read())

  lat = result['iss_position']['latitude']
  lon = result['iss_position']['longitude']
  print("https://google.com/maps/place/"+ lat +"+" + lon)
  locs = f'https://google.com/maps/place/{lat}+{lon}' 
   
  return lat,lon,locs