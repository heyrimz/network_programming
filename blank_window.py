from tkinter import *
root = Tk()



root.title('opt window')                      # 창 이름 설정
root.geometry('300x200+300+300')              # 창 크키 + 창 좌표 설정
root.resizable(False,False)       # 창 크기 변경 가능 여부

label = Label(root, text="Hello TKINTER")    # 레이블 생성
label.pack()                                 # 레이블을 화면에 배치

root.mainloop()                              # 화면 호출

