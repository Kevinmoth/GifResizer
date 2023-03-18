from PIL import Image, ImageSequence
import tkinter as tk
from tkinter import filedialog

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.minsize(400, 200) 
        self.pack(expand=True, fill="both") 
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self)
        frame.pack(side="top", padx=20, pady=20)

        self.select_button = tk.Button(frame, text="Seleccionar archivo", command=self.open_file, width=20)
        self.select_button.pack(side="top", pady=10)

        size_label = tk.Label(frame, text="Tamaño de salida:")
        size_label.pack(side="top", pady=5)
        self.size_entry = tk.Entry(frame)
        self.size_entry.insert(0, "320x240")
        self.size_entry.pack(side="top", pady=5)

        self.convert_button = tk.Button(frame, text="Convertir archivo", command=self.convert_file, width=20)
        self.convert_button.pack(side="top", pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename()

        self.select_button.configure(text=file_path)

        self.file_path = file_path

    def convert_file(self):
        size_str = self.size_entry.get()
        size = tuple(map(int, size_str.split("x")))
        im = Image.open(self.file_path)

        frames = ImageSequence.Iterator(im)

        def thumbnails(frames):
            for frame in frames:
                thumbnail = frame.copy()
                thumbnail.thumbnail(size, Image.ANTIALIAS)
                yield thumbnail

        frames = thumbnails(frames)

        output_path = self.file_path.split(".")[0] + "_out.gif"

        om = next(frames)
        om.info = im.info

        om.save(output_path, save_all=True, append_images=list(frames))

root = tk.Tk()
root.title("GifRezizer by Matecitos")
app = Application(master=root)
app.mainloop()
