'''
# 함수


def say_hello(born, name):
    age = 2024-born
    print(f"{name}님의 나이는 {age}세입니다.")


say_hello(1999, "***")


def gugudan(dan, end):
    print(f"[{dan}단]")
    for i in range(1, end+1):
        print(f"{dan}X{i}={dan*i}")


gugudan(5, 10)

# 결과값이 있는 함수


def calc_sum():
    total = 0
    for i in range(1, 11):
        total += i
    return total


result = calc_sum()
print(result)



def students():
    return {
        "name": "홍길동",
        "age": 20,
        "major": "컴퓨터공학"
    }


student = students()
print(student)



def same(x, y):
    if x == y:
        print(f"결과(곱):{x*y}")
    else:
        print(f"결과(합):{x+y}")


same(2, 2)
same(2, 3)



def dv(price):
    if price < 20000:
        price = price + 2500
        print(f"가격 : {price:,}원")

    else:
        print(f"가격 : {price:,}원")


dv(40000)
dv(12000)

def times(num):
    return [i**2 for i in num]

number = [2,3,6,9]

print(times(number))
'''


def check_machine():
    print(f"현재 남은 음료 : {vending_machine}")


def is_drink(buy):
    if buy in vending_machine:
        print(f"현재 {buy}는(은) 남아있습니다")
    else:
        print("재고가 없는 상품입니다.")


def add_drink():
    add = input("추가할 제품을 입력해주세요 : ")
    vending_machine.append(add)
    vending_machine.sort()


def remove_drink():
    erase = input("삭제할 제품을 입력해주세요 : ")
    if erase in vending_machine:
        vending_machine.remove(erase)
        print(f"{erase} 삭제 완료되었습니다.")
    else:
        print(f"현재 {erase}는 삭제 할 수 없습니다.")


vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']
while True:
    who = input("'소비자' 또는 '주인' 중 누구인지 알려주세요('종료'를 누르면 종료됩니다) : ")
    if who == '소비자':
        check_machine()
        buy = input("주문할 음료수를 입력해주세요 : ")
        is_drink(buy)
        if buy in vending_machine:
            vending_machine.remove(buy)
            print(f"{buy} 구매가 완료되었습니다.")
        else:
            print(f"현재 {buy}는 구매 할 수 없습니다.")
    elif who == '주인':
        act = input("'추가'또는'삭제'를 입력해주세요 : ")
        if act == "추가":
            add_drink()
            check_machine()
        elif act == "삭제":
            remove_drink()
            check_machine()
        else:
            continue
    elif who == '종료':
        break
    else:
        print("다시 입력해주세요")
        continue
