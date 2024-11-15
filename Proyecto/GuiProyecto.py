from PyQt5 import QtCore, QtGui, QtWidgets
import time   
import sys
import matplotlib
matplotlib.use('Qt5Agg')
import math
import numpy
from sympy import *
from InverseKinematics3R import *
from ForwardKinematics3R import *
from MoverServo import *
import matplotlib.pyplot as plt
from Robot import *
from Camera import *
from ImageCamera import figure
from Sensors import *


class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(800, 600)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.horizontalSlider_motor1 = QtWidgets.QSlider(self.centralwidget)
                self.horizontalSlider_motor1.setGeometry(QtCore.QRect(100, 80, 201, 20))
                self.horizontalSlider_motor1.setOrientation(QtCore.Qt.Horizontal)
                self.horizontalSlider_motor1.setObjectName("horizontalSlider_motor1")
                self.horizontalSlider_motor1.setRange(1, 179)
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(10, 80, 75, 18))
                self.label.setObjectName("label")
                self.horizontalSlider_motor2 = QtWidgets.QSlider(self.centralwidget)
                self.horizontalSlider_motor2.setGeometry(QtCore.QRect(100, 110, 201, 20))
                self.horizontalSlider_motor2.setOrientation(QtCore.Qt.Horizontal)
                self.horizontalSlider_motor2.setObjectName("horizontalSlider_motor2")
                self.horizontalSlider_motor2.setRange(1, 179)
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(10, 110, 75, 18))
                self.label_2.setObjectName("label_2")
                self.horizontalSlider_motor3 = QtWidgets.QSlider(self.centralwidget)
                self.horizontalSlider_motor3.setGeometry(QtCore.QRect(100, 140, 201, 20))
                self.horizontalSlider_motor3.setOrientation(QtCore.Qt.Horizontal)
                self.horizontalSlider_motor3.setObjectName("horizontalSlider_motor3")
                self.horizontalSlider_motor3.setRange(1, 179)
                initial_value = int((180 - 0) / 2)  # Valor inicial en la mitad
                self.horizontalSlider_motor3.setValue(initial_value)
                self.label_3 = QtWidgets.QLabel(self.centralwidget)
                self.label_3.setGeometry(QtCore.QRect(10, 140, 75, 18))
                self.label_3.setObjectName("label_3")
                self.horizontalSlider_motor4 = QtWidgets.QSlider(self.centralwidget)
                self.horizontalSlider_motor4.setGeometry(QtCore.QRect(100, 170, 201, 20))
                self.horizontalSlider_motor4.setOrientation(QtCore.Qt.Horizontal)
                self.horizontalSlider_motor4.setObjectName("horizontalSlider_motor4")
                self.horizontalSlider_motor4.setRange(1, 179)
                self.horizontalSlider_motor4.setValue(initial_value)
                self.label_17 = QtWidgets.QLabel(self.centralwidget)
                self.label_17.setGeometry(QtCore.QRect(10, 170, 75, 18))
                self.label_17.setObjectName("label_17")
                self.label_4 = QtWidgets.QLabel(self.centralwidget)
                self.label_4.setGeometry(QtCore.QRect(150, 10, 291, 20))
                self.label_4.setObjectName("label_4")
                self.label_5 = QtWidgets.QLabel(self.centralwidget)
                self.label_5.setGeometry(QtCore.QRect(160, 200, 58, 18))
                self.label_5.setObjectName("label_5")
                self.pushButton_pick = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_pick.setGeometry(QtCore.QRect(40, 230, 88, 34))
                self.pushButton_pick.setObjectName("pushButton_pick")
                self.pushButton_PLACE = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_PLACE.setGeometry(QtCore.QRect(230, 230, 88, 34))
                self.pushButton_PLACE.setObjectName("pushButton_PLACE")
                self.label_6 = QtWidgets.QLabel(self.centralwidget)
                self.label_6.setGeometry(QtCore.QRect(120, 50, 131, 18))
                self.label_6.setObjectName("label_6")
                self.label_7 = QtWidgets.QLabel(self.centralwidget)
                self.label_7.setGeometry(QtCore.QRect(420, 50, 211, 20))
                self.label_7.setObjectName("label_7")
                self.pos_x = QtWidgets.QLineEdit(self.centralwidget)
                self.pos_x.setGeometry(QtCore.QRect(470, 80, 121, 31))
                self.pos_x.setObjectName("pos_x")
                self.label_8 = QtWidgets.QLabel(self.centralwidget)
                self.label_8.setGeometry(QtCore.QRect(420, 90, 58, 18))
                self.label_8.setObjectName("label_8")
                self.label_9 = QtWidgets.QLabel(self.centralwidget)
                self.label_9.setGeometry(QtCore.QRect(420, 130, 58, 18))
                self.label_9.setObjectName("label_9")
                self.pos_y = QtWidgets.QLineEdit(self.centralwidget)
                self.pos_y.setGeometry(QtCore.QRect(470, 120, 121, 31))
                self.pos_y.setObjectName("pos_y")
                self.label_10 = QtWidgets.QLabel(self.centralwidget)
                self.label_10.setGeometry(QtCore.QRect(420, 170, 58, 18))
                self.label_10.setObjectName("label_10")
                self.pos_z = QtWidgets.QLineEdit(self.centralwidget)
                self.pos_z.setGeometry(QtCore.QRect(470, 160, 121, 31))
                self.pos_z.setObjectName("pos_z")
                self.pushButton_go = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_go.setGeometry(QtCore.QRect(480, 210, 88, 34))
                self.pushButton_go.setObjectName("pushButton_go")
                self.label_11 = QtWidgets.QLabel(self.centralwidget)
                self.label_11.setGeometry(QtCore.QRect(120, 310, 161, 18))
                self.label_11.setObjectName("label_11")
                self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_start.setGeometry(QtCore.QRect(150, 350, 88, 34))
                self.pushButton_start.setObjectName("pushButton_start")
                self.label_12 = QtWidgets.QLabel(self.centralwidget)
                self.label_12.setGeometry(QtCore.QRect(270, 400, 200, 200))
                self.label_12.setText("")
                self.label_12.setPixmap(QtGui.QPixmap("/home/santana19/Documentos/AlgoritmosRobotica/Imagenes/images.png"))
                self.label_12.setObjectName("label_12")
                self.label_13 = QtWidgets.QLabel(self.centralwidget)
                self.label_13.setGeometry(QtCore.QRect(10, 460, 241, 31))
                self.label_13.setObjectName("label_13")
                self.label_14 = QtWidgets.QLabel(self.centralwidget)
                self.label_14.setGeometry(QtCore.QRect(10, 490, 181, 18))
                self.label_14.setObjectName("label_14")
                self.label_15 = QtWidgets.QLabel(self.centralwidget)
                self.label_15.setGeometry(QtCore.QRect(10, 520, 191, 18))
                self.label_15.setObjectName("label_15")
                self.label_16 = QtWidgets.QLabel(self.centralwidget)
                self.label_16.setGeometry(QtCore.QRect(10, 550, 121, 20))
                self.label_16.setObjectName("label_16")
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)
        
                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
                self.horizontalSlider_motor1.valueChanged.connect(self.manual)
                self.horizontalSlider_motor2.valueChanged.connect(self.manual)
                self.horizontalSlider_motor3.valueChanged.connect(self.manual)
                self.horizontalSlider_motor4.valueChanged.connect(self.manual)
                self.pushButton_go.clicked.connect(self.semi_auto)
                self.pushButton_start.clicked.connect(self.automatic)
                self.pushButton_pick.clicked.connect(self.open)
                self.pushButton_PLACE.clicked.connect(self.close)
                
        
       
        def manual(self):
    
                theta1=self.horizontalSlider_motor1.value()
                theta2=self.horizontalSlider_motor2.value()
                theta3=self.horizontalSlider_motor3.value()
                theta4=self.horizontalSlider_motor4.value()
                q1 = int(numpy.deg2rad(theta1))
                #q1 = theta1
                q2 = int(numpy.deg2rad(theta2))
                #q2 = theta2
                q3 = int(numpy.deg2rad(theta3))
                #q3 = theta3
                #q4 = theta4
                q4 = int(numpy.deg2rad(theta4))

                Sensor1, sensor2 = sensor()

                if Sensor1 == 0 or sensor2 == 0:
                        return
                else:
                        MoverServo(theta1, theta2, theta3, theta4)

                        
                #print(f"q1 {theta1}, q2 {theta2}, q3 {q3}, q4 {q4}")
                #manualRobot(q1, q2, q3, q4)
       
        def semi_auto(self):
                l1 = 4
                l2 = 8
                l3 = 18
                
                x = self.pos_x.text()
                y = self.pos_y.text()
                z = self.pos_z.text()
                
                # Cinemática inversa
                Px = int(x)
                Py = int(y)
                Pz = int(z)

                e = sqrt(Px*2+Py*2)
                c = Pz - l1
                b = sqrt(e*2+c*2)
                
                e = sqrt(Px**2+Py**2)
                c = Pz - l1
                b = sqrt(e**2+c**2)
                # Theta 1
                theta1 = float(atan2(Py,Px))
                print(f'theta 1 = {numpy.rad2deg(theta1):.4f}')
                # Theta 3
                cos_theta3 = (b**2-l2**2-l3**2)/(2*l2*l3)
                sen_theta3 = sqrt(1-(cos_theta3)**2)
                theta3 = float(atan2(sen_theta3, cos_theta3))
                print(f'theta 3 = {numpy.rad2deg(theta3):.4f}')
                # Theta 2
                alpha = math.atan2(c,e)
                phi = math.atan2(l3*sen_theta3, l2+l3*cos_theta3)
                theta2 = float(alpha - phi)
                if theta2 <= -numpy.pi:
                    theta2 = (2*numpy.pi)+theta2

                print(f'theta 2 = {numpy.rad2deg(theta2):.4f}')
                #-------------

                q1 = theta1
                q2 = theta2
                q3 = theta3
                q4 = theta4

                if numpy.isnan(q1) or numpy.isnan(q2) or numpy.isnan(q3):
                        q1 = 0
                        q2 = 0
                        q3 = 0
                # self.mover_servo(q1,q2,q3,q4)

        def automatic(self):

                image = photo()
                show_image(image)
                color = figure()
                show_image(image)

                MoverServoAuto("B")
                print(color)

                if color == "green":
                        print("punto C")
                        MoverServoAuto("C")
                elif color == "red":
                        print("Punto A")
                        MoverServoAuto("A")
                else:
                        print("Color diferente al rojo o verde")        


        def open(self):

                q = int(numpy.deg2rad(90))

                gripperopen(q)

        def close(self):

                q = int(numpy.deg2rad(0))

                gripperclose(q)
        
        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#00aa00;\">MOTOR-1</span></p></body></html>"))
                self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#00aa00;\">MOTOR-2</span></p></body></html>"))
                self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#00aa00;\">MOTOR-3</span></p></body></html>"))
                self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#00aa00;\">MOTOR-4</span></p></body></html>"))
                self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#aa0000;\">CELDA ROBOTIZADA-ROBOT DE 3DOF</span></p></body></html>"))
                self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#00aa00;\">Gripper</span></p></body></html>"))
                self.pushButton_pick.setText(_translate("MainWindow", "PICK"))
                self.pushButton_PLACE.setText(_translate("MainWindow", "PLACE"))
                self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#00aa00;\">MODO: MANUAL</span></p></body></html>"))
                self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#00aaff;\">MODO: SEMI-AUTOMATICO</span></p></body></html>"))
                self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#00aaff;\">POS X:</span></p></body></html>"))
                self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#00aaff;\">POS Y:</span></p></body></html>"))
                self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#00aaff;\">POS Z:</span></p></body></html>"))
                self.pushButton_go.setText(_translate("MainWindow", "GO!"))
                self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#aa557f;\">MODO:AUTOMATICO</span></p></body></html>"))
                self.pushButton_start.setText(_translate("MainWindow", "¡START!"))
                self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Juan Sebastian Torres</span></p></body></html>"))
                self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Fabian Camilo Vasquez</span></p></body></html>"))
                self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Reynaldo Alonso Alape</span></p></body></html>"))
        
       



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
