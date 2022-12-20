import tkinter as tk
from signup import signup

def sign_f():
    signup(name.get())

def signupwindow():
    sign = tk.Toplevel(win)
    sign.geometry("300x100")
    sign.title("註冊")
    labelt = tk.Label(sign,text="註冊頁面")
    labelt.pack()
    page = tk.Frame(sign,padx=10,pady=10)
    page.pack()
    labeln = tk.Label(page,text="輸入姓名(使用英文):")
    labeln.grid(row=0)
    global name
    name = tk.StringVar()
    namein = tk.Entry(page, textvariable=name)
    namein.grid(row=0,column=1)
    btsign = tk.Button(sign,text="確認",padx=5,pady=5,command=sign_f)
    btsign.pack()
    sign.mainloop()

win = tk.Tk()
win.title("控制選單")
win.geometry("150x260")
frame1 = tk.Frame(win)
frame1.pack()
label1 = tk.Label(frame1, text="功能：")
label1.grid(row=0,column=0,padx=3,pady=5)
frame2 = tk.Frame(win,pady=3)
frame2.pack()
bt1 = tk.Button(frame2,text="登入",padx=17,pady=15)
bt2 = tk.Button(frame2,text="註冊",padx=17,pady=15,command=signupwindow)
bt3 = tk.Button(frame2,text="開啟鏡子",padx=5,pady=15)
bt4 = tk.Button(frame2,text="登出",padx=17,pady=15)
bt1.pack()
bt2.pack()
bt3.pack()
bt4.pack()

win.mainloop()