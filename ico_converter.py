from PIL import Image
import os, subprocess

while True:
    nueva_ruta=input("Introduzca ruta: ")
    if os.path.isdir(nueva_ruta):
        os.chdir(nueva_ruta)
        break
    else:
        print("RUTA NO VALIDA")

def ns(c):
    while c!=("s") and c!=("n"):
        print(chr(7));c=input("Escribe solo \'n\' o \'s\' según su opción: ")
    return(c)
        
while True:

    print("")
    print("_____________________________")
    print("|                           |")
    print("|       --ICO CREATOR--     |")
    print("|___________________________|")
    print("")
    
    im = input("Introduce nombre de archivo: ")
    print("")
    if im in os.listdir():
        name, ext = os.path.splitext(im)
        try:
            imagen=Image.open(im)
            imagen.save(name+".ico")
            print("ARCHIVO '.ICO' CREADO CON EXITO")
        except:
            print("No se pudo completar la operación")
    else:
        print("No se encontró el archivo",im)
    print("")
    conti = ns(input("¿Desea continuar?: "))
    if conti == "n":
         break
    subprocess.call(["cmd.exe","/C","cls"])

