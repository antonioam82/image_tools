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
    parser.add_argument('--start',default=0.0,type=float,help='inicio')
    parser.add_argument('--end',default=None,type=str,help='final')
    parser.add_argument('--show',help='Mostrar resultado',action='store_true')
    parser.add_argument('-sz',default=100,type=int,help='Tamaño en porcentage')

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
            
    probe = ffmpeg.probe(args.src)
    video_streams = [stream for stream in probe["streams"] if stream["codec_type"] == "video"]
    if args.end:
        duration = float(args.end)
    else:
        duration = video_streams[0]['duration']
    print("GIF DURATION: ",duration)
    clip = (VideoFileClip(args.src)
    .subclip((0,0),(0,float(duration)))
    .resize(args.sz/100))
    print('CREATING GIF...')
    clip.write_gif(args.dest)
    if args.show:
        show(args.dest)

if __name__=='__main__':
    main()
