
from mpu6050 import mpu6050
from time import sleep

# Inicializar MPU6050
sensor = mpu6050(0x68)

while True:
    # Leer datos del acelerómetro y giroscopio
    accel_data = sensor.get_accel_data()
    gyro_data = sensor.get_gyro_data()

    # Imprimir datos en la consola
    print("ax:", accel_data['x'], "ay:", accel_data['y'], "az:", accel_data['z'])
    print("gx:", gyro_data['x'], "gy:", gyro_data['y'], "gz:", gyro_data['z'])

    # Esperar medio segundo antes de la siguiente lectura
    sleep(0.5)
