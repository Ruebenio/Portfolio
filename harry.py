import urllib.request
import json
import random

# Function to get a random character from Harry Potter Api
def get_char():
  url='https://hp-api.onrender.com/api/characters'
  request= urllib.request.urlopen(url)
  result = json.loads(request.read())
  char=random.randint(1,40)
  name = result[char]['name']
  image = result[char]['image']
  actor = result[char]['actor']
  result = [name,image,actor]

  return result