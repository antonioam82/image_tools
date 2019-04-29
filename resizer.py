from PIL import Image
import os.path
from VALID import ns, OKI
import subprocess

while True:
    nueva_ruta=input("Introduzca ruta: ")
    if os.path.isdir(nueva_ruta):
        os.chdir(nueva_ruta)
        break
    else:
        print("RUTA NO VALIDA")
    

def resuze(fn,tama):
    file, ext = os.path.splitext(fn)
    im = Image.open(fn)
    w,h=im.size
    im.thumbnail((tama,int(tama*h/w)),Image.ANTIALIAS)
    im.save(file+"_resized"+ext,"PNG")
    #im.thumbnail((40,int(40.*h/w)),Image.ANTIALIAS)#150
    #im.save(file+"_thumbnail"+ext,'PNG')

while True:
    print("\n______________________________")
    print("|                             |")
    print("|      --IMAGE RESIZER--      |")
    print("|_____________________________|\n")
    
    imagen=input("Nombre imagen: ")
    
    tama=OKI(input("Nuevo tamaño: "))
    resuze(imagen,tama)
    conti=ns(input("\n¿Desea continuar?: "))
    if conti=="n":
        break
    subprocess.call(["cmd.exe","/C","cls"])
