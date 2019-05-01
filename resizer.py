from PIL import Image
import os.path
#from VALID import ns, OKI
import subprocess

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
 
def OKI(n):
    try:
        n=int(n)
    except:
        n=OKI(input("Caracter no valido: "))
    return n
    
def resuze(fn,tama):
    file, ext = os.path.splitext(fn)
    im = Image.open(fn)
    w,h=im.size
    im.thumbnail((tama,int(tama*h/w)),Image.ANTIALIAS)
    im.save(file+"_resized"+ext,"PNG")

while True:
    print("")
    print("_______________________________")
    print("|                             |")
    print("|      --IMAGE RESIZER--      |")
    print("|_____________________________|\n")
    
    imagen=input("Nombre imagen: ")
    if imagen in os.listdir():
        tama=OKI(input("Nuevo tamaño: "))
        resuze(imagen,tama)
        print("\nACCIÓN COMPLETADA CON ÉXITO")
    else:
        print("\nNo se encontró el archivo",imagen)
    conti=ns(input("\n¿Desea continuar?: "))
    if conti=="n":
        break
    subprocess.call(["cmd.exe","/C","cls"])
    
