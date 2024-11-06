import cv2  # Importar OpenCV

def Imagen(img):

    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)     

    # Obtener contornos
    _, binaria = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contornos, _ = cv2.findContours(binaria, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    coordenadas_x = []
    coordenadas_y = []
        
    # Imprimir las coordenadas de los contornos
    for contour in contornos:
        for punto in contour:
            x, y = punto[0]
            coordenadas_x.append(x)
            coordenadas_y.append(y)

    return coordenadas_x, coordenadas_y