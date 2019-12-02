import Pmw
import time
from PIL import Image, ImageSequence
from tkinter import filedialog
import threading
import os

ventana = Pmw.initialise(fontScheme = 'pmw1')
ventana.title("GIF CUTTER")
archivo_selec = ""
im = ""

def clear():
    display.clear()
    texto_inicio()

def iniciar_extract():
    t=threading.Thread(target=corta)
    t.start()

def corta():
    count=1
    archivo=(((archivo_selec).split("/"))[-1])
    try:
        name,ex = os.path.splitext(archivo)
        for frame in ImageSequence.Iterator(im):
            nom_imagen=name+" "+str(count)+'.png'
            im.save(nom_imagen)
            display.appendtext("\nExtraido frame: "+nom_imagen)
            count+=1
    except:
        display.appendtext("\nHUBO UN PROBLEMA AL REALIZAR LA OPERACIÓN")
        
def busca():
    global archivo_selec
    global im
    archivo_selec=filedialog.askopenfilename(initialdir = "/",
    title = "Seleccione archivo",filetypes = (("gif","*.*"),
    ("webp","*.*")))
    if archivo_selec!="":
        try:
            im=Image.open(archivo_selec)
            time.sleep(1)
            display.appendtext("Dir: "+archivo_selec+"\n")
        except:
            archivo_selec = ""
            display.appendtext("NO SE PUDO ABRIR EL ARCHIVO\n")
    
def texto_inicio():
    display.appendtext("Pulse \'BUSCAR\' para escoger archivo.\n")

display = Pmw.ScrolledText(ventana, hscrollmode='none',
                      vscrollmode='dynamic', hull_relief='sunken',#vscrollmode=dynamic
                      hull_background='gray20', hull_borderwidth=10,
                      text_background='honeydew4', text_width=55, #ancho pantalla
                      text_foreground='black', text_height=17, #alto pantalla
          text_padx=10, text_pady=10, text_relief='groove',
                      text_font=('Fixedsys', 10))
display.pack(padx=0,pady=0)

buttons = Pmw.ButtonBox(ventana)

buttons.pack(fill='both', expand=1, padx=1, pady=1)

buttons.add('LIMPIAR',bg='light blue',command=clear,width=12)
buttons.add('CARPETA',bg='light blue')
buttons.add('EXTRAER',bg='light blue',command=iniciar_extract)
buttons.add('BUSCAR',bg='light blue',command=busca)
buttons.alignbuttons()

texto_inicio()

ventana.mainloop()

