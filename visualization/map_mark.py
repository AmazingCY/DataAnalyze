# -*- coding: utf-8 -*-
# @Time : 2021/11/21 19:00
# @Author : Cao yu
# @File : map_mark.py
# @Software: PyCharm


import folium
from folium import plugins
import pandas as pd
import collections
import math

# define the world map
world_map = folium.Map()

# San Francisco latitude and longitude values
latitude = 32.86
longitude = -97.23

# Read Dataset
cdata = pd.read_csv("viusal_data/Gowalla_filter.csv")

# get the first 200 crimes in the cdata
limit = 151180
data = cdata.iloc[266265:266820, :]


def find_laoction():
    User_ID = list(cdata.User_ID.values)
    print(max(User_ID, key=User_ID.count))


def mark_location():
    # Instantiate a feature group for the incidents in the dataframe
    incidents = folium.map.FeatureGroup()

    # Loop through the 200 crimes and add each to the incidents feature group
    for lat, lng, in zip(data.latitude, data.longitude):
        incidents.add_child(
            folium.CircleMarker(
                [lat, lng],
                radius=6,  # define how big you want the circle markers to be
                color='yellow',
                fill=True,
                fill_color='red',
                fill_opacity=0.4
            )
        )

    # Add incidents to map
    san_map = folium.Map(location=[latitude, longitude], zoom_start=10)
    san_map.add_child(incidents)

    # add pop-up text to each marker on the map
    latitudes = list(data.latitude)
    longitudes = list(data.longitude)
    labels = list(data.User_ID)

    for lat, lng, label in zip(latitudes, longitudes, labels):
        folium.Marker([lat, lng], popup=label).add_to(san_map)

    # folium.PolyLine(
    #        zip(latitudes, longitudes),
    #        color='red',
    #        weight=1.5,
    #        opacity=0.8).add_to(san_map)

    # save
    san_map.save("map_mark.html")


def count_location():
    # let's start again with a clean copy of the map of San Francisco
    san_map = folium.Map(location=[latitude, longitude], zoom_start=12)

    # instantiate a mark cluster object for the incidents in the dataframe
    incidents = plugins.MarkerCluster().add_to(san_map)

    # loop through the dataframe and add each data point to the mark cluster
    for lat, lng, label, in zip(data.latitude, data.longitude, cdata.POI_ID):
        folium.Marker(
            location=[lat, lng],
            icon=None,
            popup=label,
        ).add_to(incidents)

    # add incidents to map
    san_map.add_child(incidents)
    san_map.save("map_mark.html")


if __name__ == "__main__":
    # Display the map of San Francisco
    count_location()

    pass
