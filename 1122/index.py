''' 
s1 = {1, 2, 3, 3, 4}
print(s1)
s1.add(5)
print(s1)
s1.update([6, 7, 8, 9, 10])
print(s1)
s1.remove(9)
print(s1)
s1.discard(9)  # discard는 없는 내용을 삭제해도 오류 발생 x
print(s1)

# 합집합
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s3 = s1.union(s2)
print(s3)
s3 = s1 | s2
print(s3)

# 교집합
s3 = s1.intersection(s2)
print(s3)
s3 = s1 & s2
print(s3)

# 차집합
s3 = s1.difference(s2)
print(s3)
s3 = s1-s2
print(s3)

# dictionary
dict1 = {
    "name": "홍길동",
    "age": 18,
    "city": "seoul",
    "hobby": ["런닝", "등산", "헬스"]
}
dict2 = dict(name='홍길동', age=30, city='busan')
print(dict1)
print(dict2)

print(dict1['name'])
print(dict1['hobby'][2])

dict1["hobby"].append("캠핑")
print(dict1)

fruits = {
    'apple': '사과',
    'banana': '바나나',
}

print(fruits.get('apple'))
fruits.update({
    'grape': '포도',
    'melon': '멜론'
})
print(fruits)
print(fruits.keys())
print(fruits.values())
print(fruits.items())
fruits.clear()
print(fruits)

# 성적관리
score = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 95
}
print(score)
score.update({"David": 80, "Alice": 88})
print(score)
score.pop("Bob")
print(score)

numbers = [1, 2, 3, 4, 5]
print(sum(numbers))

scores = {"국어": 90, "영어": 80, "수학": 85}
print(sum(scores.values()))

# zip()
names = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 90, 88, 95]

zipped = list(zip(names, scores))
print(zipped)
'''
