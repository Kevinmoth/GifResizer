from PIL import Image, ImageSequence
import tkinter as tk
from tkinter import filedialog

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.minsize(400, 200)  # Establecer tamaño mínimo de la ventana
        self.pack(expand=True, fill="both")  # Ajustar tamaño de marco al tamaño de la ventana
        self.create_widgets()

    def create_widgets(self):
        # Crear un marco para los widgets
        frame = tk.Frame(self)
        frame.pack(side="top", padx=20, pady=20)

        # Botón para abrir el archivo de entrada
        self.select_button = tk.Button(frame, text="Seleccionar archivo", command=self.open_file, width=20)
        self.select_button.pack(side="top", pady=10)

        # Entrada para introducir el tamaño de salida
        size_label = tk.Label(frame, text="Tamaño de salida:")
        size_label.pack(side="top", pady=5)
        self.size_entry = tk.Entry(frame)
        self.size_entry.insert(0, "320x240")
        self.size_entry.pack(side="top", pady=5)

        # Botón para ejecutar el script
        self.convert_button = tk.Button(frame, text="Convertir archivo", command=self.convert_file, width=20)
        self.convert_button.pack(side="top", pady=10)

    def open_file(self):
        # Abrir la ventana de selección de archivo
        file_path = filedialog.askopenfilename()

        # Actualizar la entrada de texto con la ruta del archivo seleccionado
        self.select_button.configure(text=file_path)

        # Guardar la ruta del archivo seleccionado para su uso posterior
        self.file_path = file_path

    def convert_file(self):
        # Obtener el tamaño de salida de la entrada de texto
        size_str = self.size_entry.get()
        size = tuple(map(int, size_str.split("x")))

        # Abrir el archivo de entrada
        im = Image.open(self.file_path)

        # Crear iterador de secuencia de imágenes
        frames = ImageSequence.Iterator(im)

        # Generador de miniaturas
        def thumbnails(frames):
            for frame in frames:
                thumbnail = frame.copy()
                thumbnail.thumbnail(size, Image.ANTIALIAS)
                yield thumbnail

        frames = thumbnails(frames)

        # Guardar el archivo de salida en la misma ubicación que el archivo de entrada
        output_path = self.file_path.split(".")[0] + "_out.gif"

        # Crear primera imagen
        om = next(frames)
        om.info = im.info

        # Guardar secuencia de imágenes en el archivo de salida
        om.save(output_path, save_all=True, append_images=list(frames))


root = tk.Tk()
root.title("GifRezizer by Matecitos")
app = Application(master=root)
app.mainloop()