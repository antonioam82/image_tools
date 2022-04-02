#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox, filedialog
import cv2
import os
import matplotlib.pyplot as plt
import numpy as np

class Histogram:
    def __init__(self):
        self.window = Tk()
        self.window.title("Image Histogramas")
        self.window.geometry("717x280")
        
        currentDir = StringVar()
        currentDir.set(os.getcwd())
        self.image_name = StringVar()

        Entry(self.window,textvariable=currentDir,width=119).place(x=0,y=0)
        Entry(self.window,textvariable=self.image_name,width=32,font=("arial",23)).place(x=10,y=40)
        Button(self.window,text="SEARCH IMAGE",height=2,width=18).place(x=570,y=40)
        Button(self.window,text="PLOT HISTOGRAM",height=2,width=98).place(x=10,y=100)
        Button(self.window,text="PLOT CHANNELS HISTOGRAM",height=2,width=98).place(x=10,y=153)

        self.window.mainloop()

if __name__=="__main__":
    Histogram()
