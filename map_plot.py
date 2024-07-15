# map_plot.py
import os
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from utils import get_current_time

def maps(latitude, longitude, current_time, speed_hours, location_name):
    plt.figure(figsize=(38.4, 10.8))
    m = Basemap(projection='mill', llcrnrlat=-60, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')

    m.drawcoastlines()
    m.drawcountries()
    m.drawmapboundary(fill_color='aqua')
    m.fillcontinents(color='lightgreen', lake_color='aqua')
    m.drawparallels(range(-90, 91, 30), labels=[1, 0, 0, 0])
    m.drawmeridians(range(-180, 181, 60), labels=[0, 0, 0, 1])

    x, y = m(longitude, latitude)
    m.plot(x, y, 'ro', markersize=8)
    plt.text(x, y, f' \n{speed_hours:.3f} km/h', fontsize=12, ha='left', va='center', color='red')

    plt.title(f"Date/Time ({current_time})\nLatitude: {latitude}, Longitude: {longitude}\nVelocidade: {speed_hours:.3f} km/h\nLocalização: {location_name}", loc='center')

    plt.pause(0.1)
    plt.show(block=False)
    plt.pause(30)
    plt.close()
