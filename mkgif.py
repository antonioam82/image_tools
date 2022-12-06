from moviepy.editor import *
import sys
import pyglet
import ffmpeg
import pathlib
from pyglet.window import key
import argparse
import os

def main():

    parser = argparse.ArgumentParser(description="Create gifs from videos.")
    parser.add_argument('-src','--source',required=True,type=str,help='Ruta archivo original')
    parser.add_argument('-dest','--destination',default='my_gif.gif',type=str,help='Ruta archivo destino')
    parser.add_argument('-st','--start',default=0.0,type=float,help='Segundo inicial del gif')
    parser.add_argument('-e','--end',default=None,type=str,help='Segundo final del gif')
    parser.add_argument('-shw','--show',help='Mostrar resultado',action='store_true')
    parser.add_argument('-sz','--size',default=100,type=int,help='Tamaño en porcentage')

    args=parser.parse_args()
    gm(args)

def show(f):
    animation = pyglet.image.load_animation(f)
    bin = pyglet.image.atlas.TextureBin()
    animation.add_to_texture_bin(bin)
    sprite = pyglet.sprite.Sprite(animation)
    w = sprite.width
    h = sprite.height
    window = pyglet.window.Window(width=w, height=h)

    @window.event
    def on_draw():
        sprite.draw()
    pyglet.app.run()

def gm(args):
    file_extension = pathlib.Path(args.source).suffix
    if file_extension == '.mp4':
        if args.source in os.listdir():
            probe = ffmpeg.probe(args.source)
            video_streams = [stream for stream in probe["streams"] if stream["codec_type"] == "video"]
            if args.end:
                duration = float(args.end)
            else:
                duration = video_streams[0]['duration']
            #print("GIF DURATION: ",duration)
            clip = (VideoFileClip(args.source)
            .subclip((0,args.start),(0,float(duration)))
            .resize(args.size/100))
            print('CREATING GIF...')
            clip.write_gif(args.destination)
            if args.show:
                show(args.destination)
        else:
            print("ERROR: File not found.")
    else:
        print("ERROR: The file must have an mp4 extension.")

if __name__=='__main__':
    main()
