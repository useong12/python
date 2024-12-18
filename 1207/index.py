import pandas as pd

name = ['홍길동', '임꺽정', '성춘향']
math = [85, 90, 78]
eng = [88, 76, 92]
sci = [95, 89, 84]

df = pd.DataFrame({
    '이름': name,
    '수학': math,
    '영어': eng,
    '과학': sci
})

# print(df)
# print()

new_data = {
    "이름": "이몽룡",
    '수학': 88,
    '영어': 85,
    '과학': 90
}

result = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
result.rename(columns={'수학': 'Math'}, inplace=True)
result.loc[result['이름'] == '임꺽정', "영어"] = 80
result["Total"] = result['Math']+result['영어']+result['과학']
print(result)
