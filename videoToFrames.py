#LIBRARIES YOU NEED.
from VALID import ns
import cv2
import os

def ny():
    while True:
        q = input('Continue?(ny): ')
        if q == 'n' or q == 'y':
            return q
            break
        else:
            print("Type y or n")


os.chdir(r'C:\Users\Antonio\Documents\Nueva carpeta')

while True:
    print("")
    print("_____________________________")
    print("|                           |")
    print("|   --FRAMES FROM VIDEO--   |")
    print("|___________________________|")
    print("")
    
    root = input("Enter path to video: ")
    if os.path.exists(root):
        file = root.split("/")[-1]
        file_name,ex = os.path.splitext(file)
        cam = cv2.VideoCapture(root)
        #CREATE FRAME COUNTER.
        currentframe = 0

        while(True):
            #READ FROM FRAMES
            ret,frame = cam.read()

            if ret:
                #IF VIDEO IS STILL LETF, CONTINUE CREATING FRAMES.
                name = file_name+str(currentframe)+'.jpg'
                print('Creating...'+name)
        
                #WRITE THE EXTRACTED FRAME.
                cv2.imwrite(name,frame)
        
                #INCREASE FRAME COUNTER.
                currentframe += 1
            else:
                break
        
        cam.release()
        cv2.destroyAllWindows()

    else:
        print('Wrong path')

    conti = ny()
    if conti == "n":
        break
