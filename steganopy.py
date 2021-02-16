from tkinter import *
import cv2
import numpy as np

class app():
    def __init__(self):
        self.window = Tk()
        self.window.title("Image Steganography")
        self.window.geometry("590x500")

        self.window.mainloop()

if __name__=="__main__":
    app()
