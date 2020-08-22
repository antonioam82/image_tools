#LIBRARIES YOU NEED.
from VALID import ns
import cv2
import os

os.chdir(r'C:\Users\Antonio\Documents\Nueva carpeta')

while True:
    print("")
    print("_____________________________")
    print("|                           |")
    print("|   --FRAMES FROM VIDEO--   |")
    print("|___________________________|")
    print("")
    
    root = input("Enter path to video: ")

    cam = cv2.VideoCapture(root)

    #CREATE FRAME COUNTER.
    currentframe = 0

    while(True):
        #READ FROM FRAMES
        ret,frame = cam.read()

        if ret:
            #IF VIDEO IS STILL LETF, CONTINUE CREATING FRAMES.
            name = 'frame'+str(currentframe)+'.jpg'
            print('Creating...'+name)
        
            #WRITE THE EXTRACTED FRAME.
            cv2.imwrite(name,frame)
        
            #INCREASE FRAME COUNTER.
            currentframe += 1
        else:
            break
        
    cam.release()
    cv2.destroyAllWindows()

    conti = ns(input("¿Continuar?(n/s): "))
    if conti == "n":
        break
