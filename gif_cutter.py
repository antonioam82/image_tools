from PIL import Image
import os, subprocess
from VALID import ns, OKI

while True:
    nueva_ruta=input("Introduzca ruta: ")
    try:
        os.chdir(nueva_ruta)
        break
    except:
        print("RUTA NO VALIDA")

while True:

    print("")
    print("_____________________________")
    print("|                           |")
    print("|       --GIF CUTTER--      |")
    print("|___________________________|")
    print("")

    giff=input("Nobre del archivo: ")
    gif_name=giff+".gif"

    if not gif_name in os.listdir():
        print("No se encontró el archivo",gif_name)
        break
        
    dato_iz=OKI(input("Introduce dato izquierdo: "))
    dato_sup=OKI(input("Introduce dato superior: "))
    dato_der=OKI(input("Introduce dato derecho: "))
    dato_inf=OKI(input("Introduce dato inferior: "))
    
    box=(dato_iz, dato_sup, dato_der, dato_inf)
    count=0
    
    im = Image.open(gif_name)
    count+=1
    file=giff+str(count)
    n_imagen = im.crop(box)
    n_imagen.save(file+".gif")
    print("")
    print("Extraido frame: ",file+".gif")
    
    im.seek(0)
    try:
        while 1:
            im.seek(im.tell()+1)
            count+=1
            file=giff+str(count)
            n_imagen = im.crop(box)
            n_imagen.save(file+".gif")
            print("Extraido frame: ",file+".gif")
    except EOFError:
        pass
    print("")
    conti=ns(input("¿Desea continuar?: "))
    if conti=="n":
        break
    subprocess.call(["cmd.exe","/C","cls"])
