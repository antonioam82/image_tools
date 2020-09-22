import ffmpeg
import pprint
from VALID import ns

while True:
    ruta = input("Introduce ruta al archivo: ")
    try:
        probe = ffmpeg.probe(ruta)
        video_streams = [stream for stream in
        probe["streams"] if stream["codec_type"] == "video"]
        pprint.pprint(video_streams[0])
    except:
        print("No se pudo obtener la información requerida.")

    conti = ns(input("¿Desea continuar?(n/s): "))
    if conti == "n":
        break
