from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer 
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from time import sleep
import sys
from Robot import *
from MoverServo import *
from Letras import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(769, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(220, 40, 104, 25))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(220, 70, 104, 25))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 40, 21, 25))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 70, 21, 25))
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QWidget(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(100, 100, 551, 371))
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(396, 40, 101, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(396, 70, 101, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(510, 70, 67, 17))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(510, 40, 67, 17))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 510, 160, 25))
        self.label_8.setObjectName("label_4")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 540, 167, 25))
        self.label_9.setObjectName("label_5")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 570, 167, 25))
        self.label_10.setObjectName("label_6")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(500, 510, 221, 151))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("/home/santana19/Documentos/AlgoritmosRobotica/Imagenes/images.png"))
        self.label_13.setObjectName("label_11")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 118, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(290, 550, 191, 25))
        self.comboBox_2.setObjectName("comboBox_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        QTimer.singleShot(100, self.puntoUno)

        self.fig = Figure()
        self.fig1 = self.fig.add_subplot(projection='3d')
        self.fig1.set_xlabel('X')
        self.fig1.set_ylabel('Y')
        self.fig1.set_zlabel('Z')
        self.fig1.set_xlim(-20, 20)
        self.fig1.set_ylim(-20, 20)
        self.fig1.set_zlim(-20, 20)

        self.canvas = FigureCanvas(self.fig)
        layout = QtWidgets.QVBoxLayout(self.label_7)
        layout.addWidget(self.canvas)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Punto 1"))
        self.label.setText(_translate("MainWindow", "X"))
        self.label_2.setText(_translate("MainWindow", "Y"))
        self.label_3.setText(_translate("MainWindow", "Articulación 1"))
        self.label_4.setText(_translate("MainWindow", "Articulación 2"))
        self.label_8.setText(_translate("MainWindow", "Juan Sebastian Torres"))
        self.label_9.setText(_translate("MainWindow", "Reynaldo Alonso Alape"))
        self.label_10.setText(_translate("MainWindow", "Fabian Camilo Vasquez"))
        self.pushButton.setText(_translate("MainWindow", "Punto 2"))
        self.comboBox_2.addItem("Selecciona un nombre")
        self.comboBox_2.addItem("ALONSO")
        self.comboBox_2.addItem("JUAN")
        self.comboBox_2.addItem("FABIAN")

        self.pushButton.clicked.connect(self.puntoDos)

        self.textEdit.textChanged.connect(self.puntoUno)
        self.textEdit_2.textChanged.connect(self.puntoUno)

        self.comboBox_2.currentTextChanged.connect(self.puntoTres)

    def puntoUno(self):

        x = self.textEdit.toPlainText()
        y = self.textEdit_2.toPlainText()
        
        if x == '' or y == '' or x == '-' or y == '-' :
            x = 13
            y = 0
            
        Px = int(x)
        Py = int(y)

        q1, q2 = Robot(x, y)

        self.label_6.setText(str(numpy.rad2deg(q1)))
        self.label_5.setText(str(numpy.rad2deg(q2)))

        MoverServo(q1, q2)
        self.plot_path(Px, Py, None, None, False)

    def puntoDos(self):

        for i in range(0, 181, 20):
            q1, q2, d = Bender(0,i)
            MoverServo(q1, q2)
            self.plot_path(None, None, d, i, False)
            sleep(0.05)

        for i in range(160, -1, -20):
            q1, q2, d = Bender(0,i)
            MoverServo(q1, q2)
            sleep(0.05)

        for i in range(0, 181, 20):
            q1, q2, d = Bender(i,0)
            MoverServo(q1, q2)
            self.plot_path(None, None, d, i, False)
            sleep(0.05)

        for i in range(0, 181, 20):
            q1, q2, d = Bender(180,i)
            MoverServo(q1, q2)
            self.plot_path(None, None, d, i, False)
            sleep(0.05)

    def puntoTres(self, palabra):
        nombre = palabra

        coordenadas_x, coordenadas_y = Letras(palabra)
        d = numpy.zeros((3, len(coordenadas_x)))

        for i in range(len(coordenadas_x)):
            x, y = coordenadas_x[i], coordenadas_y[i]
            q1, q2, d = Tercero(x, y, i, d)
            MoverServo(q1, q2)
            self.plot_path(None, None, d, i, True)

    def plot_path(self, x, y, d, i, line):
        if (x is None) and (y is None) and (line == False):
            self.fig1.plot(d[0,i],d[1,i],d[2,i],'.b')
        
        elif line == True:
            self.fig1.plot([d[0, i-1], d[0, i]], [d[1, i-1], d[1, i]], [d[2, i-1], d[2, i]], color='blue')

        else:
            self.fig1.plot(x, y, 0, '.b')

        self.canvas.draw()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())