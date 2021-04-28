from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
import cv2 as cv
import numpy as np
import os

class app:
    def __init__(self):
        self.root = Tk()
        self.root.title("Filter")
        self.root.geometry("905x250")
        self.root.configure(bg="lavender")

        self.currentDir = StringVar()
        self.currentDir.set(os.getcwd())
        self.filename = StringVar()
        self.fpath = None
        self.element = None
        self.fr = 0
        self.nframes = 0

        Entry(self.root,textvariable=self.currentDir,width=158).place(x=0,y=0)
        Entry(self.root,textvariable=self.filename,font=('arial',23,'bold'),width=40).place(x=10,y=25)
        Button(self.root,text="SEARCH",height=2,width=25,bg="light blue1").place(x=709,y=25)
        Button(self.root,text="START",width=97,height=2,bg="light green").place(x=8,y=77)
        Button(self.root,text="SAVE",height=2,width=25,bg="light blue1").place(x=709,y=77)
        Label(self.root,text="FRAME RATE:",bg="lavender").place(x=709,y=150)
        self.frLabel = Label(self.root,bg='black',width=14)
        self.frLabel.place(x=790,y=150)
        Label(self.root,text="N FRAMES:",bg="lavender").place(x=721,y=190)
        self.nframesLabel = Label(self.root,bg='black',width=14)
        self.nframesLabel.place(x=790,y=190)

        self.root.mainloop()
            
            
        
if __name__=="__main__":
    app()

