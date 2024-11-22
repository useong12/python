'''
age = 15

if age < 20:
    print("미성년자입니다")
print(f"나이는 {age}입니다")

password = "abc123"
a = input("비밀번호를 입력하세요: ")
if a == password:
    print("비밀번호가 맞습니다")
else:
    print("비밀번호가 틀립니다")

num = input("숫자를 입력하세요: ")
if int(num) % 2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")

# elif
age = int(input("나이를 입력하세요:"))

if age < 20:
    print("10대입니다")
elif age < 30:
    print("20대입니다")
elif age < 40:
    print("30대입니다")
elif age < 50:
    print("40대입니다")
else:
    print("50대 이상입니다")

score = int(input("점수를 입력하세요 : "))

if score >= 90:
    print("학점 : A")
elif score >= 80:
    print("학점 : B")
elif score >= 70:
    print("학점 : C")
elif score >= 60:
    print("학점 : D")
else:
    print("학점 : F")

age = int(input("나이를 숫자로 입력해주세요 : "))

if age <= 0:
    print("나이를 입력해주세요")
elif age < 8 or age > 75:
    print(f"{age}세의 요금은 무료입니다")
elif age < 14:
    print(f"{age}세의 요금은 450원입니다")
elif age < 20:
    pay = input("결제 방법을 입력해주세요 : ")
    if pay == "카드":
        print(f"{age}의 {pay}요금은 720원입니다")
    else:
        print(f"{age}의 {pay}요금은 1000원입니다")
elif age < 75:
    pay = input("결제 방법을 입력해주세요 : ")
    if pay == "카드":
        print(f"{age}의 {pay}요금은 1200원입니다")
    else:
        print(f"{age}의 {pay}요금은 1300원입니다")

# 삼항연산자
age = int(input("나이를 입력하세요 : "))
message = "20대입니다" if age < 30 and age >= 20 else "20대가 아닙니다"
print(message)

age = int(input("나이를 입력하세요 : "))
message = "20대입니다" if age < 30 and age >= 20 else "30대입니다" if age >= 30 and age < 40 else "2,30대가 아닙니다"
print(message)

# 조건문에서 in연산자
fruit = input("과일 이름을 한글로 입력하세요 : ")

if fruit in ['사과', '복숭아', '바나나']:
    print(f"{fruit}은(는) 과일에 포함되어 있습니다")
else:
    print("존재하지 않는 과일입니다")

fruits = {
    "apple": 95,
    "banana": 105,
    "cherry": 50
}

fr = input("과일을 영문으로 입력하세요 : ")
if fr in fruits:
    print(f"{fr}의 칼로리는 {fruits[fr]}Kcal입니다.")
else:
    print("포함되지 않은 과일입니다.")
'''
