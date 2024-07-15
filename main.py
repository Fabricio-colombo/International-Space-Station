# main.py
import time
import datetime
from utils import get_current_time
from iss import get_iss_position, get_location_name
from speed import calculate_speed
from map_plot import maps

def main():
    previous_latitude, previous_longitude = get_iss_position()
    previous_time = datetime.datetime.now()
    
    while True:
        latitude, longitude = get_iss_position()
        current_time = datetime.datetime.now()
        time_diff = (current_time - previous_time).total_seconds()
        
        speed_hours = calculate_speed(previous_latitude, previous_longitude, latitude, longitude, time_diff)
        location_name = get_location_name(latitude, longitude)

        maps(latitude, longitude, get_current_time(), speed_hours, location_name)
        
        print(f"Date/Time atual: {get_current_time()}")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
        print(f"Velocidade: {speed_hours:.2f} km/h")
        print(f"Localização: {location_name}")
        print("~~~" * 10)
        
        previous_latitude, previous_longitude = latitude, longitude
        previous_time = current_time

        time.sleep(7)

if __name__ == "__main__":
    main()
