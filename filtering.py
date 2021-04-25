from tkinter import *
from tkinter import filedialog
import cv2 as cv
import os

class app:
    def __init__(self):
        self.root = Tk()
        self.root.title("Filter")
        self.root.geometry("905x400")
        self.root.configure(bg="lavender")

        self.currentDir = StringVar()
        self.currentDir.set(os.getcwd())
        self.filename = StringVar()

        Entry(self.root,textvariable=self.currentDir,width=150).place(x=0,y=0)
        Entry(self.root,textvariable=self.filename,font=('arial',23,'bold'),width=40).place(x=10,y=25)
        Button(self.root,text="SEARCH",height=2,width=25,bg="light blue1",command=self.open_file).place(x=709,y=25)
        Button(self.root,text="START",width=125,bg="light green").place(x=10,y=85)

        self.root.mainloop()

    def open_file(self):
        fpath = filedialog.askopenfilename(initialdir = "/",
                 title = "Select File",filetypes = (("png files","*.png"),
                         ("jpg files","*.jpg"),("all files","*.*")))
        if fpath:
            self.filename.set(fpath.split("/")[-1])


if __name__=="__main__":
    app()
    
    
