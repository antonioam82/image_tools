#!/usr/bin/env python
# -*- coding: utf-8 -*-
from moviepy.editor import *
import sys
import pyglet
from pyglet.window import key
#import subprocess
from VALID import direc, ns

direccion = direc()

def show(g):
    ver = ns(input("¿Ver gif?: "))
    if ver == "s":
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
    print("|      --GIFfromVID--       |")
    print("|___________________________|")
    print("")
    
    vid = busca()
    start = (input("Inicio: ")).split(",")
    end = (input("Final: ")).split(",")
    name = input("Nombre gif: ")

    try:
        clip = (VideoFileClip(vid)
            .subclip((float(start[0]),float(start[1])),
            (float(end[0]),float(end[1]))))
        clip.write_gif(name)
        show(name)
    except:
        print("Hubo un problema al realizar la operación")
    print("")   
    conti = ns(input("¿Desea continuar?: "))
    if conti == "n":
        sys.exit()
    #subprocess.call(["cmd.exe","/C","cls"]) 
