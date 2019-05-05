#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image
import os.path
import subprocess

def OKI(n):
    try:
        n=int(n)
    except:
        n=OKI(input("Caracter no valido: "))
    return n

def ns(c):
    while c!=("s") and c!=("n"):
        print(chr(7));c=input("Escribe solo \'n\' o \'s\' según su opción: ")
    return(c)

while True:
    nueva_ruta=input("Introduzca ruta: ")
    if os.path.isdir(nueva_ruta):
        os.chdir(nueva_ruta)
        break
    else:
        print("RUTA NO VALIDA")
    

def resize(fn):
    file, ext = os.path.splitext(fn)
    try:
        im = Image.open(fn)
        tama = OKI(input("Nuevo tamaño: "))
        w,h = im.size
        if tama < w:
            im.thumbnail((tama,int(tama*h/w)),Image.ANTIALIAS)
            im.save(file+"_resized"+ext,"PNG")
            print("\nACCIÓN COMPLETADA CON ÉXITO")
        else:
            print("\nEl tamaño solicitado es igual o mayor al original",im.size)
    except:
        print("\nNo pudo realizarse la conversión de",fn)


while True:
    print("")
    print("_______________________________")
    print("|                             |")
    print("|   --CREATING THUMBNAILS--   |")
    print("|_____________________________|\n")
    
    imagen=input("Nombre imagen: ")
    if imagen in os.listdir():
        resize(imagen)
    else:
        print("\nNo se encontró el archivo",imagen)
    conti = ns(input("\n¿Desea continuar?: "))
    if conti=="n":
        break
    subprocess.call(["cmd.exe","/C","cls"])

    
