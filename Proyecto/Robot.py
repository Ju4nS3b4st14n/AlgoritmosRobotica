#------------------------------- Peter Corke ----------------------------------
from roboticstoolbox import *
from spatialmath.base import *
import matplotlib.pyplot as plt
import numpy
from sympy import *
from time import sleep

l1 = 12
l2 = 10
l3 = 10
l4 = 10

def manualRobot(q1, q2, q3, q4):

    q = [q1,q2,q3,q4]

    R = []
    R.append(RevoluteDH(d=l1, alpha=numpy.pi/2, a=0, offset=0))
    R.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))
    R.append(RevoluteDH(d=0, alpha=0, a=l3, offset=0))
    R.append(RevoluteDH(d=0, alpha=0, a=l4, offset=0))

    Robot = DHRobot(R, name='Bender')
    print(Robot)

    Robot.plot([q1, q2, q3, q4], backend='pyplot', limits=[-40,40,-40,40,-40,40])

    sleep(0.5)
    return

    #zlim([-15,30]);

    #MTH = Robot.fkine(q)
    #print(MTH)
    #print(f"Roll, Pitch, Yaw = {tr2rpy(MTH.R, 'deg', 'zyx')}")
    #theta = Robot.ikine_6s(MTH,'llllll',)
    #print(f'theta1, theta2, theta3, theta4, theta5, theta6 = {theta}')

def semi():

    # Función objetivo: calcular la distancia entre la posición obtenida y la deseada
    def objetivo(q):
        q1, q2, q3, q4 = q
        R = [
            RevoluteDH(d=l1, alpha=np.pi/2, a=0, offset=0),
            RevoluteDH(d=0, alpha=0, a=l2, offset=0),
            RevoluteDH(d=0, alpha=0, a=l3, offset=0),
            RevoluteDH(d=0, alpha=0, a=l4, offset=0)
        ]
        robot = DHRobot(R, name='Bender')
        MTH = robot.fkine([q1, q2, q3, q4])  # Cálculo de la cinemática directa
        pos_obtenida = MTH.t  # Solo la parte de la traslación
        # Error cuadrático entre la posición obtenida y la deseada
        error = np.sum((pos_obtenida - np.array([Px, Py, Pz]))**2)
        return error

    # Estimación inicial de los ángulos
    theta1_init = np.deg2rad(45)
    theta2_init = np.deg2rad(30)
    theta3_init = np.deg2rad(45)
    theta4_init = np.deg2rad(30)  # Ángulo fijo inicial de 30 grados

    # Usamos minimize para ajustar los ángulos
    result = minimize(objetivo, [theta1_init, theta2_init, theta3_init, theta4_init], bounds=[(-np.pi, np.pi), (-np.pi, np.pi), (-np.pi, np.pi), (-np.pi, np.pi)])

    # Resultados de la optimización
    q_opt = result.x
    print(f"Ángulos óptimos: theta1 = {np.rad2deg(q_opt[0]):.4f}, theta2 = {np.rad2deg(q_opt[1]):.4f}, theta3 = {np.rad2deg(q_opt[2]):.4f}, theta4 = {np.rad2deg(q_opt[3]):.4f}")

    # Verificación de la posición final
    R = [
        RevoluteDH(d=l1, alpha=np.pi/2, a=0, offset=0),
        RevoluteDH(d=0, alpha=0, a=l2, offset=0),
        RevoluteDH(d=0, alpha=0, a=l3, offset=0),
        RevoluteDH(d=0, alpha=0, a=l4, offset=0)
    ]
    robot = DHRobot(R, name='Bender')
    MTH_opt = robot.fkine(q_opt)  # Cálculo de la cinemática directa con los ángulos optimizados
    pos_opt = MTH_opt.t
    print(f"Posición final obtenida: {pos_opt}")
    print(f"Posición deseada: {[Px, Py, Pz]}")

    # Visualización interactiva
    robot.teach(q_opt, 'rpy/zyx', limits=[-30, 30, -30, 30, -30, 30])

    # También podemos usar plt.show() para asegurarnos de que se muestre la ventana de matplotlib
    plt.show()

def auto(q1, q2, q3, q4):

    q = [q1,q2,q3,q4]

    R = []
    R.append(RevoluteDH(d=l1, alpha=numpy.pi/2, a=0, offset=0))
    R.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))
    R.append(RevoluteDH(d=0, alpha=0, a=l3, offset=-1))
    R.append(RevoluteDH(d=0, alpha=0, a=l4, offset=-1))

    Robot = DHRobot(R, name='Bender')

    # Robot.plot([q1, q2, q3, q4], backend='pyplot', limits=[-40,40,-40,40,-40,40])

    sleep(0.5)