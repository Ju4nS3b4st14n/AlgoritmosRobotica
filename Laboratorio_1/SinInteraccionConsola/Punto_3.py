import numpy as np

def cartesiana_a_cilindrica(x, y, z):
    r = np.sqrt(x**2 + y**2)     # Radio en el plano XY
    theta = np.arctan2(y, x)     # Ángulo en el plano XY (en radianes)
    z_cilindrica = z             # La coordenada z permanece igual en coordenadas cilíndricas
    return r, theta, z_cilindrica

def cartesiana_a_esferica(x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)  # Radio esférico
    theta = np.arctan2(y, x)         # Ángulo en el plano XY, ángulo polar (en radianes)
    phi = np.arccos(z / r)           # Ángulo respecto al eje Z, ángulo azimutal (en radianes)
    return r, theta, phi

# Coordenadas rectangulares 
print("\nCoordenadas rectangulares:\n")
x = float(-1)
y = float(1)
z = float(2.44948974) #raiz de 6
print("x: {:.3f}".format(x), "y: {:.3f}".format(y), "z: {:.3f}".format(z))

# Conversión a coordenadas cilíndricas
r_cilindrica, theta_cilindrica, z_cilindrica = cartesiana_a_cilindrica(x, y, z)
print("\nCoordenadas rectangulares a coordenadas cilíndricas:\n")
print("r: {:.3f}".format(r_cilindrica), "theta: {:.3f}".format(theta_cilindrica), "z: {:.3f}".format(z_cilindrica))

# Conversión a coordenadas esféricas
r_esferica, phi_esferica, theta_esferica = cartesiana_a_esferica(x, y, z)
print("\nCoordenadas rectangulares a coordenadas esféricas:\n")
print("r: {:.3f}".format(r_esferica), "theta: {:.3f}".format(phi_esferica), "phi: {:.3f}".format(theta_esferica))