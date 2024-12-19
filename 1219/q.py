from bs4 import BeautifulSoup
import requests
from tkinter import *


def get_number(epi):
    url = f'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query={
        epi}%ED%9A%8C%20%EB%A1%9C%EB%98%90%EB%8B%B9%EC%B2%A8%EB%B2%88%ED%98%B8'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    number = soup.select_one(
        "#main_pack > div.sc_new.cs_lotto._lotto > div > div.content_wrap > div > div > div:nth-child(2) > div.win_number_box > div > div.winning_number")
    number = number.text
    bonus_number = soup.select_one(
        '#main_pack > div.sc_new.cs_lotto._lotto > div > div.content_wrap > div > div > div:nth-child(2) > div.win_number_box > div > div.bonus_number > span')
    bonus_number = bonus_number.text
    text.insert(END, f"당첨번호 : {number}\n보너스번호 : {bonus_number}")


def get_epi():
    epi = entry.get()
    get_number(epi)


window = Tk()
window.title("로또 당첨 확인")
window.geometry("480x240")

label1 = Label(window, text='당첨 회차 입력')
label1.grid(row=1, column=0, pady=10, sticky='w')

entry = Entry(window, width=40, bg='lightblue')
entry.grid(row=2, column=0)

button = Button(window, text='당첨 번호 확인', command=get_epi)
button.grid(row=3, column=0, sticky='e')

text = Text(window, width=40, height=10, bg='skyblue')
text.grid(row=4, column=0, rowspan=2)


window.mainloop()
