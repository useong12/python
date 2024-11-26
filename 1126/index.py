'''
# 전역변수
quantity = 10


def get_price(price):
    price = price * quantity
    return price


print(f"{quantity}개의 가격은 {get_price(2000)}입니다.")


def oneUP():
    x = 0
    x += 1
    return x


print(oneUP())

# 유효범위
quantity = 10


def price_sum(price):
    quantity = 7
    return price * quantity


print(price_sum(2000))

x = 0


def oneUp():
    global x
    x += 1
    return x


print(oneUp())
print(oneUp())
print(oneUp())

# 기본 매개변수


def pr_str(txt="안녕하세요", count=1):
    for _ in range(count):
        print(txt)


pr_str()
pr_str("Hello", 5)
pr_str("Hi")

# 함수 호출기법


def intro(name, age, city):
    print(f"이름은 {name}, 나이는 {age}, 사는 곳은 {city}입니다.")


intro("홍길동", 23, "서울")
intro(city="서울", name="임꺽정", age=25)

# 가변 매개변수


def calc_avg(*args):
    print(args)
    total = 0
    for i in args:
        total += i
    avg = total/len(args)
    return avg


print(calc_avg(1, 2, 3, 4, 5, 6, 7, 8))



def text_def(a, *args):
    print("text : ", a)
    print("args : ", args)


text_def("hi", 1, 2, 3, 4, 5)



def intro(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


intro(name="홍길동", age=20, city="서울", gender="남자")

# 내장함수


def my_abs(x):
    if x < 0:
        return -x
    else:
        return x


print(my_abs(-10))
print(my_abs(8))
print(abs(-8))

# 거듭제곱
print(pow(2, 3))


def my_pow(x, y):
    num = 1
    for i in range(y):
        print(f"{i}번째 실행,{num}X{x}={num*x}")
        num *= x
    return num


my_pow(2, 3)

# map


def square(x):
    return x ** 3


numbers = [2, 4, 6, 8]

squared = list(map(square, numbers))
print(squared)
# filter


def even_number(x):
    if x % 2 == 0:
        return x
    #return x%2 == 0 -> 필터는 반환값 true/false로 해야함


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(filter(even_number, numbers)))


def get_return():
    arr = ["사과", "바나나"]
    dic = {
        "name": "홍길동",
        "age": 28
    }
    num = 30
    return arr, dic, num  # 한번에 반환 가능


arrs, dics, nums = get_return() # 받는 쪽에서 순서대로 받아야 함
print(arrs)
print(dics)
print(nums)

nums = list(range(1, 31))


def times(x):
    sum = 0
    for num in nums:
        if num % x == 0:
            sum += 1
            print(num, end=' ')
    print()
    print(f"{x}의 배수의 개수 : {sum}")


times(3)
times(2)
times(6)

# 중첩함수
nums = list(range(1, 31))


def result(x):
    x_times = []

    def times(x):
        for num in nums:
            if num % x == 0:
                x_times.append(num)

    times(x)
    print(x_times)
    print(f"{x}의 배수의 개수 : {len(x_times)}")


result(3)



def sos(i):
    print(f"help me , {i}")
    if i == 1:
        return ""
    else:
        return sos(i-1)


sos(10)



def factorial(n):
    print(f"{n}의 값 : {n}")
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


print(factorial(5))


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


print(fibonacci(21))

# lambda


def add(x, y): return x+y


print(add(1, 2))

print((lambda x, y: x+y)(2, 3))

print((lambda x: x+1)(1))
print((lambda x: x**2)(4))


def call(func):
    for _ in range(10):
        func()


def hello():
    print("안녕하세요")


def hello2(): return print("반갑습니다")


call(hello)

numbers = [2, 4, 6, 8]
squared = map(lambda x: x**3, numbers)
print(list(squared))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(lambda x: x % 2 == 0, numbers)))
'''
