import folium
from geojson import Feature, FeatureCollection, Point, Polygon

# # geojson 데이터 생성
# Feature1 = Feature(geometry=Point((126.981818, 37.543593)),
#                    properties={'name': '서울', 'population': '1000만'})

# Feature2 = Feature(geometry=Point((129.072099, 35.186147)),
#                    properties={'name': '부산', 'population': '370만'})

# Feature3 = Feature(geometry=Point((127.384698, 36.370862)),
#                    properties={'name': '대전', 'population': '150만'})

# Feature4 = Feature(geometry=Point((128.509606, 35.873697)),
#                    properties={'name': '대구', 'population': '240만'})

# # geojson 값을 하나로 묶기
# geojson_data = FeatureCollection([Feature1, Feature2, Feature3, Feature4])

# 지도 생성
my_map2 = folium.Map(location=[37.575102, 126.972752], zoom_start=12)
my_map2.save("my_map2.html")

# # geojson 데이터 지도에 추가
# folium.GeoJson(
#     geojson_data,
#     name='GeoJson Data',
#     tooltip=folium.GeoJsonTooltip(
#         fields=['name', 'population'],  # 표시할 속성
#         aliases=["도시이름: ", "인구 : "]  # 속성의 별칭
#     )
# ).add_to(my_map2)

polygon = [
    [126.721398, 37.659301],
    [126.635943, 37.559814],
    [126.707504, 37.317101],
    [127.159606, 37.374938],
    [127.200024, 37.551386],
    [127.125540, 37.667110],
    [126.853585, 37.703209],
    [126.721398, 37.659301]
]

polygon = Polygon([polygon])

feature = Feature(geometry=polygon, properties={'name': '수도권'})

geojson_data = FeatureCollection([feature])

folium.GeoJson(
    geojson_data,
    name='GeoJson Data',
    tooltip=folium.GeoJsonTooltip(
        fields=['name'],
        aliases=['영역 이름 : ']
    ),
    style_function=lambda _:  {
        'fiilcolor': 'blue',  # 다각형 내부 색상
        'color': 'black',  # 테두리 색상
        'weight': 2,  # 테두리 두꼐
        'fillOpacity': 0.5  # 내부투명도
    }

).add_to(my_map2)

my_map2.save("my_map2.html")

# cord = [
#     []
#     []
#     []
#     []
#     []
#     []
# ]

# poly = Polygon(cord)
# feature = Feature(geometry=poly,properties={'name':'수도권'})
# data = FeatureCollection(feature)

# folium.GeoJson(
#     data,
#     name='data',
#     tooltip=folium.GeoJsonTooltip(
#         fields=['name'],
#         aliases=['영역 이름 : ']
#     )
# ).add_to(my_map2)

# my_map2.save("my_map2.html")
