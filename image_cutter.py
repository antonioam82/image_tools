#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image
from VALID import ns, OKI
import subprocess, os

def veri(n):
    ciert=False
    if n!=(""):
        for i in os.listdir():
            if i.startswith(n):
                ciert=True
                break
        if ciert==False:
            print("No se encontro ningún archivo con tales iniciales.")
    return ciert

while True:
    nueva_ruta=input("Introduzca ruta: ")
    try:
        os.chdir(nueva_ruta)
        break
    except:
        print("RUTA NO VALIDA")

#os.chdir(r'C:\Users\Antonio\Documents\Nueva carpeta\imagess')

while True:
    
    print("")
    print("_____________________________")
    print("|                           |")
    print("|     --IMAGE  CUTTER--     |")
    print("|___________________________|")
    print("")

    saving=ns(input("¿Desea conservar los archivos originales?: "))

    pasa=False
    while pasa==False:
        inicial=input("Introduce inicial: ")
        pasa=veri(inicial)
        
    dato_iz=OKI(input("Introduce dato izquierdo: "))
    dato_sup=OKI(input("Introduce dato superior: "))
    dato_der=OKI(input("Introduce dato derecho: "))
    dato_inf=OKI(input("Introduce dato inferior: "))
    
    box=(dato_iz, dato_sup, dato_der, dato_inf)
    
    print("")
    for file in os.listdir():
        if file.startswith(inicial) and not file.endswith('.gif'):
            try:
                imagen = Image.open(file)
                ig=imagen
                n_imagen = imagen.crop(box)
                if saving=="s":
                    nom, ext = os.path.splitext(file)
                    file = nom+"(copia)"+ext
                n_imagen.save(file)
                print("Operación completada con éxito para el archivo", file) 

            except:
                print("La operación no pudo completarse con éxito para el archivo", file)
                ig.save(file)
                ig.close()
                break
    print("")

    conti=ns(input("¿Continuar?: "))

    if conti=="n":
        break
    subprocess.call(["cmd.exe","/C","cls"])
