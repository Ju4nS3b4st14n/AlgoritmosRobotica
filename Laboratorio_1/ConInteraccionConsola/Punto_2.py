import random

# SOLICITA INFORMACION AL USUARIO
maximo = int(input("Digite el rango máximo: "))
minimo = int(input("Digite el rango mínimo: "))
numeros = int(input("Digite cuantos numeros aleatorios: "))
Aleatorios = []

# SE GENERAN LOS NUMEROS ALEATORIOS
for i in range(0,numeros):
    b = random.randint(minimo,maximo)
    Aleatorios.append(b)
    
print("Numeros aleatorios: ",Aleatorios)