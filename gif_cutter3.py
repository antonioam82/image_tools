import Pmw
import PIL

ventana = Pmw.initialise(fontScheme = 'pmw1')
ventana.title("GIF CUTT3R")

def clear():
    display.clear()

def texto_inicio():
    display.appendtext("Pulse \'BUSCAR\' para escoger archivo.")

display = Pmw.ScrolledText(ventana, hscrollmode='none',
                      vscrollmode='dynamic', hull_relief='sunken',#vscrollmode=dynamic
                      hull_background='gray20', hull_borderwidth=10,
                      text_background='honeydew4', text_width=50, #ancho pantalla
                      text_foreground='black', text_height=15, #alto pantalla
          text_padx=10, text_pady=10, text_relief='groove',
                      text_font=('Fixedsys', 10))
display.pack(padx=0,pady=0)

buttons = Pmw.ButtonBox(ventana)
buttons.pack(fill='both', expand=1, padx=1, pady=1)

buttons.add('LIMPIAR',bg='light blue',command=clear,width=15)
buttons.add('CORTAR',bg='light blue')
buttons.add('BUSCAR',bg='light blue')
buttons.alignbuttons()

texto_inicio()

ventana.mainloop()
