from PIL import Image
import os, subprocess

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

while True:

    print("")
    print("_____________________________")
    print("|                           |")
    print("|      --ICO CREATOR--      |")
    print("|___________________________|")
    print("")
    
    im = input("Introduce nombre de archivo: ")
    if im in os.listdir():
        diiv = im.split(".")
        name = diiv[0]
        try:
            imagen=Image.open(im)
            imagen.save(name+".ico")
            print("ARCHIVO '.ICO' CREADO CON EXITO")
        except:
            print("No se pudo completar la operación")
    else:
        print("No se encontró el archivo",im)
    conti = ns(input("¿Desea continuar?: "))
    if conti == "n":
         break
    subprocess.call(["cmd.exe","/C","cls"])


