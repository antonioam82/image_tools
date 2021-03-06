import cv2
import numpy as np
import os
import subprocess
from VALID import ns


while True:
    d = input("Introduce dirección: ")
    if os.path.isdir(d):
        os.chdir(d)
        break
    else:
        print("Dirección no válida: ")

def busca_imagen():
    while True:
        im = input("Introduzca nombre de la imagen: ")
        if im in os.listdir():
            return im
            break
        else:
            print("NO SE ENCONTRÓ LA IMAGEN ", im)
    
while True:

    print("")
    print("_____________________________")
    print("|                           |")
    print("|     --IMAGE COMPARE--     |")
    print("|___________________________|")
    print("")

    while True:
        imagen1 = cv2.imread(busca_imagen())
        imagen2 = cv2.imread(busca_imagen())
    
        tama1 = imagen1.shape
        tama2 = imagen2.shape
        if tama1==tama2:
            break
        else:
            print("LAS DIMENSIONES DE LAS IMAGENES NO COINCIDEN")
    try:
        diferencia = cv2.subtract(imagen1, imagen2)
        resul = not np.any(diferencia)
    except:
        resul = False
        
    if resul is True:
        print("Las imagenes son iguales")
    else:
        if tama1 == tama2:
            cv2.imwrite("resul.jpg",diferencia)
        print("Las imagenes son diferentes")

    conti = ns(input("¿Continuar?: "))
    if conti == "n":
        break
    subprocess.call(["cmd.exe","/C","cls"])
