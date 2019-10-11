from moviepy.editor import *
import os
from VALID import direc

direccion = direc()

vid = input("Introducir video")
mi1 = input("Corte: ")
sec1 = input("Corte: ")
mi2 = input("Corte: ")
sec2 = input("Corte: ")

clip = (VideoFileClip(vid)
        .subclip((float(mi1),float(sec1)),(float(mi2),float(sec2))))

clip.write_gif("new_gif.gif")
