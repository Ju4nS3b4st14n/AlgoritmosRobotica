import cv2

def cargar_imagen(ruta):
    """Carga una imagen desde la ruta especificada."""
    imagen = cv2.imread(ruta)
    if imagen is None:
        print(f"No se pudo cargar la imagen desde '{ruta}'")
    return imagen

def reducir_tamaño(imagen, factor=0.5):
    """Reduce el tamaño de la imagen por un factor dado."""
    return cv2.resize(imagen, None, fx=factor, fy=factor, interpolation=cv2.INTER_AREA)

def obtener_contornos(imagen_gris):
    """Encuentra y devuelve los contornos en una imagen binarizada."""
    _, binaria = cv2.threshold(imagen_gris, 127, 255, cv2.THRESH_BINARY)
    contornos, _ = cv2.findContours(binaria, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    return contornos

def mostrar_contornos(imagen, contornos, nombre_ventana):
    """Dibuja los contornos en la imagen y la muestra en una ventana."""
    imagen_contornos = imagen.copy()
    cv2.drawContours(imagen_contornos, contornos, -1, (0, 255, 0), 2)
    cv2.imshow(nombre_ventana, imagen_contornos)

def imprimir_coordenadas(contornos, nombre_logo):
    """Imprime las coordenadas de los contornos."""
    print(f"\n\nCoordenadas {nombre_logo}\n\n")
    for contour in contornos:
        for punto in contour:
            x, y = punto[0]
            print(f"Coordenada: X={x}, Y={y}")

def main():
    # Cargar las imágenes
    kia = cargar_imagen("../AlgoritmosRobotica/Imagenes/Kia.jpg")
    chevrolet = cargar_imagen("../AlgoritmosRobotica/Imagenes/Chevrolet.jpg")

    # Reducir el tamaño de las imágenes
    kia = reducir_tamaño(kia)
    chevrolet = reducir_tamaño(chevrolet)

    # Convertir a escala de grises
    gray_maserati = cv2.cvtColor(kia, cv2.COLOR_BGR2GRAY)
    gray_peugeot = cv2.cvtColor(chevrolet, cv2.COLOR_BGR2GRAY)

    # Obtener contornos
    contornos_maserati = obtener_contornos(gray_maserati)
    contornos_peugeot = obtener_contornos(gray_peugeot)

    # Mostrar las imágenes con los contornos
    mostrar_contornos(kia, contornos_maserati, 'Contorno Logo Kia')
    mostrar_contornos(chevrolet, contornos_peugeot, 'Contorno Logo Chevrolet')

    # Imprimir las coordenadas de los contornos
    imprimir_coordenadas(contornos_maserati, 'Kia')
    imprimir_coordenadas(contornos_peugeot, 'Chevrolet')

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
