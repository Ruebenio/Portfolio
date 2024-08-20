# importing librairies
import geopy.distance

# Defining the distance function to calculate the distance between myself and the ISS
def dist(coords_1_lat,coords_1_lon,coords_2_lat,coords_2_lon):
  coords_1 = (coords_1_lat, coords_1_lon) # location of ISS 
  coords_2 = (coords_2_lat, coords_2_lon) # my location


  return  round((geopy.distance.distance(coords_1, coords_2).km),2)
