import folium
import requests
import pandas as pd

API_KEY = ''

# 날씨 데이터 가져오기


def get_weather_data(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={
        lat}&lon={lon}&appid={API_KEY}&units=metric&lang=kr"
    res = requests.get(url)

    if res.status_code == 200:
        return res.json()
    else:
        return None


cities = [
    {"name": "서울", "lat": 37.543593, "lon": 126.981818},
    {"name": "부산", "lat": 35.186147, "lon": 129.072099},
    {"name": "대전", "lat": 36.370862, "lon": 127.384698},
    {"name": "대구", "lat": 35.884505, "lon": 128.609825}
]

weather_data = []

for city in cities:
    data = get_weather_data(city['lat'], city['lon'])
    if data:
        weather_data.append({
            "latitude": city["lat"],
            "longitude": city['lon'],
            "city": city["name"],
            "temperature": data["main"]["temp"],
            "weather": data['weather'][0]['description']
        })

weather_df = pd.DataFrame(weather_data)

my_map = folium.Map(location=[36.566451, 127.921216], zoom_start=7)

# 마커 추가

for _, row in weather_df.iterrows():
    popup_info = f"""
    <b>도시:</b>{row["city"]}<br/>
    <b>온도:</b>{row["temperature"]}<br/>
    <b>날씨:</b>{row["weather"]}<br/>
     """

    # 날씨에 따라 마커 색상 추가
    icon_color = "blue" if row["temperature"] < 0 else "lightblue"

    # 마커 색상
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=folium.Popup(popup_info, max_width=300),
        icon=folium.Icon(color=icon_color, icon='cloud')
    ).add_to(my_map)

    my_map.save("./my_map.html")
