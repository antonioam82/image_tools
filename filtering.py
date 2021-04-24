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

        Entry(self.root,textvariable=self.currentDir,width=150).place(x=0,y=0)

        self.root.mainloop()


if __name__=="__main__":
    app()
    
