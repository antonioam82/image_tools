from PIL import Image
from tkinter import *
from tkinter import filedialog, messagebox

class compressor():
    def __init__(self):
        self.root = Tk()
        self.root.title("Photo Compressor")
        self.root.geometry("570x300")

        self.root.mainloop()

if __name__=="__main__":
    compressor()
