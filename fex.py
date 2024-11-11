import cv2
import argparse
import os
from tqdm import tqdm
from colorama import Fore, init, Style
from pynput import keyboard

init()

stop = False
def on_press(key):
    global stop
    if key == keyboard.Key.space:
        stop = True
        return False

def extract_frames(name,ex):
    cam = cv2.VideoCapture(name+ex)
    num_frames = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"EXTRACTING {num_frames} FRAMES (press space bar to cancel)")
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    pbar = tqdm(total=num_frames,unit='frames',ncols=100)
    count = 1
    ret = True
    while ret:
        ret,frame = cam.read()
        
        if ret:
            cv2.imwrite(name+str(count)+".png",frame)
            pbar.update(1)
            count+=1

        if stop:
                print(Fore.YELLOW + Style.NORMAL + "\nFrame extraction interrupted by user." + Fore.RESET + Style.RESET_ALL)
                pbar.disable = True
                break
        
    cam.release()
    pbar.close()
    listener.stop()
    if not stop:
        print("DONE")
    
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
    #print("EXTENSION: ",extension)

    extract_frames(name,extension)

if __name__=='__main__':
    main()
