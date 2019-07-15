from PIL import Image, ImageDraw, ImageFont
from VALID import ns, OKI
import os

#INTRODUCIENDO TEXTO (CENTRADO) SOBRE CONJUNTOS DE IMAGENES REPETIDAS

def directorio():
    while True:
        dire = input("Introduce ruta al archivo: ")
        if os.path.isdir(dire):
            os.chdir(dire)
            break
        else:
            print("DIRECTORIO NO VÁLIDO")

def encuentra_archivo():
    while True:
        inicial = input("Introduce inicial del archivo/s sobre los que desea insertar texto: ")
        for i in os.listdir():
            if i.startswith(inicial) and inicial!="":
                print("founded")
                return inicial
                break
        print("INICIAL NO ENCONTRADA")


def inserta_texto(img, font, text, cuent,color):
    base = Image.open(img).convert('RGBA')
    #print(img)
    #separa_texto=img.split(".")
    #nombre_archivo = separa_texto[0]
    #print(nombre_archivo)
    txt = Image.new("RGBA", base.size, (255,255,255,0))
    draw = ImageDraw.Draw(txt)
    text_width, text_height = draw.textsize(text, font)
    position = ((base.size[0]-text_width)/2,(base.size[1]-text_height)/2)
    draw.text(position, text, color, font=font)
    out = Image.alpha_composite(base, txt)
    out.convert('RGBA')#
    out.save(img)
    print("Texto insertado en ",img)
    #cuent+=1

def color_numero(n):
    while n<0 or n>255:
        n = OKI(input("Introduzca cifra entre 0 y 255: "))
    return n
        

def fuente():
    while True:
        fuen = input("Establezca tipo de fuente: ")
        tama = OKI(input("Establezca tamaño de la fuente: "))
        try:
            fnt = ImageFont.truetype(fuen, tama)
            return fnt
            break
        except:
            print("NO SE PUDO ESTABLECER LA FUENTE ESPECIFICADA")

def color_texto():
    col = ns(input("¿Definir color del texto?: "))
    if col == "s":
        rojo = color_numero(OKI(input("Introduce valor para ROJO: ")))
        verde = color_numero(OKI(input("Introduce valor para VERDE: ")))
        azul = color_numero(OKI(input("Introduce valor para AZUL: ")))
        opac = color_numero(OKI(input("Introduce valor de opacidad: ")))
        tup_color = (rojo,verde,azul,opac)
    else:
        tup_color = (255,255,255,255)
    return tup_color

def main():
    while True:
        directorio()
        archivo = encuentra_archivo()
        texto = input("Introduzca texto a insertar: ")
        font = fuente()
        cuenta=1
        color=color_texto()
        for i in os.listdir():
            if i.startswith(archivo):
                try:
                    inserta_texto(i,font,texto,cuenta,color)
                except:
                    print("LA OPERACIÓN NO PUDO LLEVARSE A CABO PARA EL ARCHIVO ",i)
        conti = ns(input("¿Desea continuar?: "))
        if conti=="n":
            break

main()

