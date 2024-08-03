import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Determina el tipo de sistema según el valor de zeta
def tipo_sistema(zeta):
    if zeta < 1:
        return 'Subamortiguado'
    elif zeta == 1:
        return 'Críticamente amortiguado'
    else:
        return 'Sobreamortiguado'

# Coeficientes de la función de transferencia (K, wn, zeta)
K = float(input("Ingrese el coeficiente K: "))
wn = float(input("Ingrese la frecuencia natural wn: "))
zeta = float(input("Ingrese la razón de amortiguamiento zeta: "))

# Tipo de sistema
tipo = tipo_sistema(zeta)
print("\nTipo de sistema:", tipo)

# Crear la función de transferencia de segundo orden
num = [K * wn**2]
den = [1, 2 * zeta * wn, wn**2]
sys = signal.TransferFunction(num, den)

# Tiempo de respuesta
tiempo, respuesta = signal.step(sys)

# Gráfico
plt.figure(figsize=(10, 6))
plt.plot(tiempo, respuesta, label='Respuesta')
plt.title('Respuesta de la función de transferencia de segundo orden')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()
plt.show()