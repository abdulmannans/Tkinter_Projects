#Author Codemy.com Youtube Tutorial
#Modified By Abdul Mannan

from tkinter import *
from PIL import ImageTk,Image

global count
count = 0

def Forward():
    global imgLabel
    global btnFwd
    global btnBack
    global count
    count+=1
    if(count==5):
        count=0
    imgLabel.grid_forget()
    imgLabel = Label(image=imgList[count])
    imgLabel.grid(row = 0, column = 0, columnspan = 3)
    


def Backward():
    global imgLabel
    global btnFwd
    global btnBack
    global count
    count-=1
    if(count<=0):
        count=5
    imgLabel.grid_forget()
    imgLabel = Label(image=imgList[count])
    imgLabel.grid(row = 0, column = 0, columnspan = 3)

mainScreen = Tk()
mainScreen.title("Image Viewer")

icoloca = "d:/python/tkinter projects/imageviewer/viewer.ico"
mainScreen.iconbitmap(default=icoloca)

img1loca = "d:/python/tkinter projects/imageviewer/1.jpg"
img2loca = "d:/python/tkinter projects/imageviewer/2.jpg"
img3loca = "d:/python/tkinter projects/imageviewer/3.jpg"
img4loca = "d:/python/tkinter projects/imageviewer/4.jpg"
img5loca = "d:/python/tkinter projects/imageviewer/5.jpg"
img6loca = "d:/python/tkinter projects/imageviewer/6.jpg"

img1 = ImageTk.PhotoImage(Image.open(img1loca))
img2 = ImageTk.PhotoImage(Image.open(img2loca))
img3 = ImageTk.PhotoImage(Image.open(img3loca))
img4 = ImageTk.PhotoImage(Image.open(img4loca))
img5 = ImageTk.PhotoImage(Image.open(img5loca))
img6 = ImageTk.PhotoImage(Image.open(img6loca))

imgList = [img1, img2, img3, img4, img5, img6]

imgLabel = Label(image=img1)
imgLabel.grid(row = 0, column = 0, columnspan = 3)

btnBack = Button(mainScreen, text="<<", command = Backward)
btnExit = Button(mainScreen, text="Exit Program", command= mainScreen.quit)
btnFwd = Button(mainScreen, text=">>", command= Forward)

btnBack.grid(row = 1, column = 0)
btnExit.grid(row = 1, column = 1)
btnFwd.grid(row =1, column=2)


mainScreen.mainloop()
