import cv2
import numpy as np
import math

# Definir algunos colores comunes en formato RGB
common_colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0)
}

# Función para calcular la distancia Euclidiana entre dos colores RGB
def euclidean_distance(color1, color2):
    return math.sqrt((color1[0] - color2[0]) ** 2 + (color1[1] - color2[1]) ** 2 + (color1[2] - color2[2]) ** 2)

# Función para encontrar el color más cercano de la lista de colores comunes
def closest_color(color):
    min_distance = float('inf')
    closest_name = None
    for name, common_color in common_colors.items():
        dist = euclidean_distance(color, common_color)
        if dist < min_distance:
            min_distance = dist
            closest_name = name
    return closest_name

# Función para identificar la figura
def identify_shape(contour):
    # Aproximar el contorno a un polígono (reduce el número de vértices)
    epsilon = 0.04 * cv2.arcLength(contour, True)  # Tolerancia para la aproximación
    approx = cv2.approxPolyDP(contour, epsilon, True)

    # Obtener el número de vértices
    num_vertices = len(approx)

    # Identificar la figura según el número de vértices
    if num_vertices == 3:
        return "Triángulo", (0, 255, 0)  # Verde
    elif num_vertices == 4:
        # Rectángulo o Cuadrado
        # Verificar si es un cuadrado o un rectángulo (usando la relación de aspecto)
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = float(w) / h
        if 0.95 < aspect_ratio < 1.05:
            return "Cuadrado", (0, 0, 255)  # Rojo
        else:
            return "Rectángulo", (0, 0, 255)  # Rojo
    elif num_vertices > 4:
        print("Circulo")
        return "Circulo", (255, 0, 0)  # Azul
    else:
        # Si no tiene los vértices suficientes, puede ser un círculo (aproximación por redondez)
        # Calcular el área y el perímetro
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        if perimeter == 0:
            return "Desconocido", (255, 0, 0)  # Azul
        circularity = 4 * np.pi * (area / (perimeter ** 2))
        if 0.7 < circularity < 1.2:  # Umbral para redondez
            return "Círculo", (255, 255, 0)  # Amarillo
        else:
            return "Circulo", (255, 0, 0)  # Azul

def figure():

    # Cargar la imagen desde un archivo
    image = cv2.imread('imagen.jpg')

    # Verificar que la imagen se cargó correctamente
    if image is None:
        print("Error: No se pudo cargar la imagen.")
        exit()

    # Redimensionar la imagen (opcional, para mejorar el rendimiento)
    new_width = 640  # Puedes ajustar el tamaño
    height, width = image.shape[:2]
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio)
    resized_image = cv2.resize(image, (new_width, new_height))

    # Convertir la imagen redimensionada a escala de grises
    gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    # Aplicar un desenfoque para reducir el ruido
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detectar bordes usando el operador Canny
    edges = cv2.Canny(blurred, 50, 150)

    # Encontrar los contornos
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Verificar si se encontraron contornos
    if len(contours) == 0:
        print("No se encontraron contornos.")
    else:
        print(f"Se encontraron {len(contours)} contornos.")

    # Crear una máscara en blanco (negra con los contornos blancos)
    mask = np.zeros(gray.shape, dtype=np.uint8)

    # Rellenar la máscara con los contornos detectados (blanco)
    cv2.drawContours(mask, contours, -1, (255), thickness=cv2.FILLED)

    # Extraer los colores de la región de la figura usando la máscara
    masked_image = cv2.bitwise_and(resized_image, resized_image, mask=mask)

    # Calcular el promedio de color en la máscara (la figura)
    mean_color = cv2.mean(resized_image, mask=mask)

    # Obtener el color promedio en formato BGR
    mean_bgr = mean_color[:3]
    print(f"Promedio de color (BGR): {mean_bgr}")

    if mean_bgr[1] > mean_bgr[0] and mean_bgr[1] > mean_bgr[2]:
        color_figure = (0, 255, 0)
    elif mean_bgr[2] > mean_bgr[0] and mean_bgr[2] > mean_bgr[1]:
        color_figure = (255, 0, 0)
    else:
        print("No se detecta el color claramente, revisar iluminación del ambiente")

    # Encontrar el nombre del color más cercano
    color_name = closest_color(color_figure)
    print(f"Nombre aproximado del color: {color_name}")

    # Identificar la figura en cada contorno
    for contour in contours:
        shape, color = identify_shape(contour)
        # Aproximar el contorno y dibujar la figura
        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        
        # Dibujar el contorno y el nombre de la figura
        #cv2.drawContours(resized_image, [approx], -1, color, 2)
        x, y = approx.ravel()[0], approx.ravel()[1]  # Coordenadas para colocar el texto
        cv2.putText(resized_image, shape, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    # Dibujar los contornos directamente sobre la imagen original
    cv2.drawContours(resized_image, contours, -1, (0, 255, 0), 2)

    # Guardar la imagen con los contornos dibujados sobre la original
    image_figute = cv2.imwrite("imagen.jpg", resized_image)
    print("Imagen con contornos guardada como 'imagen.jpg'")

    return color_name

