import time
from picamera2 import Picamera2
from PIL import Image, ImageTk
import tkinter as tk

def photo():
    # Inicializa la cámara
    picam2 = Picamera2()

    # Configura la cámara
    picam2.configure(picam2.create_still_configuration())

    # Genera un nombre de archivo único 
    filename = f"imagen.jpg"

    # Captura una imagen
    picam2.start()  # Inicia la cámara
    picam2.capture_file(filename)  # Captura la imagen
    print(f"Imagen capturada: {filename}")

    return filename

def show_image(image_path):
    # Crear la ventana principal
    window = tk.Tk()
    window.title("Imagen Capturada")

    # Abre la imagen usando PIL
    img = Image.open(image_path)
    img = img.resize((400, 300))  # Cambiar el tamaño si es necesario

    # Convertir la imagen a un formato compatible con Tkinter
    img_tk = ImageTk.PhotoImage(img)

    # Crear un widget Label para mostrar la imagen
    label = tk.Label(window, image=img_tk)
    label.pack()

    # Iniciar el bucle principal de la interfaz gráfica
    window.mainloop()
