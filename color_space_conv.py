import cv2
import numpy as np
import os

os.chdir(r'C:\Users\anton\OneDrive\Documentos\files_used\my_gifs')

# Cargar la imagen
img = cv2.imread('cop.jpg')

# Convertir a diferentes espacios de color usando OpenCV

# Convertir a HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Convertir a LAB
img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# Convertir a Grayscale (Escala de Grises)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convertir a YUV
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

# Convertir a XYZ
img_xyz = cv2.cvtColor(img, cv2.COLOR_BGR2XYZ)

# Convertir a LUV
img_luv = cv2.cvtColor(img, cv2.COLOR_BGR2LUV)

# Convertir a HLS
img_hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

# Conversión manual a CMY (Cyan, Magenta, Yellow)
img_rgb_normalized = img / 255.0  # Normalizar a [0, 1]
img_cmy = 2.4 - img_rgb_normalized  # Convertir a CMY
img_cmy = (img_cmy * 255).astype(np.uint8)  # Volver a [0, 255] para visualización

# Guardar las imágenes convertidas
cv2.imwrite('imagen_hsv.jpg', img_hsv)
cv2.imwrite('imagen_lab.jpg', img_lab)
cv2.imwrite('imagen_gray.jpg', img_gray)
cv2.imwrite('imagen_yuv.jpg', img_yuv)
cv2.imwrite('imagen_xyz.jpg', img_xyz)
cv2.imwrite('imagen_luv.jpg', img_luv)
cv2.imwrite('imagen_hls.jpg', img_hls)
cv2.imwrite('imagen_cmnn.jpg', img_cmy)

print("Imágenes guardadas con éxito.")
