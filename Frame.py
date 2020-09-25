# Author codemy.com Youtube Tutorial
from tkinter import *

mainScreen =Tk()

mainScreen.title("Frames")

Frame = LabelFrame(mainScreen, text="This My Frame!!", padx=5, pady=5)
Frame.pack(padx=10, pady=10)

btn = Button(Frame, text="Exit", command= mainScreen.quit)
btn.pack()

mainScreen.mainloop()