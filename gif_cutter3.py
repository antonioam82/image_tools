import Pmw
#from tkinter.filedialog import askopenfilename
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
from tkinter import filedialog,Label
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
_funcids = {}
#canvas=""

def _on_drop(event):
    global _start
    global _end
    global _img
    global crop_btn

    if _end is None:
        crop_btn.config(state="disabled")

    else:

        # Acotar límites de seleción a la imagen
        img_x, img_y = _img.size

        x0, y0 = _start
        x0 = img_x if x0 > img_x else 0 if x0 < 0 else x0
        y0 = img_y if y0 > img_y else 0 if y0 < 0 else y0 
        _start = (x0, y0)

        x1, y1 = _end
        x1 = img_x if x1 > img_x else 0 if x1 < 0 else x1
        y1 = img_y if y1 > img_y else 0 if y1 < 0 else y1       
        _end = (x1, y1)

        # Normalizado para obtener vertice superior izquierdo e inferior derecho
        if x0 > x1:
            if y0 < y1: # _start es el vértice superior derecho
                _start = (x1, y0)
                _end = (x0, y1)
            else:       # _start es el vértice inferior derecho
                _start, _end = _end, _start
        else:
            if y0 > y1:  # _start es el vértice inferior izquierdo
                _start = (x0, y1)
                _end = (x1, y0)

        crop_btn.config(state="normal")

    # Redibujar rectágulo
    _draw_rectangle()

def _on_drag(event):
    global _start
    global _end
    global canvas

    x0, y0 = _start
    ex, ey = canvas.canvasx(event.x), canvas.canvasy(event.y)
    _end = (ex, ey)
    _draw_rectangle()



def _on_click(event):
    global _start
    global _end
    global canvas
    _start = (canvas.canvasx(event.x), canvas.canvasy(event.y))
    _end = None

def _enable_croping():
    global canvas
    _funcids["<Button-1>"] = canvas.bind("<Button-1>", _on_click, '+')
    _funcids["<B1-Motion>"] = canvas.bind("<B1-Motion>", _on_drag, '+')
    _funcids["<ButtonRelease-1>"] = canvas.bind("<ButtonRelease-1>", _on_drop, '+')
    print("enabled")
    

def clear():
    global archivo_selec, im
    display.clear()
    texto_inicio()
    archivo_selec=""
    im=""

def recorte():
    global _start, _end, canvas
    raiz = tk.Tk()
    mi_Frame = tk.Frame(master=raiz)
    mi_Frame.pack()
    mi_Frame.config(width=size[0], height=size[1])
    canvas = tk.Canvas(mi_Frame, bd=0)
    ima=tk.PhotoImage(master = canvas, file = archivo_selec)
    fondo=Label(mi_Frame,image=ima).place(x=0,y=0)

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
    archivo_selec=filedialog.askopenfilename(initialdir = "/",
    title = "Seleccione archivo",filetypes = (("gif","*.*"),
    ("webp","*.*")))
    archivo=(((archivo_selec).split("/"))[-1])
    if archivo_selec!="":
        try:
            im=Image.open(archivo_selec)
            size=(im.size)
            print(im)
            print(size[0])
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



