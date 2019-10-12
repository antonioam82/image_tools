from moviepy.editor import *
import os
from VALID import direc

direccion = direc()

vid = input("Introducir video:" )
start = input("Inicio: ")
end = input("Final: ")
inicio = (start).split(",")
ended = (end).split(",")
name = input("Nombre gif: ")


clip = (VideoFileClip(vid)
        .subclip((float(inicio[0]),float(inicio[1])),(float(ended[0]),float(ended[1]))))

clip.write_gif(name)
