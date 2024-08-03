import numpy as np
import matplotlib.pyplot as plt

def carga_y_descarga(V, R, C, t):
    tau = R * C
    # Carga
    V_carga = V * (1 - np.exp(-t / tau))
    # Descarga
    V_descarga = V * np.exp(-t / tau)
    return V_carga, V_descarga

def graficar(V, R, C):
    t_carga = np.linspace(0, 5*R*C, 500)          # Intervalo de tiempo para la carga en milisegundos
    t_descarga = np.linspace(5*R*C, 10*R*C, 500)  # Intervalo de tiempo para la descarga en milisegundos

    V_carga, V_descarga = carga_y_descarga(V, R, C, t_carga)

    plt.figure(figsize=(10, 6))
    # Graficar la carga
    plt.plot(t_carga, V_carga, label='Carga', color='blue')
    # Graficar la descarga conectada a la carga
    plt.plot(t_descarga, V_descarga, label='Descarga', color='red')
    plt.title('Carga y Descarga en un Circuito RC')
    plt.xlabel('Tiempo (ms)')
    plt.ylabel('Voltaje (V)')
    plt.legend(['Carga','Descarga'])
    plt.grid(True)
    plt.show()

# Pedir al usuario que ingrese los valores
V = float(input("Ingrese el voltaje (V): "))
R = float(input("Ingrese la resistencia (Ω): "))
C = float(input("Ingrese la capacitancia (μF): "))

# Llamar a la función para graficar
graficar(V, R, C)