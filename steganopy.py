from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog
import tkinter.scrolledtext as sct
import cv2
import os
import numpy as np

class app():
    def __init__(self):
        self.window = Tk()
        self.window.title("Image Steganography")
        self.window.geometry("593x520")

        self.current_dir = StringVar()

        self.entryDir = Entry(self.window,width=98,textvariable=self.current_dir)
        self.entryDir.place(x=0,y=0)
        self.textEntry = sct.ScrolledText(self.window,width=70,height=15)
        self.textEntry.place(x=5,y=28)
        self.btnCopy = Button(self.window,text="COPY TEXT")
        self.btnCopy.place(x=5,y=277)
        self.btnClear = Button(self.window,text="CLEAR TEXT")
        self.btnClear.place(x=80,y=277)

        self.show_dir()

        self.window.mainloop()

    def show_dir(self):
        dirr = os.getcwd()
        self.current_dir.set(dirr)
        

if __name__=="__main__":
    app()

