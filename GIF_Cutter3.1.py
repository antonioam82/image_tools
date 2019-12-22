import Pmw
from random import *
from tkinter import *
from PIL import Image, ImageTk, ImageSequence
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import Label
import threading
import os

ventana = Pmw.initialise(fontScheme = 'pmw1')
ventana.title("GIF CUTTER")
ventana.configure(bg="LightBlue3")
_start = (0,0)
_end=""
size=""
archivo_selec = ""
_funcids = {}
im = ""
canvas = ""

def _on_drag(event):
    global _start
    global _end
    global canvas

    x0, y0 = _start
    ex, ey = canvas.canvasx(event.x), canvas.canvasy(event.y)
    _end = (ex, ey)
    _draw_rectangle()

def _draw_rectangle():
    global canvas
    global _end
    global _start

    canvas.delete("rectangle")

    if _end is None or _start is None:    
        return None

    x0, y0 = _start
    x1, y1 = _end

    canvas.create_rectangle(x0, y0, x1, y1, fill="#18c194",
                            width=1, stipple="gray50", tags='rectangle'
                            )
    
def _on_click(event):
    global _start
    global _end
    global canvas
    
    _start = (canvas.canvasx(event.x), canvas.canvasy(event.y))
    _end = None

def clear():
    global archivo_selec, im
    display.clear()
    texto_inicio()
    archivo_selec=""
    im=""

def recorte():
    global _start, _end, canvas
    #name,ex = os.path.splitext(archivo)
    #ventana.title("SELECCIONAR AREA DE RECORTE")
    if archivo_selec!="":
        top = Toplevel()
        canvas = Canvas(top,width=_end[0],height=_end[1],background='black')
        canvas.pack(padx=0,pady=0)
        archi = ImageTk.PhotoImage(Image.open(archivo_selec))
        canvas.create_image(0,0,image=archi,anchor=NW)
        canvas.bind('<Button-1>',_on_click)
        canvas.bind("<B1-Motion>", _on_drag)
        #crop_btn = Button(top, text="Recortar imagen", state="normal", bg="light green",command=verify).pack(side="bottom",expand=1, fill=X)
        top.mainloop()
    else:
        display.appendtext("PULSE \'BUSCAR\' PARA SELECCIONAR UN ARCHIVO\n")

def direc():
    directorio=filedialog.askdirectory()
    if directorio!="":
        os.chdir(directorio)
        display.appendtext(f"Dir: {os.getcwd()}"+"\n")

def iniciar_extract():
    if archivo_selec!="" and im!="":
        t=threading.Thread(target=corta)
        t.start()
    else:
        display.appendtext("PULSE \'BUSCAR\' PARA SELECCIONAR UN ARCHIVO\n")

def corta():
    count=1
    archivo=(((archivo_selec).split("/"))[-1])
    try:
        name,ex = os.path.splitext(archivo)
        for frame in ImageSequence.Iterator(im):
            nom_imagen=name+" "+str(count)+'.png'
            c_im=im.crop(_start+_end)
            c_im.save(nom_imagen)
            display.appendtext("\nExtraido frame: "+nom_imagen)
            count+=1
        display.appendtext("\n\nPROCESO FINALIZADO\n")
    except:
        display.appendtext("\nHUBO UN PROBLEMA AL REALIZAR LA OPERACIÓN")
        
def busca():
    global archivo_selec
    global im, size, archivo
    global _end
    archivo_selec = askopenfilename(parent=ventana, initialdir="M:/",title='Choose an image.')
    archivo=(((archivo_selec).split("/"))[-1])
    if archivo_selec!="":
        try:
            im=Image.open(archivo_selec)
            size=(im.size)
            _end=size
            display.appendtext("Archivo seleccionado: "+(((archivo_selec).split("/"))[-1])+"\n")
        except:
            archivo_selec = ""
            display.appendtext("NO SE PUDO ABRIR EL ARCHIVO\n")
    
def texto_inicio():
    display.appendtext("_____________________________\n")
    display.appendtext("|                           |\n")
    display.appendtext("|       --GIF CUTTER--      |\n")
    display.appendtext("|___________________________|\n")
    display.appendtext("\n")
    display.appendtext("Pulse \'BUSCAR\' para escoger archivo.\nPulse \'CARPETA\' para escoger carpeta de destino.\n\n")

display = Pmw.ScrolledText(ventana, hscrollmode='none',
                      vscrollmode='dynamic', hull_relief='sunken',
                      hull_background='gray20', hull_borderwidth=10,
                      text_background='green4', text_width=65,
                      text_foreground='PaleGreen2', text_height=22,
                      text_padx=10, text_pady=10, text_relief='groove',
                      text_font=('Fixedsys', 10))
display.pack(padx=0,pady=0)

buttons = Pmw.ButtonBox(ventana,hull_background="LightBlue3")

buttons.pack(fill='both', expand=1, padx=1, pady=1)

buttons.add('LIMPIAR',bg='khaki',command=clear,width=12)
buttons.add('CARPETA',bg='khaki',command=direc)
buttons.add('EXTRAER',bg='khaki',command=iniciar_extract)
buttons.add('BUSCAR',bg='khaki',command=busca)
buttons.add('RECORTAR',bg='khaki',command=recorte)

buttons.alignbuttons()

texto_inicio()

ventana.mainloop()




