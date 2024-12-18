from folium.plugins import HeatMap
import folium
import requests
import pandas as pd
import numpy as np


def get_data():
    url = 'https://eonet.gsfc.nasa.gov/api/v3/events'
    params = {
        'category': 'wildfires',
        'limit': 100
    }

    res = requests.get(url, params=params)

    if res.status_code == 200:
        return res.json()

    else:
        print(res.status_code)
        return None


data = pd.DataFrame(get_data())
# print(data.head())

fire_map = folium.Map(location=[37, 127], zoom_start=5)
heatmap_data = []

for fire_event in data['events']:
    lon = fire_event['geometry'][0]['coordinates'][0]
    lat = fire_event['geometry'][0]['coordinates'][1]
    title = fire_event['title']
    date = fire_event['geometry'][0]['date']

    popup_info = f"""
    <b>date:</b>{date}<br/>
    <b>title:</b>{title}<br/>
     """

    folium.Marker(
        location=[lat, lon],
        popup=folium.Popup(popup_info, max_width=300),
        icon=folium.Icon(color='red', icon='star')
    ).add_to(fire_map)

    heatmap_data.append([lat, lon])

HeatMap(heatmap_data).add_to(fire_map)

fire_map.save('./fire_map.html')
