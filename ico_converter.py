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
        
f_count=0
while True:
    im = input("Introduce nombre de archivo: ")
    for i in os.listdir():
        if i.startswith(im):
            f_count+=1
            try:
                imagen=Image.open(i)
                imagen.save(im+".ico")
                print("CONVERSIÓN REALIZADA CON EXITO")
            except:
                print("No se pudo completar la operación")
    if f_count == 0:
        print("No se encontró el archivo",im)
    conti = ns(input("¿Desea continuar?: "))
    if conti == "n":
         break
