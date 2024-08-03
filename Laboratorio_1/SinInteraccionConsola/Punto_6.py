import math

#Fuerza de avance ## descripcion
def f_de_avance(presion, diametro_piston):
    area = (diametro_piston / 2) ** 2 * math.pi     # Área del pistón (A = π * r^2)
    fuerza = presion * area                         # Fuerza = Presión * Área
    return fuerza

#fuerza de retroceso
def f_de_retroceso(presion, diametro_piston, diametro_vastago):
    area_piston = (diametro_piston / 2) ** 2 * math.pi     # Área del pistón (A = π * r^2)
    area_vastago = (diametro_vastago / 2) ** 2 * math.pi   # Área de la barra (A = π * r^2)
    area_efectiva = area_piston - area_vastago             # Área efectiva para el retroceso
    fuerza = presion * area_efectiva                       # Fuerza = Presión * Área efectiva
    return fuerza

# Datos del cilindro
P_KPa = float(600)
presion = float(P_KPa*1000)
print("Presion del cilindro doble efecto:              {:.2f}".format(P_KPa),"KPa")        #Presion en kilo-pascales
mm_piston = float(32)
diametro_piston = float(mm_piston/1000)
print("Diámetro del pistón del cilindro doble efecto:   {:.2f}".format(mm_piston),"mm")    #Diametro en milímetros
mm_vastago = float(10)
diametro_vastago = float(mm_vastago/1000)
print("Diámetro del vastago del cilindro doble efecto:  {:.2f}".format(mm_vastago), "mm")  #Diametro en milímetros

# Calcular fuerza de avance y retroceso
fuerza_avance = f_de_avance(presion, diametro_piston)
fuerza_retroceso = f_de_retroceso(presion, diametro_piston, diametro_vastago)

# Mostrar resultados
print("\nFuerza de avance del cilindro:     {:.2f} N".format(fuerza_avance))      #fuerza en Newton
print("Fuerza de retroceso del cilindro:  {:.2f} N".format(fuerza_retroceso))     #fuerza en Newton