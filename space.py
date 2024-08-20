import urllib.request
import json

# Function to get the number of people in space
def people_space():
  url = 'http://api.open-notify.org/astros.json'

  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  number = result['number']

  #print(result)
  print(f"The number of people in space are {number}")
  return number