from PIL import Image, ImageDraw, ImageFont
from VALID import ns, OKI
import os

def directorio():
    while True:
        dire = input("Introduce ruta al archivo: ")
        if os.path.isdir(dire):
            os.chdir(dire)
            break
        else:
            print("DIRECTORIO NO VÁLIDO")

def abre_archivo():
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
    #cuent+=1

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

def main():
    while True:
        directorio()
        archivo = abre_archivo()
        texto = input("Introduzca texto a insertar: ")
        font = fuente()
        cuenta=1
        color="white"
        for i in os.listdir():
            if i.startswith(archivo):
                inserta_texto(i,font,texto,cuenta,color)
        conti = ns(input("¿Desea continuar?: "))
        if conti=="n":
            break

main()
