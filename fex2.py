#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import argparse
from PIL import Image
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

def extract_animated_img_frames(name, ex, args):
    try:
        img = Image.open(name + ex)
        total_frames = getattr(img, 'n_frames', 1)
        
        print(f"EXTRACTING {total_frames} FRAMES FROM ANIMATED IMAGE")
        pbar = tqdm(total=total_frames, unit='frames', ncols=100)

        for i in range(total_frames):
            if stop:
                print(Fore.YELLOW + "\nExtraction interrupted by user." + Fore.RESET)
                break
            
            img.seek(i)
            # Convertir a RGB para asegurar compatibilidad con JPG/PNG
            frame_rgb = img.convert("RGB")
            
            frame_name = f"{name}_{i+1:03d}.{args.extension}"
            
            if args.create_folder:
                destination = os.path.join(args.create_folder, frame_name)
            else:
                destination = frame_name
            
            frame_rgb.save(destination)
            pbar.update(1)
            
        pbar.close()
        if not stop:
            print("DONE")
            
    except Exception as e:
        print(Fore.RED + f"Error procesando imagen animada: {e}" + Fore.RESET)

def extract_frames(name, ex, args):
    cam = cv2.VideoCapture(name + ex)
    num_frames = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
    
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    initial_frame = args.from_frame
    final_frame = args.to_frame if args.to_frame else num_frames
    
    if (0 <= initial_frame < num_frames) and (0 < final_frame <= num_frames) and (initial_frame < final_frame):
        cam.set(cv2.CAP_PROP_POS_FRAMES, initial_frame)
        total_to_extract = final_frame - initial_frame
        
        print(f"EXTRACTING {total_to_extract} FRAMES (press space bar to cancel)")
        pbar = tqdm(total=total_to_extract, unit='frames', ncols=100)
    
        count = initial_frame
        while count < final_frame:
            ret, frame = cam.read()
            if not ret or stop:
                if stop:
                    print(Fore.YELLOW + "\nFrame extraction interrupted by user." + Fore.RESET)
                break
            
            count += 1
            frame_name = f"{name}_{count:03d}.{args.extension}"
            
            if args.create_folder:
                destination = os.path.join(args.create_folder, frame_name)
            else:
                destination = frame_name
                
            cv2.imwrite(destination, frame)
            pbar.update(1)

        cam.release()
        pbar.close()
        listener.stop()
        if not stop:
            print("DONE")
    else:
        print(Fore.RED + Style.BRIGHT + "Invalid index for initial or final frame." + Fore.RESET + Style.RESET_ALL)

def check_outp_ext(ex):
    if ex not in ['png', 'jpg']:
        raise argparse.ArgumentTypeError(f"Output files must be 'png' or 'jpg' ('{ex}' is not valid).")
    return ex
    
def check_source_ext(file):
    supported_formats = ['.mp4', '.avi', '.mov', '.wmv', '.rm', '.webp', '.gif']
    _, ex = os.path.splitext(file.lower())
    if os.path.exists(file):
        if ex not in supported_formats:
            raise argparse.ArgumentTypeError(f"Unsupported format: {ex}")
    else:
        raise argparse.ArgumentTypeError(f"FILE NOT FOUND: {file}")
    return file

def main():
    parser = argparse.ArgumentParser(prog="FEX 0.2", description="Extract frames from video or animated images.")
    parser.add_argument('-src', '--source', required=True, type=check_source_ext, help='Source file name')
    parser.add_argument('-from', '--from_frame', default=0, type=int, help='Frame index to extract from')
    parser.add_argument('-to', '--to_frame', default=None, type=int, help='Frame index to extract to')
    parser.add_argument('-ex', '--extension', default='png', type=check_outp_ext, help='Output extension (png/jpg)')
    parser.add_argument('-cf', '--create_folder', default="", help='Destination folder')

    args = parser.parse_args()
    name, extension = os.path.splitext(args.source)
    extension = extension.lower()

    if args.create_folder and not os.path.exists(args.create_folder):
        os.makedirs(args.create_folder)

    print("SOURCE FILE: ", name + extension)

    if extension in [".webp", ".gif"]:
        extract_animated_img_frames(name, extension, args)
    else:
        extract_frames(name, extension, args)

if __name__ == '__main__':
    main()
