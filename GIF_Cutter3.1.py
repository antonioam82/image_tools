import Pmw
from tkinter import *
from PIL import Image, ImageTk, ImageSequence
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, askdirectory
import threading
import os

ventana = Pmw.initialise(fontScheme = 'pmw1')
ventana.title("GIF CUTTER")
ventana.configure(bg="LightBlue3")
_start = (0,0)
_end=""
size=""
archivo_selec = ""
im = ""
ver = False
canvas = ""


def verify():
    global ver
    ver = True
    top.destroy()
    display.appendtext("EFECTUADO RECORTE\n")

def delete_rectangle(event):
    canvas.delete("rectangle")
    crop_btn.config(state="disabled")

def _on_click(event):
    global _start
    global _end
    global canvas
    
    _start = (canvas.canvasx(event.x), canvas.canvasy(event.y))
    _end = None
    crop_btn.config(state="normal")

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
    
def _on_drag(event):
    global _start
    global _end
    global canvas

    x0, y0 = _start
    ex, ey = canvas.canvasx(event.x), canvas.canvasy(event.y)
    _end = (ex, ey)
    _draw_rectangle()

def clear():
    global archivo_selec, im, ver
    display.delete('1.0',END)
    texto_inicio()
    archivo_selec=""
    im=""
    ver = False

def recorte():
    global canvas
    root = Tk()
    canv = Canvas(root, width=500, height=375, bg='white')
    canv.grid(row=0, column=0)
    img = ImageTk.PhotoImage(archivo_selec)
    canv.create_image(0, 0, anchor=NW, image=img)
    canv.pack(side="left")
    
    root.mainloop()

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

def _on_drop(event):
    global _start
    global _end
    global im

    if not _end is None:
        
        # Acotar límites de seleción a la imagen
        img_x, img_y = im.size

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

        # Redibujar rectágulo
        _draw_rectangle()

def recorte():
    global canvas, crop_btn, top
    if archivo_selec!="":
        top = Toplevel()
        canvas = Canvas(top,width=size[0],height=size[1],background='black')
        canvas.pack(padx=0,pady=0)
        archi = ImageTk.PhotoImage(Image.open(archivo_selec))
        canvas.create_image(0,0,image=archi,anchor=NW)
        canvas.bind('<Button-1>',_on_click)
        canvas.bind("<B1-Motion>", _on_drag)
        canvas.bind('<Button-3>',delete_rectangle)
        canvas.bind("<ButtonRelease-1>", _on_drop, '+')
        crop_btn = Button(top, text="Recortar imagen", state="disabled", bg="light green",command=verify)
        crop_btn.pack(side="bottom",expand=1, fill=X)
        top.mainloop()
    else:
        display.appendtext("PULSE \'BUSCAR\' PARA SELECCIONAR UN ARCHIVO\n")

def name_file(cr,c,n):
    if cr == True:
        nf = n+"_crop "+str(count)+".png"
    else:
        nf = n+" "+str(count)+".png"
    return nf

def corta():
    global _start, _end, ver, count
    if ver == True:
        box = (_start+_end)
        cropped = True
    else:
        box = ((0,0)+size)
        cropped = False
        print(box)
    display.delete('1.0',END)
    display.appendtext("\nPROCESO EN CURSO\n")
    count=1
    archivo=(((archivo_selec).split("/"))[-1])
    #try:
    name,ex = os.path.splitext(archivo)
    for frame in ImageSequence.Iterator(im):
        nom_imagen=name_file(cropped,count,name)
        c_im=im.crop(box)
        c_im.save(nom_imagen)
        display.appendtext("\nExtraido frame: "+nom_imagen)
        count+=1
    display.appendtext("\n\nPROCESO FINALIZADO :D\n")
        
    #except:
        #display.appendtext("\nHUBO UN PROBLEMA AL REALIZAR LA OPERACIÓN")
    ver = False
    
def busca():
    global archivo_selec
    global im, size, archivo
    global _end, ver
    archivo_selec = askopenfilename(parent=ventana, initialdir="M:/",title='Elegir archivo.')
    archivo=(((archivo_selec).split("/"))[-1])
    if archivo_selec!="":
        try:
            im=Image.open(archivo_selec)
            size=(im.size)
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
                      text_background='black', text_width=73,
                      text_foreground='light blue', text_height=22,
                      text_padx=10, text_pady=10, text_relief='groove',
                      text_font=('Fixedsys', 10))
display.pack(padx=0,pady=0)

buttons = Pmw.ButtonBox(ventana,hull_background="LightBlue3")

buttons.pack(fill='both', expand=1, padx=1, pady=1)

buttons.add('LIMPIAR',bg='light green',command=12)
buttons.add('CONVERTIR',bg='light green')
buttons.add('CARPETA',bg='light green',command=direc)
buttons.add('EXTRAER',bg='light green',command=iniciar_extract)
buttons.add('BUSCAR',bg='light green',command=busca)
buttons.add('RECORTAR',bg='light green',command=recorte)

buttons.alignbuttons()

texto_inicio()

ventana.mainloop()




