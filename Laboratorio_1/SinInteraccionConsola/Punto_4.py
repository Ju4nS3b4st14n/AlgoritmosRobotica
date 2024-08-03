def resistencia_PT100pos(temperatura):
    # Coeficientes de la ecuación de Callendar-Van Dusen
    A = 3.9083e-3
    B = -5.775e-7
    C = -4.183e-12

    # Resistencia a 0°C
    R0 = 100.0  # en ohmios

    # Calcula la resistencia en función de la temperatura utilizando la ecuación de Callendar-Van Dusen
    resistencia = R0 * (1 + A * temperatura + B * temperatura ** 2)
    return resistencia

def resistencia_PT100neg(temperatura):
    # Coeficientes de la ecuación de Callendar-Van Dusen
    A = 3.9083e-3
    B = -5.775e-7
    C = -4.183e-12

    # Resistencia a 0°C
    R0 = 100.0  # en ohmios

    # Calcula la resistencia en función de la temperatura utilizando la ecuación de Callendar-Van Dusen
    resistencia = R0 * ((1) + (A * temperatura) + (B * temperatura ** 2)+( C * (temperatura-100) * pow(temperatura,3) ))
    return resistencia

temp1 = float(200) #Temperatura en grados celsius
temp2 = float(-66)

# Calcular la resistencia para la temperatura dada
resistencia1 = resistencia_PT100pos(temp1)
resistencia2 = resistencia_PT100neg(temp2)

# Mostrar el resultado
print("La resistencia de la RTD a {:.2f}".format(temp1), "°C es de: {:.2f}".format(resistencia1), "ohmios")
print("La resistencia de la RTD a {:.2f}".format(temp2), "°C es de: {:.2f}".format(resistencia2), "ohmios")