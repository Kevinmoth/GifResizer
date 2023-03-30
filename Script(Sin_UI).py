from PIL import Image, ImageSequence

size = 640, 480  # Tamaño de salida
im = Image.open("archivo_de_entrada.gif")
frames = ImageSequence.Iterator(im)
def thumbnails(frames):
    for frame in frames:
        thumbnail = frame.copy()
        thumbnail.thumbnail(size, Image.ANTIALIAS)
        yield thumbnail
frames = thumbnails(frames)
om = next(frames) 
om.info = im.info 
om.save("Archivo_de_salida.gif", save_all=True, append_images=list(frames))