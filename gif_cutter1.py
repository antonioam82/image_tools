from __future__ import print_function
from PIL import Image, ImageSequence
import os, subprocess
from VALID import ns, OKI

#while True:
    #nueva_ruta=input("Introduzca ruta: ")
    #if os.path.isdir(nueva_ruta):
        #os.chdir(nueva_ruta)
        #break
    #else:
        #print("RUTA NO VALIDA")

os.chdir(r'C:\Users\Antonio\Documents\Nueva carpeta\imagess')

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
        
    dato_iz=OKI(input("Introduce dato izquierdo: "))
    dato_sup=OKI(input("Introduce dato superior: "))
    dato_der=OKI(input("Introduce dato derecho: "))
    dato_inf=OKI(input("Introduce dato inferior: "))
    
    box=(dato_iz, dato_sup, dato_der, dato_inf)
    count=0
    
    #im = Image.open(gif_name)

    for frame in ImageSequence.Iterator(im):
        try:
            n_imagen=im.crop(box)
            n_imagen.save(giff+str(count)+".png")
            print("Extraído frame: ",giff+str(count)+".png")
            count += 1
        except EOFError:
            print("La operación no pudo completarse con éxito")
            pass
    
    print("")
    conti=ns(input("¿Desea continuar?: "))
    if conti=="n":
        break
    subprocess.call(["cmd.exe","/C","cls"])
