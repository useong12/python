'''
number = [1, 2, 3, "hello", "python"]
print(number[3])
print(number[0])

text = "Hello, Python"
text = list(text)
print(text)

shop = ['반팔', '청바지', '이어폰', ['무선키보드', '기계식키보드']]
print(shop[2])
print(shop[3][0])
shop[0] = '긴팔'
print(shop[0])

a = [1, 2, 3]
b = ['a', 'b', 'c']
c = a+b
print(c)
print(b*3)

# 정렬함수
num = [3, 1, 5, 2]
num_asc = sorted(num)
print(num_asc)
num_desc = sorted(num, reverse=True)
print(num_desc)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)

korean = ['강', '이', '박', '최', '김']
korean.sort()
print(korean)
korean.sort(reverse=True)
print(korean)

alpabet = ['b', 'c', 'a', 'd']
alpabet.reverse()
print(alpabet)
print(alpabet.index('c'))

a = ['a', 'b', 'c', "안녕", "hi"]
a.append("Good")
print(a)
a.pop()
print(a)
a.remove("안녕")
print(a)
a.insert(2, "잘가")
print(a)
a.clear()
print(a)

x = ['q', 'w', 'e', 'r', 'w']
print(x.count('w'))

rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
print(rainbow[2])
rainbow.sort()
print(rainbow)
rainbow.append("gray")
print(rainbow)
del rainbow[3:7]
print(rainbow)

# 이차원 리스트
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[2][0])
# 요소 추가
matrix[1] = matrix[1]+[99]
print(matrix)

# 행  추가
matrix = matrix+[[10, 11, 12]]
print(matrix)

# 요소 수정
matrix[0][0] = 100
matrix[1][1] = 500
print(matrix)
del matrix[1][3]
print(matrix)

# 행의 개수
rows = len(matrix)
print(rows)
cols = len(matrix[0])
print(cols)

# 이차원 메서드
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix[0].append(10)
matrix[1].append(20)
matrix[2].append(30)
print(matrix)

matrix.append([40, 50, 60, 70])
print(matrix)

matrix[0].extend([11, 12])
print(matrix)

# 튜플
t1 = (1,)
t2 = (1, 2, 3, 4, 3, 5, 3, 6)
t3 = 1, 2, 3

print(t1[0])
print(t2.count(3))
print(t2.index(2))
'''
# set
s1 = {1, 1, 1, 1, 1, 1, 1, 11, 111, 1111, 11, 11, 111, 111, 11, 111}
print(s1)
s2 = set(['안녕', '잘가', 'Hi', '안녕', '잘가'])
print(s2)
