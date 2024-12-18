import folium
import csv

sub_map = folium.Map(location=[37.585410, 126.909486], zoom_start=12)
sub_map.save("sub_map.html")

map_info = [
    {'location': [37.585410, 126.909486], 'popup': '증산역'},
    {'location': [37.592551, 126.914035], 'popup': '새절역'},
    {'location': [37.600304, 126.915237], 'popup': '응암역'},
    {'location': [37.578540, 126.901504], 'popup': 'DMC역'},
    {'location': [37.582281, 126.895839], 'popup': '수색역'}
]

csv_path = "./subway.csv"

with open(csv_path, mode='w', encoding='utf-8', newline='') as csv_file:

    csv_writer = csv.writer(csv_file)

    for info in map_info:
        latitude = info['location'][0]
        longitude = info['location'][1]
        popup_text = info['popup']
        csv_writer.writerow([latitude, longitude, popup_text])


for info in map_info:

    folium.Marker(location=info['location'], popup=info['popup'], icon=folium.Icon(
        color='green', icon='star')).add_to(sub_map)

    folium.Circle(
        location=info['location'],
        radius=300,
        color='blue',
        fill=True,
        fill_color='cyan',
        popup=info['popup']
    ).add_to(sub_map)

sub_map.save("sub_map.html")
