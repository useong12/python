import folium


my_map = folium.Map(lacation=[37.649113, 126.972979], zoom_start=32)
# my_map.save("my_map.html")

# 원형 마커 추가
# folium.Circle(
#     location=[37.649113, 126.972979],
#     radius=1000,
#     color='blue',
#     fill=True,
#     fill_color='cyan',
#     popup='남한산성'
# ).add_to(my_map)

# my_map.save("castle.html")

# 딕셔너리 형태로 추가

# map_info = [
#     {'location': [37.5758, 12.6733], 'pop_up': '경복궁역'},
#     {'location': [37.5458, 12.7033], 'pop_up': '종각역'},
#     {'location': [37.5158, 12.8833], 'pop_up': '덕수궁'},
# ]

# for info in map_info:
#     folium.Marker(location=info['location'], popup=info['pop_up'], icon=folium.Icon(
#         color='green', icon='star')).add_to(my_map)

# my_map.save("./my_map.html")
