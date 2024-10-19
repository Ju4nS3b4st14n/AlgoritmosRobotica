from PyQt5 import QtCore, QtGui, QtWidgets
from gpiozero import *
from mpu6050 import mpu6050
import time
from time import sleep


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 60, 301, 17))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(330, 110, 113, 25))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 160, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 220, 131, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 270, 150, 17))
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
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(320, 290, 150, 17))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(320, 310, 150, 17))
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.tiempo)

        self.sensor = mpu6050(0x68)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Tiempo de muestra del sensor en segundos"))
        self.pushButton.setText(_translate("MainWindow", "Iniciar"))
        self.label_2.setText(_translate("MainWindow", "Lectura del sensor"))
        self.label_3.setText(_translate("MainWindow", "Celerometro en X"))
        self.label_8.setText(_translate("MainWindow", "Celerometro en Y"))
        self.label_9.setText(_translate("MainWindow", "Celerometro en Z"))
        self.label_4.setText(_translate("MainWindow", "Juan Sebastian Torres"))
        self.label_5.setText(_translate("MainWindow", "Fabian Camilo Vasquez"))
        self.label_6.setText(_translate("MainWindow", "Reynaldo Alonso Alape"))

    def tiempo(self):

        t = self.textEdit.toPlainText()
        t1 = time.time()
        t2 = 0.0
        while t2 <= float(t):
            accel_data = self.sensor.get_accel_data()
            gyro_data = self.sensor.get_gyro_data()

            # Imprimir datos en la consola
            #print("ax:", accel_data['x'], "ay:", accel_data['y'], "az:", accel_data['z'])
            #print("gx:", gyro_data['x'], "gy:", gyro_data['y'], "gz:", gyro_data['z'])

            # Esperar medio segundo antes de la siguiente lectura
            #sleep(0.3)
            
            #distancia = self.sensor.distance
            self.label_3.setText("ax: {:.2f}".format(accel_data['x']))
            self.label_8.setText("ay: {:.2f}".format(accel_data['y']))
            self.label_9.setText("az: {:.2f}".format(accel_data['z']))
            #self.label_3.setText("Distancia {:.2f} metros".format(distancia))
            QtWidgets.QApplication.processEvents()
            t2 = time.time() - t1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


