from PIL import Image
from tkinter import *
from tkinter import filedialog, messagebox

class compressor():
    def __init__(self):
        self.root = Tk()
        self.root.title("Photo Compressor")
        self.root.geometry("572x309")

        self.entry_name = Entry(self.root,font=('arial',18,'bold'),width=43)
        self.entry_name.place(x=5, y=10)        

        self.root.mainloop()



if __name__=="__main__":
    compressor()
