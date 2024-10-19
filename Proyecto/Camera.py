import time
from picamera2 import Picamera2

# Inicializa la cámara
picam2 = Picamera2()

# Configura la cámara
picam2.configure(picam2.create_still_configuration())

# Genera un nombre de archivo único usando la fecha y hora
timestamp = time.strftime("%Y%m%d-%H%M%S")
filename = f"image_{timestamp}.jpg"

# Captura una imagen
picam2.start()  # Inicia la cámara
picam2.capture_file(filename)  # Captura la imagen
print(f"Imagen capturada: {filename}")
