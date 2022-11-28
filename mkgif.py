from moviepy.editor import *
import sys
import pyglet
import ffmpeg
from pyglet.window import key
import argparse
import os

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-src',type=str,help='Archivo original')
    parser.add_argument('-dest',type=str,help='Archivo destino')
    parser.add_argument('--show',default=False,type=bool,help='Mostrar resultado')
    parser.add_argument('-sz',default=100,type=int,help='Tamaño en %')

    args=parser.parse_args()
    gm(args)

def gm(args):
    probe = ffmpeg.probe(args.src)
    video_streams = [stream for stream in probe["streams"] if stream["codec_type"] == "video"]
    print("DURATION: ",video_streams[0]['duration'])

if __name__=='__main__':
    main()
