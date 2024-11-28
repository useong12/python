'''
# 추상 클래스
from abc import ABC, abstractmethod


class PaymentSystem(ABC):

    # 추상 메서드 -> 선언만 하고 구현은 자식 클래스에서
    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def process_payment(self, amount):
        pass

    def payment_info(self, amount):
        print(f"{amount}원 결제가 완료되었습니다.")


class KakaoPay(PaymentSystem):
    def authenticate(self):
        print("카카오페이 인증완료")

    def process_payment(self, amount):
        print(f"카카오페이로 {amount}원을 결제합니다.")


pay = 50000
kakao = KakaoPay()
kakao.authenticate()
kakao.process_payment(pay)
kakao.payment_info(pay)


# 클래스 메서드 -> 인스턴스 생성 X


class Converter:
    conversion_rate = 1.60934

    @classmethod
    def mile_to_kilo(cls, mile):
        return mile*cls.conversion_rate


print(Converter.mile_to_kilo(7))



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2024 - birth_year
        return cls(name, age)


# 클래스 메서드를 통해서 객체를 생성
p1 = Person.from_birth_year("홍길동", 1990)
print(p1.name, p1.age)



class Counter:
    count = 0

    @classmethod
    def increament(cls):
        cls.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


Counter.increament()
print(Counter.get_count())

# 자식클래스의 정보 유지


class Animal:
    species = '동물'

    @classmethod
    def get_species(cls):
        return cls.species


class Dog(Animal):
    species = "진돗개"


print(Animal.get_species())
print(Dog.get_species())

# 정적메서드


class MathUtils:
    @staticmethod
    def add(a, b):
        return a+b

    @staticmethod
    def minus(a, b):
        return a-b


print(MathUtils.add(30, 40))
print(MathUtils.minus(10, 20))
'''
from abc import ABC, abstractmethod

electricity_usage = [
    {"date": "2024-11-01", "usage": 12.5},
    {"date": "2024-11-02", "usage": 15.3},
    {"date": "2024-11-03", "usage": 10.8},
    {"date": "2024-11-04", "usage": 14.2},
    {"date": "2024-11-05", "usage": 13.6}
]


class ElectricityData(ABC):

    def __init__(self, usage_data):
        self.__usage_data = usage_data
        self.__total_usage = self.calculate_total_usage()

    @abstractmethod
    def calculate_total_usage(self):
        pass

    @abstractmethod
    def get_usage_on_date(self, date):
        pass

    def add_usage(self, date, usage):
        new_data = {"date": date, "usage": usage}
        electricity_usage.append(new_data)
        print(electricity_usage)

    def remove_usage(self, date):
        for item in self._usage_data:
            if item["date"] == date:
                self._usage_data.remove(item)
                break

    @property
    def usage_data(self):
        return self.__usage_data

    @usage_data.setter
    def usage_data(self, value):
        self.__usage_data = value

    @property
    def total_usage(self):
        return self.__total_usage

    @total_usage.setter
    def total_usage(self, value):
        self.__total_usage = value


class HomeElectricityData(ElectricityData):

    def __init__(self, usage_data):
        super().__init__(usage_data)

    def calculate_total_usage(self):
        total = sum(item["usage"] for item in self._usage_data)
        print(f"총 전력 사용량 : {total}")
        return total

    def get_usage_on_date(self, date):
        for item in self._usage_data:
            if item["date"] == date:
                return item["usage"]
            else:
                None

    @classmethod
    def date_filter(cls, usage_data, start_date, end_date):
        filtered_data = [
            item for item in usage_data if start_date <= item["date"] <= end_date]
        print(f"특정 날짜 범위 내 사용량 : {filtered_data}")
        return filtered_data


class FindMinMAx:

    @staticmethod
    def max_usage(self):
        for item in electricity_usage:
            max_usage = item["usage"]
            if max_usage < item["usage"]:
                max_usage = item["usage"]


elec = HomeElectricityData(electricity_usage)
elec.calculate_total_usage()
