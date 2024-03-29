from tkinter import *
from tkinter import filedialog
import pyexiv2
import os

class App:
    def __init__(self):
        self.window = Tk()
        self.window.title("Image Data")
        self.window.configure(bg="gray79")
        self.window.geometry("1175x570")

        self.currentDir = StringVar()
        self.currentDir.set(os.getcwd())
        self.filename = StringVar()

        canvas = Canvas(self.window,width=453,height=458)
        canvas.place(x=10,y=40)
        Entry(self.window,textvariable=self.currentDir,width=195).place(x=0,y=0)
        Entry(self.window,textvariable=self.filename,width=40,font=('arial',18)).place(x=473,y=40)
        Button(self.window,text="SEARCH",width=64).place(x=10,y=510)
        

        self.window.mainloop()

if __name__=="__main__":
    App()

