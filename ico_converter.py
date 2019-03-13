from PIL import Image
from VALID import ns
import os

while True:
    nueva_ruta=input("Introduzca ruta: ")
    if os.path.isdir(nueva_ruta):
        os.chdir(nueva_ruta)
        break
    else:
        print("RUTA NO VALIDA")
        
while True:
    im = input("Introduce nombre de archivo: ")
    if im in os.listdir():
        diiv = im.split(".")
        name = diiv[0]
        try:
            imagen=Image.open(im)
            imagen.save(name+".ico")
            print("CONVERSIÓN REALIZADA CON EXITO")
        except:
            print("No se pudo completar la operación")
    else:
        print("No se encontró el archivo",im)
    conti = ns(input("¿Desea continuar?: "))
    if conti == "n":
         break

