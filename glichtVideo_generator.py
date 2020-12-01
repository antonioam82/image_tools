import cv2
import numpy as np
import os
import random
from os.path import isfile, join
from VALID import OKI, ns


def convertToVideo(pathIn, pathOut, fps, time):
    print("\nCREATING VIDEO...\n")
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f)) and not 'glichtVid' in f]
    #print(files)
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

def create_frames(d):
    global lista_frames
    os.chdir(d)
    frame_rate = OKI(input("Introduce Frame Rate: "))
    fr_range = int(((OKI(input("Duración en segundos: ")))*frame_rate)/2)
    blu_rang = input("Rango azul: ").split(",")
    gre_rang = input("Rango verde: ").split(",")
    red_rang = input("Rango rojo: ").split(",")

    print("\nWRITTING "+str(fr_range)+" FRAMES...\n")
    for i in range(0,fr_range):
        img = np.zeros((900,1600,3),np.uint8)

        for x in range(900):
            for y in range(1600):
                img[x,y] = [random.randint(int(blu_rang[0]),int(blu_rang[1])),random.randint(int(gre_rang[0]),int(gre_rang[1])),random.randint(int(red_rang[0]),int(red_rang[1]))]#0,256
        name = "ima "+str(i)+".png"
        
        cv2.imwrite(name,img)
        print("DONE: ",name)
        lista_frames.append(name)
    print("TASK COMPLETED")
    return frame_rate

lista_frames=[]
directory = 'C:/Users/Antonio/Documents/videos/imas'
fps = create_frames(directory)

pathIn = directory + '/'
pathOut=pathIn + 'glichtVid2.mp4' 
#fps = #30#15
time = 2
convertToVideo(pathIn, pathOut, fps, time)
elim = ns(input("¿Eliminar frames generados?(n/s): "))
if elim == "s":
    for i in lista_frames:
        os.remove(i)

