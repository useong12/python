'''
# for문
fruits = ["사과", "포도", "바나나", "복숭아"]
for fruit in fruits:
    print("과일은 : ", fruit)

# 합계구하기
number = [10, 20, 30, 40, 50]
total = 0
for num in number:
    total += num
print(f"리스트 값의 합계는 {total}입니다.")

# 조건문
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in number:
    if num % 2 == 0:
        print(num, end=' ')

# 리스트 내 for문
squares = [i**2 for i in range(1, 20)]
print(squares)

even_squares = [i**2 for i in range(1, 10) if i % 2 == 0]
print(even_squares)

# dictionary(***keys,values,items)
my_dic = {
    "name": "홍길동",
    "address": "서울시 은평구",
    "gender": "남자",
    "hobby": ["런닝", "헬스", "낚시"]
}

for i in my_dic:
    print(i)
print()
for i in my_dic.keys():
    print(i)
print()
for i in my_dic.values():
    print(i)
print()
for i, j in my_dic.items():
    print(f"key 값은 {i}, value 값은 {j}")
# JSON이 dict형태임

# 구구단

while True:
    x = input("몇 단을 출력할까요 : ")

    if x.isdigit() == 0:
        print("0~9의 숫자를 입력해주세요")
        continue

    x = int(x)
    for i in range(1, 10):
        print(f"{x} X {i} = {x*i}")
    break


while True:
    x = input("어디까지 계산할까요? : ")

    if x.isdigit() == 0:
        print("숫자를 입력해주세요")
        continue

    x = int(x)
    sum = 0
    for i in range(1, x):
        if x % 2 == 1:
            sum += x
    print(f"1부터 {x}까지의 홀수의 합 : {sum}")
    break


students = {
    "student1":  {
        "korean": 83,
        "english": 92,
        "math": 88
    },

    "student2":  {
        "korean": 90,
        "english": 79,
        "math": 86
    },

    "student3":  {
        "korean": 88,
        "english": 86,
        "math": 94
    }
}
average_scores = {}

# 각 학생의 점수를 순회
for student, scores in students.items():
    print(student)
    print()
    print(scores)
    # 각 학생의 과목 점수 합계
    total_score = sum(scores.values())
    # 과목 수
    num_subjects = len(scores)
    # 평균 점수 계산
    average = total_score / num_subjects
    # 평균 점수를 딕셔너리에 저장
    average_scores[student] = average

# 결과 출력
# print(average_scores)

# 이중 for문
for i in range(5):
    for j in range(3):
        print(f"{i}:i,j:{j}")
    print()

matrix = [
    [3, 6, 9, 12],
    [2, 4, 6, 8],
    [10, 20, 30, 40],
    [11, 12, 13, 14]
]

total = 0
for row in matrix:
    for col in row:
        if col % 3 == 0:
            total += col
            print(col, end=' ')
print(total)

for i in range(2, 10):
    print(f"[{i}단]")
    for j in range(1, 10):
        print(f"{i} X {j} = {i*j}")
    print()
'''
vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']
while True:

    who = input("'소비자' 또는 '주인' 중 누구인지 알려주세요('종료'를 누르면 종료됩니다) : ")
    if who == '소비자':
        print(vending_machine)
        buy = input("주문할 음료수를 입력해주세요 : ")
        if buy in vending_machine:
            vending_machine.remove(buy)
            print(f"{buy} 구매가 완료되었습니다.")
        else:
            print(f"현재 {buy}는 구매 할 수 없습니다.")

    elif who == '주인':
        while True:
            act = input("'추가'또는'삭제'를 입력해주세요 : ")
            if act == "추가":
                print(vending_machine)
                add = input("추가할 제품을 입력해주세요 : ")
                vending_machine.append(add)
                vending_machine.sort()
                print(vending_machine)

            elif act == "삭제":
                erase = input("삭제할 제품을 입력해주세요 : ")
                if erase in vending_machine:
                    vending_machine.remove(erase)
                    print(f"{erase} 삭제 완료되었습니다.")
                else:
                    print(f"현재 {erase}는 삭제 할 수 없습니다.")
            else:
                print("잘못된 입력입니다.")
                continue

    elif who == '종료':
        break

    else:
        print("다시 입력해주세요")
        continue
