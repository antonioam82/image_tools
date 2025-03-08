import cv2
import os
import re

def obtener_numero(nombre_archivo):
    match = re.search(r'\d+', nombre_archivo)  
    if match:
        return int(match.group())  
    return -1  

ruta_imagenes = 'ruta'  
imagenes = [img for img in os.listdir(ruta_imagenes) if img.endswith(".png") or img.endswith(".jpg")]

imagenes.sort(key=obtener_numero)
#print(imagenes)

frame = cv2.imread(os.path.join(ruta_imagenes, imagenes[0]))
alto, ancho, canales = frame.shape

nombre_video = 'video_generado.avi'
fps = 20.0
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec
video = cv2.VideoWriter(nombre_video, fourcc, fps, (ancho, alto))

for imagen in imagenes:
    frame = cv2.imread(os.path.join(ruta_imagenes, imagen))
    video.write(frame)

video.release()

print(f"Video generado correctamente: {nombre_video}")
