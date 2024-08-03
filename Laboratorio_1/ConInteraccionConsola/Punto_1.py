# SOLICITAR AL USUARIO VALORES DE VOLTAJE Y CORRIENTE
Voltaje = input("Digite el valor de Voltaje (V): ")
Corriente = input("Digite el valor de la Corriente (A): ")

# CONVERTIR VALORES A FLOTANTES Y REALIZAR OPERACION
Potencia = float(Voltaje) * float(Corriente)
# IMPRIMIR POTENCIA RESULTANTE
print("La potencia del circuito es: {:.2f}".format(Potencia), "W")