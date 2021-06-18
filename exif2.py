from tkinter import *
from tkinter import filedialog
import pyexiv2

class App:
    def __init__(self):
        self.window = Tk()
        self.window.title("Image Data")
        self.window.configure(bg="gray79")
        self.window.geometry("1200x500")

        self.window.mainloop()

if __name__=="__main__":
    App()
