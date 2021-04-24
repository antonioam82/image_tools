from tkinter import *
import cv2 as cv
import os

class app:
    def __init__(self):
        self.root = Tk()
        self.root.title("Filter")
        self.root.geometry("905x400")

        self.currentDir = StringVar()
        self.currentDir.set(os.getcwd())
        self.filename = StringVar()

        Entry(self.root,textvariable=self.currentDir,width=150).place(x=0,y=0)
        Entry(self.root,textvariable=self.filename,font=('arial',23,'bold'),width=40).place(x=10,y=25)
        Button(self.root,text="SEARCH",height=2,width=25).place(x=707,y=25)

        self.root.mainloop()

if __name__=="__main__":
    app()
    
