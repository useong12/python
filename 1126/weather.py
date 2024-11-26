# 날씨 데이터 분석 프로그램

weather_data = [
    ["2024-11-20", "서울", 15.2, 0.0],
    ["2024-11-20", "부산", 18.4, 0.0],
    ["2024-11-21", "서울", 10.5, 2.3],
    ["2024-11-21", "부산", 14.6, 1.2],
    ["2024-11-22", "서울", 8.3, 0.0],
    ["2024-11-22", "부산", 12.0, 0.0]
]


def main():
    while True:
        print('''[날씨 데이터 분석 프로그램]
1. 평균 기온 계산
2. 최고/최저 기온 찾기
3. 강수량 분석
4. 날씨 데이터 추가
5. 전체 데이터 출력
6. 종료''')
        print()
        ch = input("원하는 기능의 번호를 입력하세요 : ")
        if ch.isdigit() == 0:
            print("1~6 사이의 숫자를 입력해주세요")
            continue
        elif int(ch) == 6:
            print("프로그램을 종료합니다.")
            break
        elif int(ch) == 1:
            weather_avg()
        elif int(ch) == 2:
            weather_minmax()
        elif int(ch) == 3:
            weather_rain()
        elif int(ch) == 4:
            add_data()
        elif int(ch) == 5:
            print(weather_data)
        else:
            print("1~6 사이의 숫자를 입력해주세요")
            continue


def weather_avg():
    while True:
        city = input("원하는 도시의 이름을 입력하세요 (종료하려면 '종료' 입력): ")

        if city == "종료":
            break

        city_data = [data for data in weather_data if data[1] == city]

        if city_data:
            total_temp = sum([data[2] for data in city_data])
            avg_temp = total_temp / len(city_data)
            print(f"{city}의 평균 기온은 {avg_temp:.1f}도 입니다.")
        else:
            print(f"{city}의 데이터가 존재하지 않습니다. 다시 입력해주세요.")


def weather_minmax():
    while True:
        city = input("원하는 도시의 이름을 입력하세요 (종료하려면 '종료' 입력) : ")

        if city == "종료":
            break

        city_data = [data for data in weather_data if data[1] == city]

        if city_data:
            temp = list(map(lambda x: x[2], city_data))
            print(f"{city}의 최고기온 : {max(temp)}, 최저기온 : {min(temp)}")

        else:
            print(f"{city}의 데이터가 존재하지 않습니다. 다시 입력해주세요.")


def weather_rain():
    while True:
        city = input("원하는 도시의 이름을 입력하세요 (종료하려면 '종료' 입력) : ")

        if city == "종료":
            break

        city_data = [data for data in weather_data if data[1] == city]

        if city_data:
            rain = list(map(lambda x: x[3], city_data))
            rain = list(filter(lambda x: x > 0, rain))
            print(f"{city}의 총 강수량 : {sum(rain)}mm")
            print(f"{city}의 강수량이 있었던 날 : {len(rain)}일")

        else:
            print(f"{city}의 데이터가 존재하지 않습니다. 다시 입력해주세요.")


def add_data():
    new_data = []

    data = input("날짜를 입력하세요 (YYYY-MM-DD) : ")
    new_data.append(data)
    data = input("도시를 입력하세요 : ")
    new_data.append(data)
    data = input("평균기온을 입력하세요 : ")
    new_data.append(data)
    data = input("강수량을 입력하세요 : ")
    new_data.append(data)

    weather_data.append(new_data)
    print(weather_data)


main()
