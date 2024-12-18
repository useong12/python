from folium.plugins import HeatMap
import folium
import requests
import pandas as pd
import numpy as np
import cv2


# def download_image():
#     url = 'https://wvs.earthdata.nasa.gov/api/v1/snapshot'
#     params = {
#         "REQUEST": "GetSnapshot",
#         "BBOX": "-90,-180,90,180",
#         "WIDTH": "1920",
#         "HEIGHT": "1080",
#         "FORMAT": "image/png",
#         "LAYERS": "VIIRS_SNPP_CorrectedReflectance_TrueColor",
#         "CRS": "EPSG:4326",
#         "TIME": "2024-11-01"
#     }

#     res = requests.get(url, params=params, stream=True)
#     with open("./test.png", "wb") as file:
#         for chunk in res.iter_content(1024):
#             file.write(chunk)


# download_image()

def fire_result():
    image = cv2.imread('./1218/test.png')
    if image is None:
        return
