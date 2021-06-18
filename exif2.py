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

        canvas = Canvas(self.window,width=450,height=450)
        canvas.place(x=10,y=40)
        self.entryDir = Entry(self.window,textvariable=self.currentDir,width=195)
        self.entryDir.place(x=0,y=0)
        

        self.window.mainloop()

if __name__=="__main__":
    App()
