import RPi.GPIO as GPIO
from PyQt5 import QtCore, QtGui, QtWidgets
from adafruit_pca9685 import PCA9685
from adafruit_servokit import ServoKit 
import board
import busio
import sys
from time import sleep

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(250, 210, 311, 16))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setRange(0, 180)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(390, 150, 51, 25))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 110, 331, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(590, 205, 101, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(96, 205, 121, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 510, 160, 25))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 450, 160, 25))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 480, 160, 25))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(500, 380, 221, 151))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../Imagenes/images.png"))
        self.label_7.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.i2c=busio.I2C(board.SCL,board.SDA)
        self.pca=PCA9685(self.i2c)
        self.pca.frequency=60
        self.textEdit.textChanged.connect(self.move_motor)
        self.horizontalSlider.valueChanged.connect(self.update_angle)

        self.selected_motor = None

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Ingresa el número del servomotor a seleccionar"))
        self.label_2.setText(_translate("MainWindow", "Grados: 0 °"))
        self.label_3.setText(_translate("MainWindow", "Servomotor: "))
        self.label_4.setText(_translate("MainWindow", "Juan Sebastian Torres"))
        self.label_5.setText(_translate("MainWindow", "Fabian Camilo Vasquez"))
        self.label_6.setText(_translate("MainWindow", "Alonso Mancipe"))
        
    def update_angle(self):
        valor = str(self.horizontalSlider.value())
        self.label_2.setText("Grados: {} °".format(valor))  # Ajuste: Actualizar el texto del label con el valor del slider
        angle = int(valor)
        if self.selected_motor:
            self.move_servo(self.selected_motor, angle)

    def move_motor(self):
        
        motor_id = self.textEdit.toPlainText()
        
        if motor_id not in ["1", "2"]:
            self.selected_motor = None
            return
        if motor_id == "1":
            self.selected_motor = 8

        elif motor_id == "2":
            self.selected_motor = 14
        
        angle = self.horizontalSlider.value()
        self.move_servo(self.selected_motor, angle)
            
    def move_servo(self, servo_pin, angle, servo_max=1970,servo_min=980):
    
        if servo_pin is None:
            return
        
        if angle == 0:
            angle = 2

        if angle == 180:
            angle = 178

        pulse_width=int((angle/22)*(servo_max-servo_min)+servo_min) #28 para servomotor pequeño
        self.pca.channels[servo_pin].duty_cycle=pulse_width

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())