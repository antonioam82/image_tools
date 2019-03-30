#!/usr/bin/python
# -*- coding: latin-1 -*-
from __future__ import print_function
from PIL import Image, ImageSequence
import os, subprocess
from VALID import ns, OKI

while True:
    nueva_ruta=input("Introduzca ruta: ")
    if os.path.isdir():
		os.chdir(nueva_ruta)
		break
    else:
        print("RUTA NO VALIDA")
       

while True:

    print("")
    print("_____________________________")
    print("|                           |")
    print("|       --GIF CUTTER--      |")
    print("|___________________________|")
    print("")

    giff=input("Nombre del archivo: ")
    gif_name=giff+".gif"

    if not gif_name in os.listdir():
        print("No se encontró el archivo",gif_name)
        break
    
    im=Image.open(gif_name)
    print("")
    print("Dimensiones: ",im.size[0],"x",im.size[1])
    print("")
    
    corte=ns(input("¿Desea efectuar recortes sobre la imagen?: "))
    
    if corte=="s":
		dato_iz=OKI(input("Introduce dato izquierdo: "))
		dato_sup=OKI(input("Introduce dato superior: "))
		dato_der=OKI(input("Introduce dato derecho: "))
		dato_inf=OKI(input("Introduce dato inferior: "))
		
		box=(dato_iz, dato_sup, dato_der, dato_inf)
    count=1
    
    formato=input("Introduce formato para frames: ")
    t_ar="."+formato
    print("")
    
    for frame in ImageSequence.Iterator(im):
        try:
			if corte=="s":
				n_imagen=im.crop(box)
			else:
				n_imagen=im
			n_imagen.save(giff+str(count)+t_ar)
			print("Extraído frame: ",giff+str(count)+t_ar)
			count += 1
        except:
            print("La operación no pudo completarse con éxito")
            break
    
    print("")
    conti=ns(raw_input("¿Desea continuar?: "))
    if conti=="n":
        break
    subprocess.call(["cmd.exe","/C","cls"])
        
