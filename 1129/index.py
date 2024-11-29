'''
# 모듈
import calc
# 모듈 내 함수 호출
print(calc.add(1, 2))
print(calc.minus(1, 2))
print(calc.multi(1, 2))
print(calc.div(1, 2))

from calc import add, div

print(add(1, 2))
print(div(1, 2))

from calc import add as a, div as d

print(a(1, 2))
print(d(1, 2))

from calc import *

print(add(1, 2))
print(minus(1, 2))
print(multi(1, 2))
print(div(1, 2))


from datetime import datetime, timedelta

now = datetime.today()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

print(f"{now.year}년 {now.month}월 {now.day}일")


from datetime import datetime, timedelta, timezone

now = datetime.now()
# print(now)

# 특정 날짜 계산


# next_week = now + timedelta(weeks=1, hours=1)
# print(next_week)

# 타임존 계산
seoul_tz = timezone(timedelta(hours=9))
print(datetime.now(timezone.utc))
print(datetime.now(seoul_tz))


from datetime import date

open_day = date(year=2024, month=11, day=18)
print(date.today())
print(date.today().weekday())
week = ['월', '화', '수', '목', '금', '토', '일']
print(week[date.today().weekday()])

pass_day = date.today() - open_day
print(pass_day.days)


import time

print(time.time())
print(time.localtime())
print("2초대기")
time.sleep(2)
print("대기완료")

start = time.perf_counter()
time.sleep(1)
end = time.perf_counter()
print(end-start)


import math

# print(math.pi)
# print(math.sqrt(25))
# print(math.factorial(5))

print(math.ceil(2.43))  # 올림
print(math.floor(4.88))  # 버림
print(round(2.50))  # 반올림


import random
import math

# print(random.randint(1, 10))
# print(random.uniform(1.1, 5.5))
# print(random.random())
# print(random.randrange(1000, 10000))

choices = ['월', '화', '수', '목', '금', '토', '일']
print(random.choice(choices))

rand = 1000 + math.floor(random.random()*9000)
print(rand)


import random

selected_numbers = []

while len(selected_numbers) < 6:
    selected_number = random.randint(1, 45)
    if selected_number not in selected_numbers:
        selected_numbers.append(selected_number)

selected_numbers.sort()
print(selected_numbers)

import random

lotto = set()

while len(lotto) < 6:
    lotto.add(random.randint(1, 45))

print(sorted(lotto))


import sys

print(sys.argv)
print(sys.argv[1:])

if "-h" in sys.argv or "--help" in sys.argv:
    print("사용법: python main.py [옵션]")
    print("-h, --help    도움말 표시")
    print("-v,--version  버전정보표시")
    sys.exit(0)

if "-v" in sys.argv or "--version" in sys.argv:
    print("버전 : 1.0.0")
    sys.exit(0)


import os

# dir_current = os.getcwd()
# print(dir_current)

# file__pass = os.chdir(dir_current)
# dir = os.popen('ls')
# print(dir.read())

# os.mkdir("test") #-> 폴더 생성
# os.rmdir("test") #-> 폴더 삭제

print(os.environ.get('PATH'))


import json

data = {
    "nanme": "홍길동",
    "age": 20,
    "city": "서울"
}

json_str = json.dumps(data)
print(json_str)

json_obj = json.loads(json_str)
print(json_obj)
'''
import random
import time

words = ["mountain", "river", "forest", "ocean", "desert",
         "tree", "flower", "cloud", "rain", "sunlight"]


def main():
    while True:
        select = input("영어 타자 연습 ('start'를 입력하면 시작합니다) : ")
        if select == "start":
            eng()
        else:
            print("프로그램을 종료합니다.")
            break


def eng():
    start_time = time.perf_counter()
    win = 0

    while True:
        rand_eng = random.choice(words)
        print(f"단어 : {rand_eng} ('exit'입력 시 종료)")
        ans = input("입력 : ")

        if ans == "exit":
            end_time = time.perf_counter()
            print("게임 종료!")
            return result(win, start_time, end_time)

        elif ans == rand_eng:
            win += 1
            print("통과")
            print()

        else:
            print("오타! 다시 시도하세요")
            print(f"단어 : {rand_eng} ('exit'입력 시 종료)")
            ans = input("입력 : ")

            if ans == "exit":
                end_time = time.perf_counter()
                print("게임 종료!")
                return result(win, start_time, end_time)

            elif ans == rand_eng:
                win += 1
                print("통과")
                print()

            else:
                print("두 번째 실패입니다.")
                continue

    return win, start_time, end_time


def result(win, start_time, end_time):
    total_time = end_time - start_time

    if win > 0:
        print(f"총 {win}개의 단어를 입력했습니다.")
        print(f"총 걸린시간 : {total_time:.2f}")
        print(f"단어 당 평균입력시간 : {(total_time / win):.2f}")
        print()
    else:
        print("한 개도 입력하지 못했습니다.")
        print()


main()
