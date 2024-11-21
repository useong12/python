import sys
'''
#사이즈
print(getsizeof(1))
print(getsizeof("1"))

#형변환
print(type(1))
print(type("안녕하세요"))
print(type(True))
print(type(None))

num = input("숫자입력 : ")
a = int(num) % 2 == 0
print("False면 홀수, True면 짝수 : ", a)

print(int(5.5))
print(float(6))
a = "30"
print(type(int(a)))
print(type(a))

# 문자열 연산
a = "python"
print("안녕하세요 "+a+" 반갑습니다")
print("오류 "+str(1234))
print("hey!"*5)


korea_song = """
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산
대한사람 대한으로 길이 보전하세
"""
print(korea_song)

print("'오늘 뭐 먹지?'라고 생각하는 중이다")
print('"오늘 뭐 먹지?"라고 말하는 중이다')

# 이스케이프 문자
print("hello \nworld\nhello\tworld")
print('It\'s fish')
print("what's the \"fish\"")

# 문자열 포맷팅
year = "올해는 2024년 용띠의 해이다"
new_year = "올해는 %d년 %s의 해이다" % (2025, "뱀띠")
print(year)
print(new_year)

# 포맷코드 활용
age = "저는 올해 %d살 입니다" % (26)
print(age)
calc = "20 나누기 3 = %.2f입니다" % (20/3)
print(calc)
char = "이모티콘은%c 쓸게요" % "😒"
print(char)

# format() 예문
country = '대한민국'
city = '서울'
people = '한국인'
text = "저는 올해 {0}살입니다".format(20)
print(text)
text = "저는 {0} 사람이며 {1}에 살고 있습니다".format(country, city)
print(text)
text = "제가 사는 {0}은 {{{a}}}에 있습니다".format(city, a="한국")
print(text)
text = "{},{},{},{}".format(80, 90, 100, 200)
print(text)

a = "{0:!^20.7f}".format(20/3)
print(a)

# f문자열 포매팅
name = '홍길동'
age = 20
text = f"내 이름은 {name}이고 나이는 {age}입니다"
print(text)
print(f"내 이름은 {name} 나이는 {age+1}")

a = "{0:=^9}".format("조우성")
print(a)
print("문자열 실습입니다.{{{0}}}를 출력해보세요".format("중괄호"))
print(f"문자열 실습입니다.{{중괄호}}를 출력해보세요")

a = "20240930"
print(a[:4]+","+a[4:6]+","+a[6:])

a = "Hello, Python!"
print(len(a))
print(a.count('l'))
print(a.find('o'))
# index는 없는 문자를 찾을 경우 오류 발생, find는 -1로 표시, 대소문자도 구분

print(a.replace("Python", "파이썬"))
print(a)

a = "Hello, Python!"
print(a.split("l"))

a = "         hello           "
print(f"{a.strip()}")
print(a)

print("1234".isdecimal())
print("1234".isdigit())
print("1234".isnumeric())

print("hello".islower())
print("hello".isupper())

# 종합실습
name = input("이름을 입력하세요.")
age = input("나이를 입력하세요.")
print("안녕하세요!"+name+"님 "+"("+age+"세)")
print()

name = input("이름을 입력하세요.")
birth = input("태어난 년도를 입력하세요.")
year = input("올해 년도를 입력하세요.")
age = int(year)-int(birth)
print(age)
print("올해는 "+year+"년,"+name+"님의 나이는 "+str(int(year)-int(birth))+"세 입니다")
print(f"올해는 {year}년, {name}님의 나이는 {age}세 입니다")
'''
