"""
print()함수
print("안녕하세요")
print("Hello", "Python")
print("Hello", "Python", sep="|")
print("안녕하세요", end="/")
print("저는 000입니다.")
print(1111111)


# input() 함수
# singer = input("좋아하는가수는? ")
# print("좋아하는 가수는 ", singer, "입니다")
"""
# 한 줄 주석에 사용. 코드뒤에서도 사용가능

'''
# 변수
x = 10
print("before x", x, id(x))
# y, z = 3.14, "안녕하세요"
# print("y", y)
# print("z", z)
x = "반갑습니다"
print("after x", x, id(x))
# x = 10
# print("x", x)

a = [1, 2, 3]
print("before a", a,  id(a))
a.append(4)
print("after a", a,  id(a))

# 키워드
import keyword
# print(keyword.kwlist)

# x = 48 / 2 (9 + 3)
# print(x)

# x = (100 - 2) / 7 + (9 * 3)
# print(x)

# 복합대입연산자
# num = 5
# # += 5 ===> num = num + 5
# num += 5
# print("+=", num)
# num -= 2  # num = num - 2
# print("-=", num)
# num *= 6  # num = num * 6
# print("*=", num)
# num /= 2  # num = num / 2
# print("/=", num)
# num //= 5  # num = num // 5
# print('//=', num)
# num %= 3  # num = num % 3
# print('%=', num)
# num = 4
# num **= 4  # num = num ** 4
# print('**=', num)

# 비교연산자
# num1 = 10
# num2 = 20
# num3 = "10"
# print(num1 > num2)
# print(num1 < num2)
# print(num1 == num3)
# print(num1 >= 10)
# print(num2 <= 19)
# print(num1 != num3)

# 논리연산자
# a = 2 > 1  # True
# b = 3 < 2  # False
# c = 1 == 1  # True
# d = 3 >= 4  # False
# print(a and c)  # True
# print(a and d)  # False
# print(b or c)  # True
# print(b or d)  # False
# print(not a)  # False
# print(not d)  # True


# in 연산자
a = "hello world"
print("H" in a)  # False
print("h" in a)  # True
print("a" not in a)  # True
print("w" not in a)  # False
'''


# 실습. 연산자 연습
num = 30
a = num % 2 == 0
print("True면짝수, False면 홀수: ", a)
