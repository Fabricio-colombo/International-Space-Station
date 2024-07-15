# speed.py
import math
from geolocation import haversine

def calculate_speed(lat1, lon1, lat2, lon2, time_diff):
    distance = haversine(lat1, lon1, lat2, lon2)
    speed = distance / time_diff
    speed_hours = speed * 3600
    return speed_hours
