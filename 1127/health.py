class Person:

    def __init__(self):
        self._name = ""
        self._hp = 100

    def workout(self, workout):
        print(f"{workout}시간 운동하다")
        if self._hp == 100:
            self._hp = 100
        else:
            self._hp += workout

    def drink(self, drink):
        print(f"술을 {drink}잔 마시다")
        if self._hp == 1:
            self._hp = 1
        else:
            self._hp -= drink

    def print_info(self):
        print(f"{self._name} - hp : {self._hp}")
        print("====================================")

    def set_hp(self, hp):
        self._hp = hp

    def get_hp(self):
        return self._hp

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


p1 = Person()
p1.set_name("나몸짱")
p1.workout(5)
p1.drink(2)
p1.print_info()

p2 = Person()
p2.set_name("나약해")
p2.workout(1)
p2.drink(12)
p2.print_info()
