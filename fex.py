import cv2
import argparse
import os
from tqdm import tqdm
from colorama import Fore, init, Style
from pynput import keyboard

init()

def extract_frames(name,ex):
    cam = cv2.VideoCapture(name+ex)
    num_frames = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"EXTRACTING {num_frames} FRAMES")
    pbar = tqdm(total=num_frames,unit='frames',ncols=100)
    count = 1
    while(True):
        ret,frame = cam.read()
        
        if ret:
            cv2.imwrite(name+str(count)+".png",frame)
            pbar.update(1)
            count+=1
            
        else:
            break
        
    cam.release()
    pbar.close()
    print("\nDONE")
    
def check_source_ext(file):
    supported_formats = ['.mp4','.avi','.mov','.wmv','.rm','.webp']
    name, ex = os.path.splitext(file)
    if file in os.listdir():
        if ex not in supported_formats:
            raise argparse.ArgumentTypeError(Fore.RED+Style.BRIGHT+f"Source file must be '.mp4', '.avi', '.mov', '.wmv', '.rm' or '.webp' ('{ex}' is not valid)."+Fore.RESET+Style.RESET_ALL)
    else:
        raise argparse.ArgumentTypeError(Fore.RED+Style.BRIGHT+f"FILE NOT FOUND: File '{file}' not found."+Fore.RESET+Style.RESET_ALL)
    return file

def main():
    parser = argparse.ArgumentParser(prog="FEX 0.1", conflict_handler = 'resolve',
                                     description = "Extract frames from video.",
                                     epilog = "...")
    parser.add_argument('-src','--source',required=True,type=check_source_ext,help='Source file name')

    args = parser.parse_args()
    name, extension = os.path.splitext(args.source)
    print("VIDEO NAME: ",name)
    print("EXTENSION: ",extension)

    extract_frames(name,extension)

if __name__=='__main__':
    main()
