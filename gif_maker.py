#!/usr/bin/env python
# -*- coding: utf-8 -*-
from moviepy.editor import *
import sys
import pyglet
import os
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
        filename = input("Introduce nombre del video: ")
        if filename in os.listdir():
            return filename
            break
        print("VIDEO NO ENCONTRADO")

while True:
    print("")
    print("_____________________________")
    print("|                           |")
    print("|       --GIF MAKER--       |")
    print("|___________________________|")
    print("")

    opcion = input("Introduzca aqui su opción: ")
    
    if opcion == "A":
        vid = busca()
        start = input("Inicio: ").split(",")
        end = input("Final: ").split(",")
        name = input("Nombre gif: ")
        try:
            clip = (VideoFileClip(vid)
            .subclip((float(start[0]),(float(start[1])),((float(start[0]),(float(start[1])))
            .crop(145,400)))))
            clip.write_gif(name)
            show(name)
        except:
            print("Hubo un problema al realizar la operación")
    else:
        name = input("Nombre gif: ")
        file = input("Palabra clave: ")
        frames=[]
        for i in os.listdir():
            if file in i:
                frames.append(i)
        frames.sort(key=lambda x: int(x.split()[1]))
        clip = ImageSequence(frames,fps=25)
        clip.write_gif(name)
        show(name)
            
    print("")   
    conti = ns(input("¿Desea continuar?: "))
    if conti == "n":
        sys.exit()
    #subprocess.call(["cmd.exe","/C","cls"])
