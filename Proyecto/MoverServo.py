from adafruit_servokit import ServoKit
from adafruit_pca9685 import PCA9685
import board
import busio
import time   
from Robot import *

i2c=busio.I2C(board.SCL,board.SDA)
pca=PCA9685(i2c)
pca.frequency=60
servo_min=980
servo_max=1970

def MoverServo(q1, q2, q3, q4):
    
    q3 = 180 - q3
    q4 = 180 - q4
                
    if q1 == 0:
        q1 = 5
                    
    elif  q1 == 180:
        q1 = 175
                
    if q2 == 0:
        q2 = 5
                    
    elif  q2 == 180:
        q2 = 175
                    
    if q3 == 0:
        q3 = 5
                    
    elif  q3 == 180:
        q3 = 175

    if q4 == 0:
        q4 = 5
                    
    elif  q4 == 180:
        q4 = 175
        

    pulse_width=int((q1/22)*(servo_max-servo_min)+servo_min)
    pca.channels[15].duty_cycle=pulse_width
       
    pulse_width=int((q2/22)*(servo_max-servo_min)+servo_min)
    pca.channels[0].duty_cycle=pulse_width
    
    pulse_width=int((q3/22)*(servo_max-servo_min)+servo_min)
    pca.channels[8].duty_cycle=pulse_width

    pulse_width=int((q4/24)*(servo_max-servo_min)+servo_min)
    pca.channels[12].duty_cycle=pulse_width

    time.sleep(0.09)

    return

def MoverServoAuto(punto):

    if punto == "A":

        for i in range(90, -1, -5):

            q1 = int(numpy.deg2rad(i))
            q2 = int(numpy.deg2rad(0))
            q3 = int(numpy.deg2rad(90))
            q4 = int(numpy.deg2rad(90))
            
            auto(q1, q2, q3, q4)
            MoverServo(i, 20, 90, 90)

            print("Movimiento punto A")
        time.sleep(3)

        for i in range(0, 95, 5):

            q1 = int(numpy.deg2rad(i))
            q2 = int(numpy.deg2rad(0))
            q3 = int(numpy.deg2rad(90))
            q4 = int(numpy.deg2rad(90))
            
            auto(q1, q2, q3, q4)
            MoverServo(i, 20, 90, 90)

            print("punto B")

    if punto == "B":

        for i in range(0, 91, 5):

            q1 = int(numpy.deg2rad(i))
            q2 = int(numpy.deg2rad(0))
            q3 = int(numpy.deg2rad(90))
            q4 = int(numpy.deg2rad(90))
            
            auto(q1, q2, q3, q4)
            MoverServo(i, 20, 90, 90)

            print("punto B")
        time.sleep(3)

    if punto == "C":

        for i in range(90, 181, 5):
            q1 = int(numpy.deg2rad(i))
            q2 = int(numpy.deg2rad(0))
            q3 = int(numpy.deg2rad(90))
            q4 = int(numpy.deg2rad(90))

            auto(q1, q2, q3, q4)
            MoverServo(i, 20, 90, 90)
        
        print("Movimiento punt C")
        time.sleep(3)

        for i in range(180, 90, -5):
            q1 = int(numpy.deg2rad(i))
            q2 = int(numpy.deg2rad(0))
            q3 = int(numpy.deg2rad(90))
            q4 = int(numpy.deg2rad(90))
            
            auto(q1, q2, q3, q4)
            MoverServo(i, 20, 90, 90)

        print("Movimiento punto B")

def gripperopen(q):

    pulse_width=int((q/24)*(servo_max-servo_min)+servo_min)
    pca.channels[7].duty_cycle=0

def gripperclose(q):

    pulse_width=int((q/24)*(servo_max-servo_min)+servo_min)
    pca.channels[7].duty_cycle=0