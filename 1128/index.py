'''
# 상속 (부모클래스에 생성자가 없을 때)


class Animal:
    def speak(self):
        print("동물이 소리를 냅니다.")

    def move(self):
        print("동물이 움직입니다.")


class Cat(Animal):
    def meow(self):
        print("야옹")


cat = Cat()
cat.speak()
cat.move()
cat.meow()


# 상속 (부모클래스에 생성자가 있을 때)


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}이 소리를 냅니다.")

    def move(self):
        print(f"{self.name}이 움직입니다.")


class Cat(Animal):
    def __init__(self, name, sound="야옹"):
        super().__init__(name)
        self.sound = sound

    def meow(self):
        print(f"{self.name}가 \"{self.sound}\" 소리를 냅니다")


cat = Cat("장화")
cat.speak()
cat.move()
cat.meow()

# 다중상속


class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower


class Wheel:
    def __init__(self, count):
        self.count = count


class Car(Engine, Wheel):
    def __init__(self, horsepower, count):
        Engine.__init__(self, horsepower)
        Wheel.__init__(self, count)

    def info(self):
        print(f"이 자동차는 {self.horsepower}마력과 {self.count}개의 바퀴를 가지고 있습니다.")


car = Car(100, 4)
car.info()

# 오버라이딩


class Parent:
    def greet(self):
        print("안녕하세요.부모클래스")


class Child(Parent):
    def greet(self):
        super().greet()  # 부모클래스 greet함수 호출
        print("안녕하세요.자식클래스")


p = Parent()
p.greet()
print()

c = Child()
c.greet()
'''


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # 재고 업데이트 메서드
    def update_quantity(self, amount):
        self.quantity += amount
        print(f"{self.name} 재고가 {amount}만큼 {'증가' if amount >
              0 else '감소'}했습니다. 현재 재고: {self.quantity}")

    # 상품 정보 출력 메서드
    def display_info(self):
        print(f"상품명: {self.name}")
        print(f"가격: {self.price:,}원")
        print(f"재고: {self.quantity}개")


class Electronic(Product):
    def __init__(self, name, price, quantity, warranty_period='12'):
        super().__init__(name, price, quantity)
        self.warranty_period = warranty_period

    def extend_warranty(self, month):
        self.warranty_period = self.warranty_period + month
        print(f"보증 기간이 {month}개월 늘어났습니다. 현재 보증 기간 : {self.warranty_period}개월")

    def display_info(self):
        super().display_info()
        print(f"보증기간: {self.warranty_period}개월")


class Food(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date

    def is_expired(self, date):
        if date > self.expiration_date:
            print(f"{self.name}은(는) 유통기한이 지났습니다.")
        else:
            print(f"{self.name}은(는) 유통기한이 지나지 않았습니다.")

    def display_info(self):
        super().display_info()
        print(f"유통기한: {self.expiration_date}")


elec = Electronic("스마트 TV", 1500000, 5, 24)
food = Food("사과", 3000, 50, "2025-03-12")

elec.display_info()
elec.extend_warranty(12)
elec.display_info()
print()

food.is_expired("2024-11-28")
food.is_expired("2025-11-28")
food.display_info()
