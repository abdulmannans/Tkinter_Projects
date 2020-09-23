#Author Codemy.com Youtube Tutorial
from tkinter import *


#Functions
def btnClick(number):
    current = textbox.get()
    textbox.delete(0, END)
    textbox.insert(0, str(current)+str(number))

def btnClear():
    textbox.delete(0, END)

def btnEqual():
    sNum = 0 
    sNum = textbox.get()
    textbox.delete(0, END)

    if(math == "add"):
        textbox.insert(0, fNum + int(sNum))
    elif(math == "sub"):
        textbox.insert(0, fNum - int(sNum))
    elif(math == "mul"):
        textbox.insert(0, fNum * int(sNum))
    elif(math == "div"):
        textbox.insert(0, fNum / int(sNum))


def btnAdd():
    temp = textbox.get()
    global fNum 
    global math
    math = "add"
    fNum = int(temp)
    textbox.delete(0, END)

def btnSub():
    temp = textbox.get()
    global fNum 
    global math
    math = "sub"
    fNum = int(temp)
    textbox.delete(0, END)

def btnMul():
    temp = textbox.get()
    global fNum 
    global math
    math = "mul"
    fNum = int(temp)
    textbox.delete(0, END)

def btnDiv():
    temp = textbox.get()
    global fNum 
    global math
    math = "div"
    fNum = int(temp)
    textbox.delete(0, END)


#MainScreen
mainScreen = Tk()

mainScreen.title("Calculator")
mainScreen.iconbitmap(default="calc.ico")


textbox = Entry(mainScreen, width = 35, borderwidth = 5)
textbox.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

#buttons

btn_1 = Button(mainScreen, text = "1", padx = 40, pady = 20, command = lambda: btnClick(1))
btn_2 = Button(mainScreen, text = "2", padx = 40, pady = 20, command = lambda: btnClick(2))
btn_3 = Button(mainScreen, text = "3", padx = 40, pady = 20, command = lambda: btnClick(3))
btn_4 = Button(mainScreen, text = "4", padx = 40, pady = 20, command = lambda: btnClick(4))
btn_5 = Button(mainScreen, text = "5", padx = 40, pady = 20, command = lambda: btnClick(5))
btn_6 = Button(mainScreen, text = "6", padx = 40, pady = 20, command = lambda: btnClick(6))
btn_7 = Button(mainScreen, text = "7", padx = 40, pady = 20, command = lambda: btnClick(7))
btn_8 = Button(mainScreen, text = "8", padx = 40, pady = 20, command = lambda: btnClick(8))
btn_9 = Button(mainScreen, text = "9", padx = 40, pady = 20, command = lambda: btnClick(9))
btn_0 = Button(mainScreen, text = "0", padx = 40, pady = 20, command = lambda: btnClick(0))
btn_add = Button(mainScreen, text = "+", padx = 39, pady = 20, command = btnAdd)
btn_sub = Button(mainScreen, text = "-", padx = 40.5, pady = 20, command = btnSub)
btn_mul = Button(mainScreen, text = "/", padx = 40, pady = 20, command = btnDiv)
btn_div = Button(mainScreen, text = "*", padx = 41, pady = 20, command = btnMul)
btn_equal = Button(mainScreen, text = "=", padx = 91, pady = 20, command = btnEqual)
btn_clear = Button(mainScreen, text = "Clear", padx = 79, pady = 20, command = btnClear)


btn_1.grid(row = 3, column = 0)
btn_2.grid(row = 3, column = 1)
btn_3.grid(row = 3, column = 2)

btn_4.grid(row = 2, column = 0)
btn_5.grid(row = 2, column = 1)
btn_6.grid(row = 2, column = 2)

btn_7.grid(row = 1, column = 0)
btn_8.grid(row = 1, column = 1)
btn_9.grid(row = 1, column = 2)

btn_0.grid(row = 4, column = 0)
btn_clear.grid(row = 4, column = 1, columnspan = 2)

btn_add.grid(row = 5, column = 0)
btn_equal.grid(row = 5, column = 1, columnspan = 2)

btn_sub.grid(row = 6, column = 0)
btn_mul.grid(row = 6, column = 1)
btn_div.grid(row = 6, column = 2)


mainScreen.mainloop()
