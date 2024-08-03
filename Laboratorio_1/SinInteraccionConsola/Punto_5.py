import numpy as np

#Función para realizar una rotación en el eje X.
def rotacion_x(angulo):
    rad = np.radians(angulo)
    matriz = np.array([[     1     ,     0      ,       0     ],
                       [     0     , np.cos(rad), -np.sin(rad)],
                       [     0     , np.sin(rad), np.cos(rad)]])
    return matriz

#Función para realizar una rotación en el eje Y.
def rotacion_y(angulo):
    rad = np.radians(angulo)
    matriz = np.array([[ np.cos(rad),       0     , np.sin(rad)],
                       [      0     ,       1     ,      0     ],
                       [-np.sin(rad),       0     , np.cos(rad)]])
    return matriz

#Función para realizar una rotación en el eje X.
def rotacion_z(angulo):
    rad = np.radians(angulo)
    matriz = np.array([[np.cos(rad), -np.sin(rad),       0     ],
                       [np.sin(rad),  np.cos(rad),       0     ],
                       [     0     ,       0     ,       1     ]])
    return matriz

# Función para mostrar una matriz con valores de tres decimales
def mostrar_matriz(matriz):
    for fila in matriz:
        print("[", end="")
        for valor in fila:
            print("{:.3f}".format(valor), end=", ")
        print("]")

# Angulo de rotacion en grados
angulo = float(60)
print("Ángulo de rotación: {:.2f}".format(angulo),"° \n")

# Rotación en el eje X
matriz_rotacion_x = rotacion_x(angulo)
print("Matriz de rotación en el eje X:")
mostrar_matriz(matriz_rotacion_x)

# Rotación en el eje Y
matriz_rotacion_y = rotacion_y(angulo)
print("\nMatriz de rotación en el eje Y:")
mostrar_matriz(matriz_rotacion_y)

# Rotación en el eje Z
matriz_rotacion_z = rotacion_z(angulo)
print("\nMatriz de rotación en el eje Z:")
mostrar_matriz(matriz_rotacion_z)