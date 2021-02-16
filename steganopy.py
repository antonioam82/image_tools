from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog
import tkinter.scrolledtext as sct
import cv2
import numpy as np

class app():
    def __init__(self):
        self.window = Tk()
        self.window.title("Image Steganography")
        self.window.geometry("593x500")

        self.entryDir = Entry(self.window,width=98)
        self.entryDir.place(x=0,y=0)

        self.window.mainloop()

if __name__=="__main__":
    app()
