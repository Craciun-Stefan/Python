from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from functools import partial

home = (45.79620, 24.17838)
work = (45.79596, 24.14903)
print(geodesic(home, work).kilometers)
geolocator = Nominatim(user_agent="http")
geocode = partial(geolocator.geocode, language="en")
print(geocode("45.79620, 24.17838"))
