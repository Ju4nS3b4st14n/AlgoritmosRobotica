from roboticstoolbox import *
from spatialmath.base import *
import math
import numpy
from sympy import *

l1 = 10
l2 = 10
l3 = 10
l0 = 10

# Cinemática inversa
Px = 0
Py = 20
Pz = 20
beta = numpy.deg2rad(90)

e = Px - l3*round(cos(beta))
c = Py - l3*round(sin(beta))
# Theta 0
theta0 = float(atan2(Py,Px))
print(f'theta 0 = {numpy.rad2deg(theta0):.4f}')

# Theta 2
b = round(sqrt(e**2+c**2))
cos_theta2 = (b**2-l2**2-l1**2)/(2*l1*l2)
sen_theta2 = math.sqrt(1-(cos_theta2)**2)
theta2 = float(atan2(sen_theta2, cos_theta2))
print(f'theta 2 = {numpy.rad2deg(theta2):.4f}')
# Theta 1
alpha = math.atan2(c,e)
phi = math.atan2(l2*sen_theta2, l1+l2*cos_theta2)
theta1 = alpha - phi
if theta1 <= -numpy.pi:
    theta1 = (2*numpy.pi)+theta1

print(f'theta 1 = {numpy.rad2deg(theta1):.4f}')
#Theta 3
theta3 = beta - theta1 - theta2
print(f'theta 3 = {numpy.rad2deg(theta3):.4f}')
#-------------

q0 = theta0
q1 = theta1
q2 = theta2
q3 = theta3

R = []
R.append(RevoluteDH(d=l1, alpha=numpy.pi/2, a=0, offset=0))
R.append(RevoluteDH(d=0, alpha=0, a=l1, offset=0))
R.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))
R.append(RevoluteDH(d=0, alpha=0, a=l3, offset=0))

Robot = DHRobot(R, name='Bender')
print(Robot)

Robot.teach([q0, q1, q2, q3], 'rpy/zyx', limits=[-30,30,-30,30,-30,30])

#zlim([-15,30]);

MTH = Robot.fkine([q1,q2,q3])
print(MTH)
print(f"Roll, Pitch, Yaw = {tr2rpy(MTH.R, 'deg', 'zyx')}")