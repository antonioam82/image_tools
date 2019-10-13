from moviepy.editor import *
import os
import pyglet
import subprocess
from VALID import direc, ns

direccion = direc()

def show(g):
    animation = pyglet.image.load_animation(g)
    bin = pyglet.image.atlas.TextureBin()
    animation.add_to_texture_bin(bin)
    sprite = pyglet.sprite.Sprite(animation)

    w = sprite.width
    h = sprite.height

    window = pyglet.window.Window(width=w, height=h)

    @window.event
    def on_draw():
        sprite.draw()
    pyglet.app.run()

def busca():
    while True:
        filename = input("Introduce nombre del video fuente: ")
        if filename in os.listdir():
            return filename
            break
        print("VIDEO NO ENCONTRADO")

while True:
    print("")
    print("_____________________________")
    print("|                           |")
    print("|       --GIFfromVID--      |")
    print("|___________________________|")
    print("")
    
    vid = busca()
    start = input("Inicio: ")
    end = input("Final: ")
    inicio = (start).split(",")
    ended = (end).split(",")
    name = input("Nombre gif: ")

    try:
        clip = (VideoFileClip(vid)
            .subclip((float(inicio[0]),float(inicio[1])),
            (float(ended[0]),float(ended[1]))))
        clip.write_gif(name)
        show(name)
    except:
        print("Hubo un problema al realizar la operación")
        
    print("")   
    conti = ns(input("¿Desea continuar?: "))
    if conti == "n":
        break
    subprocess.call(["cmd.exe","/C","cls"])
