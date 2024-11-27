'''
# 클래스

# 클래스 정의


class Car:
    model = ""
    cc = 0

    def info(self):
        print(f"모델명 : {self.model}, 배기량 : {self.cc}cc")


# 사용
car1 = Car()  # 인스턴스 생성
car1.model = "싼타페"
car1.cc = 2000

# print(f"모델명 : {car1.model}")
# print(f"배기량 : {car1.cc}cc")

car1.info()

# 생성자


class Car:
    def __init__(self, model, cc):
        self.model = model
        self.cc = cc

    def __str__(self):
        return f"모델명 : {self.model}, 배기량 : {self.cc}cc"

    def info(self):
        print(f"모델명 : {self.model}, 배기량 : {self.cc}cc")


car1 = Car("싼타페", 2000)
# car1.info()
car2 = Car("bmw", 2200)
# car2.info()
print(car1)
print(car2)
print("== == == == == == == ==승용차 리스트 == == == == == == == ==")

cars = [
    Car("소나타", 2000),
    Car("쏘렌토", 3000),
    Car("아반떼", 1000)
]

for car in cars:
    print(car)



class Math:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plus(self, x, y):
        plus = self.x + self.y
        return plus

    def minus(self, x, y):
        minus = self.x - self.y
        return minus

    def multi(self, x, y):
        multi = self.x * self.y
        return multi

    def div(self, x, y):
        if self.y == 0:
            print("분모는 0이 될 수 없습니다.")
        return  self.x / self.y



ex1 = Math(2, 3)

print("plus :", ex1.plus())
print("minus :", ex1.minus())
print("multi :", ex1.multi())
print("div :", ex1.div())

# 클래스 변수와 인스턴스 변수


class Dog:
    kind = "진돗개"  # 클래스 변수

    def __init__(self, name):
        self.name = name  # 인스턴스 변수


dog1 = Dog("백구")
dog2 = Dog("초코")

print(dog1.name)  # 인스턴스 변수 출력

print(Dog.kind)  # 클래스 변수 출력



class Example:
    shared = "공유변수"

    def __init__(self, name):
        self.name = name


e1 = Example("A")
e2 = Example("B")
Example.shared = "변경된 공유 변수"

print(e1.shared)
print(e2.shared)

e1.name = "C"

print(e1.name)
print(e2.name)

# 사번 자동부여 클래스


class Employee:
    serial_num = 1000  # 클래스변수

    def __init__(self, name):
        Employee.serial_num += 1
        self.id = Employee.serial_num
        self.name = name

    def __str__(self):
        return f"사번 : {self.id}, 이름 : {self.name}"


e1 = Employee("홍길동")
print(e1)

e2 = Employee("임꺽정")
print(e2)

employees = [Employee("이몽룡"), Employee("심청"), Employee("변사또"), Employee("전우치")]

for employee in employees:
    print(employee)



class Supermarket:

    def __init__(self, location, name, product, customer):
        self.location = location
        self.name = name
        self.product = product
        self.customer = customer

    def print_location(self):
        return print(f"위치 : {self.location}")

    def change_category(self, change):
        self.product = change

    def show_list(self):
        return print(f"상품 : {self.product}")

    def enter_customer(self):
        self.customer += 1

    def show_info(self):
        return print(f"위치 : {self.name}, 이름 : {self.location}, 상품 : {self.product}, 고객수 : {self.customer}")


market1 = Supermarket("마포구 염라동", "마켓온", "음료", 12)

market1.print_location()
market1.show_list()
market1.show_info()
'''
# 정보은닉


class Person:
    def __init__(self):
        self._name = ""
        self._age = 0

    # 이름을 설정
    def setname(self, name):
        self._name = name

    # 이름을 출력
    def getname(self):
        return self._name

    # 나이를 설정
    def setage(self, age):
        self._age = age

    # 나이를 출력
    def getage(self):
        return self._age


p1 = Person()
p1.setname("홍길동")
print(p1.getname())
p1.setage(20)
print(p1.getage())
