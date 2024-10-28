#------------------------------- Peter Corke ----------------------------------
from roboticstoolbox import *
from spatialmath.base import *
import numpy
from sympy import *

l1 = 12
l2 = 10
l3 = 10
l4 = 10

q1 = 0
q2 = 0
q3 = 0
q4 = 0

q = [q1,q2,q3,q4]

R = []
R.append(RevoluteDH(d=l1, alpha=numpy.pi/2, a=0, offset=0))
R.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))
R.append(RevoluteDH(d=0, alpha=0, a=l3, offset=0))
R.append(RevoluteDH(d=0, alpha=0, a=l4, offset=0))

Robot = DHRobot(R, name='Bender')
print(Robot)

Robot.teach(q, 'rpy/zyx', limits=[-50,50,-50,50,-50,50])

#zlim([-15,30]);

MTH = Robot.fkine(q)
print(MTH)
print(f"Roll, Pitch, Yaw = {tr2rpy(MTH.R, 'deg', 'zyx')}")
#theta = Robot.ikine_6s(MTH,'llllll',)
#print(f'theta1, theta2, theta3, theta4, theta5, theta6 = {theta}')