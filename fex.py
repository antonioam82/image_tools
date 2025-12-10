#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import argparse
from PIL import Image
import os
from tqdm import tqdm
from colorama import Fore, init, Style
from pynput import keyboard
#import shutil

init()

stop = False
def on_press(key):
    global stop
    if key == keyboard.Key.space:
        stop = True
        return False

def extract_webp_frames(name, ex, args):
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    
    img = Image.open(name + ex)
    output_dir = args.create_folder if args.create_folder else os.getcwd()
    if args.create_folder:
        os.makedirs(output_dir, exist_ok=True)

    for i in range(img.n_frames):
        img.seek(i)
        
        frame_name = f"frame_{i+1}.png"
        save_path = os.path.join(output_dir, frame_name)

        img.save(save_path)
        print(f"Guardado: {save_path}")

        if stop:
            print(Fore.YELLOW + Style.NORMAL + "\nFrame extraction interrupted by user." + Fore.RESET + Style.RESET_ALL)
            #pbar.disable = True
            break

    if not stop:
        print("DONE")
    listener.stop()

def extract_frames(name,ex,args):
    cam = cv2.VideoCapture(name+ex)
    num_frames = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
    #print(num_frames)
    
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    
    initial_frame = args.from_frame
    if args.to_frame:
        final_frame = args.to_frame
    else:
        final_frame = num_frames
    
    if (initial_frame >= 0 and initial_frame <= num_frames)and (final_frame > 0 and final_frame <= num_frames) and (initial_frame < final_frame):
        cam.set(cv2.CAP_PROP_POS_FRAMES,initial_frame)###########################
        if initial_frame == 0:
            total_frames = abs(num_frames - initial_frame) - abs(final_frame - num_frames)###########################
        else:
            total_frames = abs(num_frames - (initial_frame +1)) - abs(final_frame - num_frames)###########################
        print(f"EXTRACTING {total_frames + 1} FRAMES (press space bar to cancel)")
        pbar = tqdm(total=total_frames,unit='frames',ncols=100)
    
        count = 0
        ret = True
        while ret:
            ret,frame = cam.read()
            count+=1
        
            if ret:
                frame_name = name+"_"+str(count)+"."+args.extension
                
                if args.create_folder: ########################
                    destination =  os.path.join(args.create_folder, frame_name)
                else:
                    destination = frame_name
                    #shutil.move(frame_name, destination) ########################
                cv2.imwrite(destination,frame)
                pbar.update(1)

            if args.to_frame:
                current_frame = int(cam.get(cv2.CAP_PROP_POS_FRAMES))
                pbar.update(1)
                
                if current_frame >= args.to_frame:
                    pbar.disable = True
                    break

            if stop:
                print(Fore.YELLOW + Style.NORMAL + "\nFrame extraction interrupted by user." + Fore.RESET + Style.RESET_ALL)
                pbar.disable = True
                break
                
        cam.release()
        pbar.close()
        listener.stop()
        if not stop:
            print("DONE")
    else:
        print(Fore.RED+Style.BRIGHT+"Invalid index for initial or final frame."+Fore.RESET+Style.RESET_ALL)

def check_outp_ext(ex):
    if ex not in ['png','jpg']:
        raise argparse.ArgumentTypeError(Fore.RED+Style.BRIGHT+f"Output files must be 'png' or 'jpg' ('{ex}' is not valid)."+Fore.RESET+Style.RESET_ALL)
    return ex
    
def check_source_ext(file):
    supported_formats = ['.mp4','.avi','.mov','.wmv','.rm','.webp','.gif']
    name, ex = os.path.splitext(file)
    if os.path.exists(file):
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
    parser.add_argument('-from','--from_frame',default=0,type=int,help='Frame index to extract from')
    parser.add_argument('-to','--to_frame',default=None,type=int,help='Frame index to extract to')
    parser.add_argument('-ex','--extension',default='png',type=check_outp_ext,help='Output extension')
    parser.add_argument('-cf','--create_folder',default="",help='.....')

    args = parser.parse_args()
    name, extension = os.path.splitext(args.source)
    if args.create_folder != "" and not os.path.exists(args.create_folder): #################################################################3333
        os.makedirs(args.create_folder)#################################################################3
    print("VIDEO NAME: ",name+extension)

    if extension != ".webp":
        extract_frames(name,extension,args)
    else:
        extract_webp_frames(name,extension,args)

if __name__=='__main__':
    main()

