# while문
'''
i = 0
while i < 3:
    print("반복문")
    i += 1
print("종료")

num = 1
total = 0
while num <= 10:
    total += num
    num += 1
print(f"1부터 10까지의 합은 {total}입니다")

user_input = []
while user_input2 != "종료":
user_input2 = input("원하는 값을 입력하고 종료하려면 '종료'를 입력하세요")
user_input.append(user_input2)
print(f"입력한 값 : {user_input}")
print("프로그램이 종료되었습니다.")

while(True):
    dinner = input("오늘 저녁 뭐먹지?")
    if dinner == "제육":
        break
    print(f"오늘 저녁 메뉴는 {dinner}입니다.")
print("저녁 메뉴 완료")

count = 0
while (True):
    print(count, end=" ")
    count += 1
    if count == 10:
        break

count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count, end=" ")


while (True):
    user_input = input("양수를 입력해주세요('종료'입력 시 종료됩니다) : ")
    if user_input == "종료":
        print("프로그램을 종료합니다.")
        break
    elif user_input.isdigit() == False:
        print("숫자를 입력해주세요")
        continue
    else:
        user_input = int(user_input)
        if user_input == 0:
            continue
        elif user_input < 0:
            print("양수만 입력하세요")
            continue
        else:
            i = 0
            sum = 0
            while (i <= user_input):
                sum += i
                i += 1
        print(f"1부터 {user_input}까지의 합은 {sum}입니다.")

# for문
for i in range(10):
    print(i, end=" ")
print()
for i in range(3, 9):
    print(i, end=" ")
print()
for i in range(1, 100, 12):
    print(i, end=" ")

fruits = ['사과', '바나나', '포도', '체리']
for fruit in fruits:
    print(fruit, end=" ")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for num in numbers:
    total += num
print(f"합계는 {total}입니다.")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 != 0:
        print(num, end=' ')
'''
