# iss.py
import requests

def get_iss_position():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    latitude = float(data['iss_position']['latitude'])
    longitude = float(data['iss_position']['longitude'])
    return latitude, longitude

def get_location_name(latitude, longitude):
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="my-app")
    location = geolocator.reverse((latitude, longitude), language='en')
    return location.address if location else "Unknown Location"
