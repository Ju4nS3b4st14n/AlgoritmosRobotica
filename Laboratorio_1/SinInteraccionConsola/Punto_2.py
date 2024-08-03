import numpy as np

matriz1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

matriz2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print("Matriz 1:\n", matriz1, "\nMatriz 2:\n", matriz2)

# Sumar las matrices
suma = matriz1 + matriz2

# Restar las matrices
resta = matriz1 - matriz2

# Multiplicar las matrices
producto_punto = np.dot(matriz1, matriz2)

# Producto cruz de los vectores
producto_cruz = np.cross(matriz1, matriz2)

# Dividir las matrices (elemento por elemento)
division = matriz1 / matriz2

print("La suma es:\n", suma,
      "\nLa resta es:\n", resta, 
      "\nEl producto punto es:\n", producto_punto, 
      "\nEl producto cruz es:\n", producto_cruz,
      "\nLa división es:\n", division
      )