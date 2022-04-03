#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox, filedialog
import cv2
import os
import threading
import matplotlib.pyplot as plt
import numpy as np

class Histogram:
    def __init__(self):
        self.window = Tk()
        self.window.title("Image Histogramas")
        self.window.geometry("717x167")
        
        currentDir = StringVar()
        currentDir.set(os.getcwd())
        self.image_name = StringVar()
        self.image = ""

        Entry(self.window,textvariable=currentDir,width=119).place(x=0,y=0)
        Entry(self.window,textvariable=self.image_name,width=32,font=("arial",23)).place(x=10,y=40)
        Button(self.window,text="SEARCH IMAGE",height=2,width=18,bg="gray80",command=self.open_file).place(x=570,y=40)
        Button(self.window,text="SHOW IMAGE",height=2,width=18,bg="gray80",command=self.show_image).place(x=570,y=100)
        Button(self.window,text="PLOT HISTOGRAM",height=2,width=37,bg="gray87").place(x=10,y=100)
        Button(self.window,text="PLOT CHANNELS HISTOGRAM",height=2,width=37,bg="gray87",command=self.channels_hist).place(x=289,y=100)

        self.window.mainloop()

    def open_file(self):
        self.image = filedialog.askopenfilename(initialdir="/",title="SELECT FILE",
                        filetypes=(("jpg files","*.jpg"),("png files","*.png")))
        if self.image:
            self.image_name.set(self.image)

    def show_image(self):
        if self.image != "":
            image = cv2.cvtColor(cv2.imread(self.image), cv2.COLOR_RGB2BGR)
            plt.figure(figsize=(10,10))
            plt.imshow(image)
            plt.show()

    def channels_hist(self):
        colors = ('blue', 'green', 'red')
        if self.image != "":
            image = cv2.imread(self.image)
            for i, col in enumerate(colors):
                histr = cv2.calcHist([image],[i], None, [256], [0,256])
                intensity_values = np.array([x for x in range(histr.shape[0])])
                plt.plot(intensity_values,histr,color = col,label=col+" channel")
                plt.xlim([0,256])
            plt.legend()
            plt.title("Histogram Channels")
            plt.grid()
            plt.show()

if __name__=="__main__":
    Histogram()
