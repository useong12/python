# 쿠폰 추첨기
from tkinter import *
import random


window = Tk()
window.title("쿠폰추첨기")
window.geometry("640x480")

# # # 이미지 넣기
# label_img = Label(window)
# img = PhotoImage(file='')
# label_img.config(image=img)
# label_img.pack()

# 추첨버튼


def on_click():
    name_list = ["1", '2', '3', '4', '5', '6']
    win = []

    name = random.sample(name_list, 2)
    text.delete("1.0", END)
    text.insert(END, name)


Button(window, text='추첨', command=on_click).pack()

# 출력
text = Text(window, width=40, height=5, bg='yellow')
text.pack()

window.mainloop()
