from tkinter import *

count = 0

def count_plus():
    global count
    count += 1
    label.config(text=str(count))

def count_minus():
    global count
    count -= 1
    label.config(text=str(count))


button1 = Button(root, width=10,text='plus',overrelief='solid', command=count_plus)
button1.pack()

button2 = Button(root, width=10,text='minus',overrelief='solid', command=count_minus)
button2.pack()
# 창 띄우기
# root.title('opt window')                      # 창 이름 설정
# root.geometry('300x200+300+300')              # 창 크키 + 창 좌표 설정
# root.resizable(False,False)       # 창 크기 변경 가능 여부
#
# # 창에 글씨 쓰기
# label = Label(root, text="Hello TKINTER")    # 레이블 생성
# label.pack()                                 # 레이블을 화면에 배치

root.mainloop()                              # 화면 호출

