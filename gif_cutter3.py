import Pmw
#from tkinter.filedialog import askopenfilename
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import Label
import threading
import os

ventana = Pmw.initialise(fontScheme = 'pmw1')
ventana.title("GIF CUTTER")
_start = (0,0)
_end=""
size=""
archivo_selec = ""
im = ""
canvas = ""

def clear():
    global archivo_selec, im
    display.clear()
    texto_inicio()
    archivo_selec=""
    im=""

def recorte():
    global _start, _end, canvas
    name,ex = os.path.splitext(archivo)
    if ex!=".webp":
        raiz = tk.Tk()
        raiz.title("SELECCIONE AREA CON EL RATÓN")
        mi_Frame = tk.Frame(master=raiz)
        mi_Frame.pack()
        mi_Frame.config(width=size[0], height=size[1])
        canvas = tk.Canvas(mi_Frame, bd=0)
        ima=tk.PhotoImage(master = canvas, file = archivo_selec)
        fondo=Label(mi_Frame,image=ima).place(x=0,y=0)
        crop_btn = tk.Button(raiz, text="Recortar imagen", state="disabled", bg="light green").pack(side="bottom",expand=1, fill=tk.X)
    
    ventana.mainloop()

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
        display.appendtext("\nSELECCIONE UN ARCHIVO\n")

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
            print(im)
            print(size[0])
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
                      text_background='honeydew4', text_width=65,
                      text_foreground='black', text_height=22,
          text_padx=10, text_pady=10, text_relief='groove',
                      text_font=('Fixedsys', 10))
display.pack(padx=0,pady=0)

buttons = Pmw.ButtonBox(ventana)

buttons.pack(fill='both', expand=1, padx=1, pady=1)

buttons.add('LIMPIAR',bg='light blue',command=clear,width=12)
buttons.add('CARPETA',bg='light blue',command=direc)
buttons.add('EXTRAER',bg='light blue',command=iniciar_extract)
buttons.add('BUSCAR',bg='light blue',command=busca)
buttons.add('RECORTAR',bg='light blue',command=recorte)
buttons.alignbuttons()

texto_inicio()

ventana.mainloop()


