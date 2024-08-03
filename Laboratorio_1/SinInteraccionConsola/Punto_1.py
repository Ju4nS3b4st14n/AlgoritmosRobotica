import numpy as np

# Definir los vectores
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

print("Vector 1:", vector1, "Vector 2:", vector2)

# Sumar los vectores
suma = vector1 + vector2

# Restar los vectores
resta = vector1 - vector2

# Producto punto de los vectores
producto_punto = np.dot(vector1, vector2)

# Producto cruz de los vectores
producto_cruz = np.cross(vector1, vector2)

# Dividir elemento por elemento
division_elemento_por_elemento = vector1 / vector2

print("La suma es:", suma,
      "\nLa resta es:", resta, 
      "\nEl producto punto es:", producto_punto, 
      "\nEl producto cruz es:", producto_cruz,
      "\nLa división es:", division_elemento_por_elemento
      )