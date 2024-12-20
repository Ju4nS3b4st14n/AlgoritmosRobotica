import numpy
import math
from roboticstoolbox import *

l1 = 7
l2 = 6
n = 181

def Robot(x, y):

    d = numpy.zeros((3,n))
            
    Px = int(x)
    Py = int(y)

    b = math.sqrt(Px**2+Py**2)
    # Theta 2
    cos_theta2 = (b**2-l2**2-l1**2)/(2*l1*l2)
    sen_theta2 = math.sqrt(1-(cos_theta2)**2)#(+)codo abajo y (-)codo arriba
    theta2 = math.atan2(sen_theta2, cos_theta2)
    #print(f'theta 2 = {numpy.rad2deg(theta2):.4f}')
    # Theta 1
    alpha = math.atan2(Py,Px)
    phi = math.atan2(l2*sen_theta2, l1+l2*cos_theta2)
    theta1 = alpha - phi
    #print(f'theta 1 = {numpy.rad2deg(theta1):.4f}')

    if theta1 <= -numpy.pi:
        theta1 = (2*numpy.pi)+theta1

    q1 = theta1
    q2 = theta2
        
    if numpy.isnan(q1) or numpy.isnan(q2):
        q1 = 0
        q2 = 0

    R = []
    R.append(RevoluteDH(d=0, alpha=0, a=l1, offset=0))
    R.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))

    robot_instance = DHRobot(R, name='Bender')

    robot_instance.plot([q1, q2], backend='pyplot', limits=[-20, 20, -20, 20, -20, 20])

    return q1, q2

def Bender(min, max):

    d = numpy.zeros((3,n))

    R = []
    R.append(RevoluteDH(d=0, alpha=0, a=l1, offset=0))
    R.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))

    robot_instance = DHRobot(R, name='Bender')

    q1 = numpy.deg2rad(min)
    q2 = numpy.deg2rad(max)

    MTH = robot_instance.fkine([q1,q2])
    d[:,max] =  MTH.t 
    robot_instance.plot([q1, q2], backend='pyplot', limits=[-20, 20, -20, 20, -20, 20])
    
    return q1, q2, d

def Tercero(x, y, i, d):

    R = []
    R.append(RevoluteDH(d=0, alpha=0, a=l1, offset=0))
    R.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))
    robot_instance = DHRobot(R, name='Bender')
    
    Px = x/2.5-7
    Py = y/2.5+6

    b = math.sqrt(Px**2+Py**2)
    # Theta 2
    cos_theta2 = (b**2-l2**2-l1**2)/(2*l1*l2)
    sen_theta2 = math.sqrt(1-(cos_theta2)**2)#(+)codo abajo y (-)codo arriba
    theta2 = math.atan2(sen_theta2, cos_theta2)
        
    # Theta 1
    alpha = math.atan2(Py,Px)
    phi = math.atan2(l2*sen_theta2, l1+l2*cos_theta2)
    theta1 = alpha - phi

    if theta1 <= -numpy.pi:
        theta1 = (2*numpy.pi)+theta1 

    q1 = theta1
    q2 = theta2

    if q2 <= -numpy.pi:
        q2 = (2*numpy.pi)+q2

    MTH = robot_instance.fkine([q1,q2])
    d[:, i] =  MTH.t

    # robot_instance.plot([q1, q2], backend='pyplot', limits=[-20, 20, -20, 20, -20, 20])

    return q1, q2, d

def Cuarto(x, y, i, d, seleccion):

    R = []
    R.append(RevoluteDH(d=0, alpha=0, a=l1, offset=0))
    R.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))
    robot_instance = DHRobot(R, name='Bender')

    # Cinemática inversa
    if seleccion == "Puma":
        Px = x/110-5
        Py = y/110+4
    elif seleccion == "Toyota":
        Px = x/100-2
        Py = y/100+4
    elif seleccion == "Apple":
        Px = x/110-2
        Py = y/110+4
    elif seleccion == "Pepsi":
        Px = x/120-4
        Py = y/110+4

    b = math.sqrt(Px**2+Py**2)
    # Theta 2
    cos_theta2 = (b**2-l2**2-l1**2)/(2*l1*l2)
    sen_theta2 = math.sqrt(1-(cos_theta2)**2)#(+)codo abajo y (-)codo arriba
    theta2 = math.atan2(sen_theta2, cos_theta2)
        
    # Theta 1
    alpha = math.atan2(Py,Px)
    phi = math.atan2(l2*sen_theta2, l1+l2*cos_theta2)
    theta1 = alpha - phi
        
    if theta1 <= -numpy.pi:
        theta1 = (2*numpy.pi)+theta1 

    q1 = theta1
    q2 = theta2

    if q2 <= -numpy.pi:
        q2 = (2*numpy.pi)+q2

    MTH = robot_instance.fkine([q1,q2])
    d[:, i] =  MTH.t

    #robot_instance.plot([q1, q2], backend='pyplot', limits=[-20, 20, -20, 20, -20, 20])

    return q1, q2, d
