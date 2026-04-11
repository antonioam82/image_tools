from PIL import Image, ImageSequence

def convertir_webp_a_gif(input_path, output_path, dimensiones=None, duracion_ms=100):
    """
    Convierte un WebP a GIF.
    - dimensiones: Tupla (ancho, alto). Si es None, mantiene el original.
    - duracion_ms: Tiempo en milisegundos por cada fotograma.
    """
    try:
        with Image.open(input_path) as img:
            # Extraer todos los fotogramas del WebP
            frames = []
            for frame in ImageSequence.Iterator(img):
                # Convertir a formato RGBA para preservar transparencias si es necesario
                # Luego a P (paletizado) que es el estándar para GIFs
                f = frame.copy().convert("RGBA")
                
                if dimensiones:
                    f = f.resize(dimensiones, Image.Resampling.LANCZOS)
                
                frames.append(f.convert("P", palette=Image.Palette.ADAPTIVE))

            # Guardar como GIF animado
            frames[0].save(
                output_path,
                save_all=True,
                append_images=frames[1:],
                duration=duracion_ms,
                loop=0, # 0 significa bucle infinito
                optimize=True
            )
            print(f"Éxito: Archivo guardado en {output_path}")

    except Exception as e:
        print(f"Error al convertir: {e}")

# --- CONFIGURACIÓN ---
archivo_entrada = "animacion.webp"
archivo_salida = "resultado.gif"
nuevas_dimensiones = (500, 500)  # (Ancho, Alto) o None para original
velocidad = 80                   # Milisegundos entre fotogramas (menor = más rápido)

convertir_webp_a_gif(archivo_entrada, archivo_salida, nuevas_dimensiones, velocidad)
