from adafruit_servokit import ServoKit
from adafruit_pca9685 import PCA9685
import numpy
import board
import busio
import time 

i2c=busio.I2C(board.SCL,board.SDA)
pca=PCA9685(i2c)
pca.frequency=60
servo_min=980
servo_max=1970

def MoverServo(q1, q2):

    q1s = int(numpy.rad2deg(q1))
    q2s = int(numpy.rad2deg(q2))

    if q1s == 0:
        q1s = 5

    if q1s == 180:
        q1s = 175

    if q2s == 0:
        q2s = 5

    if q2s == 180:
        q2s = 175

    pulse_width=int((q1s/24)*(servo_max-servo_min)+servo_min) #28 para servomotor pequeño
    pca.channels[15].duty_cycle=pulse_width
        
    pulse_width=int((q2s/21)*(servo_max-servo_min)+servo_min) #28 para servomotor pequeño
    pca.channels[14].duty_cycle=pulse_width