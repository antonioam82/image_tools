#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from PIL import Image, ImageSequence
import os, subprocess
import shutil
from VALID import ns, OKI

while True:
    nueva_ruta=input("Introduzca ruta: ")
    if os.path.isdir(nueva_ruta):
        os.chdir(nueva_ruta)
        break
    else:
        print("RUTA NO VALIDA")

def busca():
    archiv=input("Nombre del archivo: ")
    if not ".gif" in archiv:
        archiv=archiv+".gif"
    return archiv

def carpeta_nueva(m,n):
    if not os.path.exists(n):
        os.makedirs(n)
    shutil.move(m,n)

#formatos = ["P", "L", "RGB", "RGBA", "LA"]

while True:

    carpeta_destino="frames"

    print("")
    print("_____________________________")
    print("|                           |")
    print("|       --GIF CUTTER--      |")
    print("|___________________________|")
    print("")

    #giff=input("Nombre del archivo: ")
    gif_name=busca()

    while not gif_name in os.listdir():
        print("NO SE ENCONTRÓ EL ARCHIVO",gif_name)
        gif_name=busca()
        
    name,ext=os.path.splitext(gif_name)
        
    try:
        im=Image.open(gif_name)
        print("\nDimensiones: ",im.size[0],"x",im.size[1])
        print("")
    except:
        print("\nNo se pudo abrir el archivo",gif_name)
        break

    #while True:
        #form=input("Fromato: ")
        #if form in formatos:
            #continue
        #else:
            #break

    corte=ns(input("¿Desea realizar cortes sobre los frames?: "))

    if corte=="s":
        carpeta_destino="cropped"
        dato_iz=OKI(input("Introduce dato izquierdo: "))
        dato_sup=OKI(input("Introduce dato superior: "))
        dato_der=OKI(input("Introduce dato derecho: "))
        dato_inf=OKI(input("Introduce dato inferior: "))
    
        box=(dato_iz, dato_sup, dato_der, dato_inf)
    count=1
    
    for frame in ImageSequence.Iterator(im):
        try:
            if corte=="s":
                n_imagen=im.crop(box)
            else:
                n_imagen=im#convert(form)
            nom_imagen=name+str(count)+'.png'
            n_imagen.save(nom_imagen)
            print("Extraído frame: ",nom_imagen)
            carpeta_nueva(nom_imagen,carpeta_destino)
            count += 1
        except:
            print("La operación no pudo completarse con éxito")
            os.remove(name+str(count)+'.png')
            break
    print("\nLos archivos han sido guardados en la carpeta", carpeta_destino)
        
    
    print("")
    conti=ns(input("¿Desea continuar?: "))
    if conti=="n":
        break
    subprocess.call(["cmd.exe","/C","cls"])
