#!/usr/bin/env python
# -*- coding: utf-8 -*-
from moviepy.editor import *
import sys
import pyglet
import os
from pyglet.window import key
from VALID import direc, ns, OKI, OK

direccion = direc()

def ab(r):
    while r!='A' and r!='B':
        r = input("Introduzca \'A\' o \'B\' según su opción: ")
    return r

def size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            print (f"{bytes:.2f}{unit}{suffix}")
        bytes /= factor
        
def new_size(d):
    if d == "s":
        ns = OK(input("Nuevo tamaño: "))
    else:
        ns = 1.0
    return ns

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

def add_ext(n):
    if not ".gif" in n:
        n = n+".gif"
    return n

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
    print("         ESCOJA OPCIÓN        ")
    print("A) CREAR GIF A PARTIR DE VIDEO")
    print("B) CREAR A PARTIR DE SECUENCIA\n")
    opcion = ab(input("Introduzca aqui su opción (A o B): ").upper())
    
    if opcion == "A":
        vid = busca()
        start = input("Inicio (min,sec): ").split(",")
        end = input("Final (min,sec): ").split(",")
        name = add_ext(input("Nombre del nuevo gif: "))
        change = ns(input("¿Cambiar tamaño?: "))
        try:
            clip = (VideoFileClip(vid)
            .subclip((float(start[0]),float(start[1])),
                     (float(end[0]),float(end[1])))
            .resize(new_size(change)))
            clip.write_gif(name)
            print("\nTAMAÑO")
            siz = size(os.stat(name).st_size)
            print("\n")
            show(name)
        except:
            print("Hubo un problema al realizar la operación")
    else:
        name = input("Nombre del nuevo gif: ")
        file = (input("Palabra clave: ")+" ")
        speed = OKI(input("Velocidad: "))
        frames=[]
        try:
            for i in os.listdir():
                if file in i:
                    frames.append(i[:-4])
            frames.sort(key=lambda x: int(x.split()[1]))
            #try:
                #frames_new = list(map(lambda x: x+".png",frames))
            #except:
                #print("busqueda se .jpg")
            frames_new = list(map(lambda x: x+".jpg",frames))
            clip = ImageSequenceClip(frames_new,fps=speed)
            clip.write_gif(name)
            print("\nTAMAÑO")
            siz = size((os.stat(name)[6]))
            print("\n")
            show(name)
        except Exception as e:
            print(str(e))
            
    print("")   
    conti = ns(input("¿Desea continuar?: "))
    if conti == "n":
        sys.exit()

