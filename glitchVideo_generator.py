import cv2
import numpy as np
import os
import random
from os.path import isfile, join

def OKI(n):
    try:
        n=int(n)
    except:
        n=OKI(input("Caracter no valido: "))
    return n

def ns(c):
    while c!=("s") and c!=("n"):
        print(chr(7));c=input("Escribe solo \'n\' o \'s\' según su opción: ")
    return(c)

def define_name():
    count = 0
    for i in os.listdir():
        if "glitchVid" in i:
            count+=1
    if count>0:
        filename="glitchVid"+str(count)+".mp4"
    else:
        filename="glitchVid.mp4"
    return filename

def convertToVideo(pathIn, pathOut, fps, time):
    if len(lista_frames) > 0:
        print("\nCREATING VIDEO...\n")
        frame_array = []
        files = [f for f in lista_frames if isfile(join(pathIn, f)) and not 'glichtVid' in f]
        files.sort(key=lambda x: int((x.split(".")[0]).split(" ")[1]))#REORDENA FRAMES
        for i in range(len(files)):
            filename = pathIn+files[i]
            print(filename)
            img=cv2.imread(filename)
            height, width, layers = img.shape
            size = (width,height)

            for k in range (time):
                frame_array.append(img)

        out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
        for i in range(len(frame_array)):
            out.write(frame_array[i])
        out.release()
        print("TASK COMPLETED")
    else:
        print("\nNO SE GENERÓ VIDEO")

def create_frames(d):
    global lista_frames
    os.chdir(d)
    frame_rate = OKI(input("Introduce Frame Rate: "))
    fr_range = int(((OKI(input("Duración en segundos: ")))*frame_rate)/2)
    width = validate_size("Ancho imagen: ")
    height = validate_size("Alto imagen: ")
    blu_rang = validate_range("Rango azul: ").split(",")
    gre_rang = validate_range("Rango verde: ").split(",")
    red_rang = validate_range("Rango rojo: ").split(",")
    
    if fr_range > 0:
        print("\nWRITTING "+str(fr_range)+" FRAMES...\n")
        for i in range(0,fr_range):
            img = np.zeros((height,width,3),np.uint8)

            for x in range(height):
                for y in range(width):
                    img[x,y] = [random.randint(int(blu_rang[0]),int(blu_rang[1])),random.randint(int(gre_rang[0]),
                                int(gre_rang[1])),random.randint(int(red_rang[0]),int(red_rang[1]))]#0,256
            name = "ima "+str(i)+".png"
        
            cv2.imwrite(name,img)
            print("DONE: ",name)
            lista_frames.append(name)
        print("TASK COMPLETED")
        return frame_rate
    else:
        print("\n0 FRAMES GENERADOS")

def validate_size(st):
    while True:
        size = OKI(input(st))
        if size > 0:
            break
        else:
            print("El valor introducido debe ser mayor de 0")
    return size
    
def validate_dir():
    while True:
        dire = input("Introduce directorio válido(ej:C:/Users/..): ")
        if os.path.isdir(dire):
            break
    return dire

def validate_range(q):
    while True:
        c = (input(q))
        tup= c.split(",")
        if len(tup) == 2:
            elem1 = tup[0]
            elem2 = tup[1]
            if str(elem1).isdigit() and str(elem2).isdigit() and int(elem1) < int(elem2):
                break
    return c

while True:
    print("")
    print("_____________________________")
    print("|                           |")
    print("|      --GLITCH MAKER--     |")
    print("|___________________________|")
    print("")
    
    lista_frames=[]

    directory = validate_dir()
    fps = create_frames(directory)

    pathIn = directory + '/' 
    fileName=define_name()
    pathOut=pathIn + fileName
    time = 2
    convertToVideo(pathIn, pathOut, fps, time)
    if len(lista_frames) > 0:
        elim = ns(input("¿Eliminar frames generados?(n/s): "))
        if elim == "s":
            for i in lista_frames:
                os.remove(i)

    conti = ns(input("¿Continuar?(n/s): "))
    if conti == "n":
        break
