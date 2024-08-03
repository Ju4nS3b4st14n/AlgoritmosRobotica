import matplotlib.pyplot as plt
import numpy as np

def calcular_resistencia(temperatura):
      # Coeficientes de la ecuación de Callendar-Van Dusen
    A = 3.9083e-3
    B = -5.775e-7
    C = -4.183e-12

    # Resistencia a 0°C
    R0 = 100.0  # en ohmios

    if temperatura >= 0:
        resistencia = R0 * (1 + A * temperatura + B * temperatura ** 2)
    else:
        resistencia = R0 * (1 + A * temperatura + B * temperatura * 2 + C * (temperatura - 100) * temperatura * 3)
    
    return  resistencia

# Crear una lista de temperaturas en el rango de -200 a 200°C
temperaturas = np.linspace(-200, 200, 50)

# Calcular la resistencia para cada temperatura
resistencias = []
for temperatura in temperaturas:
    resistencias.append(calcular_resistencia(temperatura))

# Graficar la relación entre la resistencia y la temperatura
plt.plot(temperaturas, resistencias)
plt.title('PT100 -200 A 200 GRADOS CENTIGRADOS')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Resistencia (ohmios)')
plt.grid(True)
plt.show()