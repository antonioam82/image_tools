#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox, filedialog
import cv2
import matplotlib.pyplot as plt
import numpy as np

class Histogram:
    def __init__(self):
        self.window = Tk()
        self.window.title("Image Histogramas")
        self.window.geometry("623x575")

        self.window.mainloop()

if __name__=="__main__":
    Histogram()
