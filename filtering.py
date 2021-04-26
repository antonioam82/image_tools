from tkinter import *
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

        Entry(self.root,textvariable=self.currentDir,width=150).place(x=0,y=0)
        Entry(self.root,textvariable=self.filename,font=('arial',23,'bold'),width=40).place(x=10,y=25)
        Button(self.root,text="SEARCH",height=2,width=25,bg="light blue1",command=self.open_file).place(x=709,y=25)
        Button(self.root,text="START",width=125,bg="light green",command=self.filter).place(x=10,y=85)

        self.root.mainloop()

    def open_file(self):
        self.fpath = filedialog.askopenfilename(initialdir = "/",
                 title = "Select File",filetypes = (("png files","*.png"),
                         ("jpg files","*.jpg"),("all files","*.*")))
        if self.fpath:
            self.filename.set(self.fpath.split("/")[-1])

    def filter(self):
        if self.fpath:
            try:
                img = cv.imread(self.fpath)
                kernel = np.ones((5,5),np.float32)/25
                dst = cv.filter2D(img,-1,kernel)
                cv.imshow("NEW",dst)
                cv.imwrite("NewImage.png",dst)
            except Exception as e:
                messagebox.showwarning("UNEXPECTED ERROR",str(e))
            
            
        


if __name__=="__main__":
    app()
    
