# window programing
from tkinter import messagebox
from tkinter import *


root = Tk()
root.title("윈도우 프로그래밍 연습")
root.geometry("640x480")

# 기본 창 띄우기
# label = Label(root, text='안녕하세요')
# label.pack(side="left")

# layout pack() 방식

# label1 = Label(root, text='TOP', bg='red', fg='white')
# label1.pack(side="top", fill="x", padx=10, pady=10)

# label2 = Label(root, text='BOTTOM', bg='blue', fg='white')
# label2.pack(side='bottom', fill='x', padx=10, pady=10)

# label3 = Label(root, text='Left', bg='green', fg='white')
# label3.pack(side='left', fill='y', padx=10, pady=10)

# label4 = Label(root, text='right', bg='yellow', fg='black')
# label4.pack(side='right', fill='y', padx=10, pady=10)

# label5 = Label(root, text='center', bg='purple', fg='white')
# label5.pack(side='top', fill='both', expand=True, padx=10, pady=10)

# # layout grid 방식
# label1 = Label(root, text='Label1', bg='red', fg='white')
# label1.grid(row=0, column=0, padx=10, pady=10)

# label2 = Label(root, text='Label2', bg='blue', fg='white')
# label2.grid(row=1, column=1, padx=10, pady=10)

# label3 = Label(root, text='Label3', bg='green', fg='white')
# label3.grid(row=2, column=2, padx=10, pady=10)

# label4 = Label(root, text='Label4', bg='yellow', fg='black')
# label4.grid(row=3, column=3, padx=10, pady=10)

# label5 = Label(root, text='Label5', bg='purple', fg='black')
# label5.grid(row=8, column=8, rowspan=2,columnspan=2 padx=10, pady=10)

# label1 = Label(root, text='Hello,Tkinter', font=('Pretendard', 20), fg='blue')
# label1.pack()

# 버튼 만들기


# def on_click():
#     print("button clicked")


# button = Button(root, text="button", command=on_click, bg='blue', fg='white')
# button.pack()

# # 단일 텍스트 입력
# def show_text():
#     # entried = entry.get()
#     # label.config(text=f"입력된 문자 : {entried}")
#     # entry.delete(0, END)  # 엔트리에 있는 문자열 입력 후 삭제
#     print(text.get("1.0", END))


# text = Text(root, width=40, height=10) # 텍스트는 여러 줄에 사용
# text.pack()

# # entry = Entry(root, width=30)
# # entry.pack()

# button = Button(root, text='버튼 클릭', command=show_text)
# button.pack(side='left')

# label = Label(root, text='')
# label.pack(side='top')

# # 프레임
# top_frame = Frame(root, bg='lightblue')
# top_frame.pack(side='top', fill='x')
# Label(top_frame, text='탑 프레임').pack(pady=50)

# bottom_frame = Frame(root, bg='lightgreen')
# bottom_frame.pack(fill='both', expand=True)
# Label(bottom_frame, text='바텀 프레임').pack(pady=50)

# 체크 버튼
# def show_state():
#     print("check는 ", var.get())


# var = IntVar()
# checkbtn = Checkbutton(root, text='동의합니다', variable=var, command=show_state)
# checkbtn.pack()

# # 라디오 버튼
# var = StringVar(value="option1")


# def show_choice():
#     print("선택 : ", var.get())


# radio1 = Radiobutton(root, text='option1', variable=var,
#                      value="option1", command=show_choice)
# radio1.pack(pady=10)

# radio2 = Radiobutton(root, text='option2', variable=var,
#                      value="option2", command=show_choice)
# radio2.pack(pady=10)

# 리스트 박스
# listbox = Listbox(root)
# listbox.pack(pady=10)


# def show_select():
#     selection = listbox.curselection()
#     if selection:
#         print(f"선택된 과일은 {listbox.get(selection[0])} 입니다.") # -> 이 부분 이해 안됌


# for item in ['사과', '바나나', '포도', '체리']:
#     listbox.insert(END, item) # -> 이 부분 이해 안됌

# button = Button(root, text='선택', command=show_select)
# button.pack(pady=10)

# 메세지창
# def show_info():
#     messagebox.showinfo("경고", "메세지창 띄우기")


# button = Button(root, text='메세지창', command=show_info)
# button.pack(pady=10)

# 메뉴

# def new_file():
#     messagebox.showinfo("메뉴", "파일이 선택되었습니다")


# def exit_app():
#     root.quit()


# menubar = Menu(root)

# filemenu = Menu(menubar, tearoff=0)

# filemenu.add_command(label="New", command=new_file)
# filemenu.add_separator()
# filemenu.add_command(label='exit', command=exit_app)

# menubar.add_cascade(label='파일', menu=filemenu)
# root.config(menu=menubar)


root.mainloop()
