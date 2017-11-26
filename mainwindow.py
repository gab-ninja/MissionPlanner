#
# MISSION PLANNER
#
# This is a software that helps user to determine orbits and oyher orbital mechanics parameters
#
# Programmed by Mario Gabriel Campos
#
# Interface created by: PyQt5 UI code generator 5.6 (pyuic5)
#

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from functions import *
from functools import partial
from math import *
import sys
import numpy as np
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1181, 522)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("MDS-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(90, 150, 261, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(50, 60, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setMaxVisibleItems(12)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.currentIndexChanged.connect(self.on_combobox_changed, self.comboBox.currentIndex())
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(390, 150, 361, 211))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 60, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(50, 60, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.bt_circulares_clicked)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 160, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 1091, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        # ------------------------------------ IMAGEM --------------------------
        self.label100 = QtWidgets.QLabel(self.centralwidget)
        self.label100.setGeometry(QtCore.QRect(150, 250, 321, 261))
        self.label100.setObjectName('label_100')
        self.pixmap100 = QPixmap('Earth-small.png')
        self.label100.setPixmap(self.pixmap100)

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(790, 150, 311, 261))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 160, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 60, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_8.setGeometry(QtCore.QRect(50, 210, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_9.setGeometry(QtCore.QRect(50, 110, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.label.raise_()
        self.groupBox_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1181, 26))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mission Design Software"))
        self.groupBox.setTitle(_translate("MainWindow", "Central Body"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Earth"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Moon"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Sun"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Mercury"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Venus"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Mars"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Jupiter"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Saturn"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Uranus"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Neptune"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Pluto"))
        self.comboBox.setItemText(11, _translate("MainWindow", "Other"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Orbit Definition"))
        self.pushButton_4.setText(_translate("MainWindow", "Hyperbolic"))
        self.pushButton.setText(_translate("MainWindow", "Circular"))
        self.pushButton_3.setText(_translate("MainWindow", "Parabolic"))
        self.pushButton_2.setText(_translate("MainWindow", "Elliptical"))
        self.pushButton_5.setText(_translate("MainWindow", "Type Unknown"))
        self.label.setText(_translate("MainWindow", "Mission Design Software"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Utilities"))
        self.pushButton_6.setText(_translate("MainWindow", "Julian Dates"))
        self.pushButton_7.setText(_translate("MainWindow", "Ephemeris"))
        self.pushButton_8.setText(_translate("MainWindow", "Propellant Mass"))
        self.pushButton_9.setText(_translate("MainWindow", "Plane Changes"))

    def on_combobox_changed(self):
        value = self.comboBox.currentIndex()
        self.label100.setGeometry(QtCore.QRect(150, 250, 321, 261))
        if value == 0:
            self.pixmap100 = QPixmap('Earth-small.png')
        elif value == 1:
            self.pixmap100 = QPixmap('Moon-small.png')
        elif value == 2:
            self.pixmap100 = QPixmap('Sun-small.png')
        elif value == 3:
            self.pixmap100 = QPixmap('Mercury-small.png')
        elif value == 4:
            self.pixmap100 = QPixmap('Venus-small.png')
        elif value == 5:
            self.pixmap100 = QPixmap('Mars-small.png')
        elif value == 6:
            self.pixmap100 = QPixmap('Jupiter-small.png')
        elif value == 7:
            self.pixmap100 = QPixmap('Saturn-small.png')
            self.label100.setGeometry(QtCore.QRect(62, 250, 321, 261))
        elif value == 8:
            self.pixmap100 = QPixmap('Uranus-small.png')
        elif value == 9:
            self.pixmap100 = QPixmap('Neptune-small.png')
        elif value == 10:
            self.pixmap100 = QPixmap('Pluto-small.png')
        elif value == 11:
            self.pixmap100 = QPixmap('MDS-logo-small.png')
        self.label100.setPixmap(self.pixmap100)

    def bt_circulares_clicked(self):
        CircularWindow.show()

class Ui_CircularWindow(object):
    def __init__(self):
        self.periodo = 0  # periodo em segundos
        self.periodo_unit = 0 # tipo 0 que é segundos
        self.altitude = 0
        self.raio = 0
        self.velocidade = 0
        self.exists_graph = 0

    def setupUi(self, CircularWindow):
        CircularWindow.setObjectName("CircularWindow")
        CircularWindow.resize(1172, 534)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("MDS-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CircularWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(CircularWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(80, 90, 371, 241))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 50, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 170, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(250, 50, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(110, 50, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 90, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 130, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 170, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(250, 90, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(250, 170, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(250, 130, 73, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.currentIndexChanged.connect(self.on_combobox_changed, self.comboBox.currentIndex())
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(40, 210, 271, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 410, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.bt_calculate)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 410, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.bt_exit)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(600, 40, 491, 401))
        self.graphicsView.setObjectName("graphicsView")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 30, 551, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(350, 370, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(70, 370, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.bt_clear)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(210, 370, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        CircularWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CircularWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1172, 26))
        self.menubar.setObjectName("menubar")
        CircularWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CircularWindow)
        self.statusbar.setObjectName("statusbar")
        CircularWindow.setStatusBar(self.statusbar)
        #------------Gráfico-------------------------------------------
        self.cw = pg.GraphicsLayoutWidget(self.centralwidget)
        self.cw.setObjectName("graph")
        self.cw.setGeometry(QtCore.QRect(550, 40, 575, 450))

        self.retranslateUi(CircularWindow)
        QtCore.QMetaObject.connectSlotsByName(CircularWindow)

    def retranslateUi(self, CircularWindow):
        _translate = QtCore.QCoreApplication.translate
        CircularWindow.setWindowTitle(_translate("CircularWindow", "Circular Orbit"))
        self.groupBox.setTitle(_translate("CircularWindow", "Input any Element"))
        self.label.setText(_translate("CircularWindow", "Altitude:"))
        self.label_2.setText(_translate("CircularWindow", "Radius:"))
        self.label_3.setText(_translate("CircularWindow", "Period:"))
        self.label_4.setText(_translate("CircularWindow", "Velocity:"))
        self.label_5.setText(_translate("CircularWindow", "[Km]"))
        self.label_6.setText(_translate("CircularWindow", "[Km]"))
        self.label_8.setText(_translate("CircularWindow", "[Km/s]"))
        self.comboBox.setItemText(0, _translate("CircularWindow", "[s]"))
        self.comboBox.setItemText(1, _translate("CircularWindow", "[h]"))
        self.comboBox.setItemText(2, _translate("CircularWindow", "[days]"))
        self.label_7.setText(_translate("CircularWindow", "Given element is underlined"))
        self.pushButton_3.setText(_translate("CircularWindow", "Calculate"))
        self.pushButton_5.setText(_translate("CircularWindow", "Exit"))
        self.label_9.setText(_translate("CircularWindow", "Circular Earth Orbit"))
        self.pushButton_6.setText(_translate("CircularWindow", "Export Data"))
        self.pushButton_7.setText(_translate("CircularWindow", "Clear"))
        self.pushButton_8.setText(_translate("CircularWindow", "Graph Settings"))

    def bt_clear(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.periodo = 0
        self.raio = 0
        self.velocidade = 0
        self.altitude = 0
        if self.exists_graph:
            self.p2 = self.cw.removeItem(self.p2)
            self.exists_graph = 0

    def bt_exit(self):
        CircularWindow.close()

    def make_graph(self, radius, plamet_radius):
        if self.exists_graph:
            self.p2 = self.cw.removeItem(self.p2)

        self.p2 = self.cw.addPlot()
        a = radius
        b = radius
        limit = 1.1 * a
        x = -a * np.sin(np.linspace(0, 2 * np.pi, 1000))
        y = b * np.cos(np.linspace(0, 2 * np.pi, 1000))

        rp = plamet_radius
        e = np.sqrt(1 - (b / a) ** 2)

        xp = rp * np.sin(np.linspace(0, 2 * np.pi, 1000)) + a * e
        yp = rp * np.cos(np.linspace(0, 2 * np.pi, 1000))

        self.c = self.p2.plot(x, y)
        self.d = self.p2.plot(xp, yp)
        self.a = pg.CurveArrow(self.c)
        # b = pg.CurveArrow(d)
        self.a.setStyle(headLen=40)
        self.p2.addItem(self.a)
        self.p2.addItem(self.d)
        self.p2.setXRange(-limit, limit)
        self.p2.setYRange(-limit, limit)
        self.p2.setAspectLocked(lock=True, ratio=1)
        self.anim = self.a.makeAnimation(loop=-1)
        self.anim.start()
        self.exists_graph = 1

    def bt_calculate(self):
        p1 = ui_circ.lineEdit.text().replace(',', '.')
        planeta = ui.comboBox.currentIndex()
        if p1:
            id = 0
            try:
                p1 = float(p1)
            except Exception:
                QMessageBox.critical(CircularWindow, "Error", "The altitude value is not valid")
                return 0
                pass
            [self.altitude, self.raio, self.periodo, self.velocidade] = orbita_circular(planeta, id, p1)
            ui_circ.lineEdit_2.setText('%.6f' % self.raio)
            ui_circ.lineEdit_4.setText('%.6f' % self.velocidade)
            aux = self.periodo  # (Seconds)
            if self.comboBox.currentIndex() == 0:  # s
                ui_circ.lineEdit_3.setText('%.6f' % aux)
            elif self.comboBox.currentIndex() == 1:  # h
                aux /= 3600
                hours = int(aux)
                aux -= hours
                aux *= 60
                minutes = int(aux)
                aux -= minutes
                secunds = aux * 60
                ui_circ.lineEdit_3.setText('%dh %dm %.2fs' % (hours,  minutes, secunds))
            else:  # days
                aux /= (3600*24)
                ui_circ.lineEdit_3.setText('%.6f' % aux)
            planet = Planetas(planeta)
            self.make_graph(self.raio, planet.radius)
        else:
            p1 = ui_circ.lineEdit_2.text().replace(',', '.')
            if p1:
                id = 1
                try:
                    p1 = float(p1)
                except Exception:
                    QMessageBox.critical(CircularWindow, "Error", "The radius value is not valid")
                    return 0
                    pass
                [self.altitude, self.raio, self.periodo, self.velocidade] = orbita_circular(planeta, id, p1)
                ui_circ.lineEdit.setText('%.6f' % self.altitude)
                ui_circ.lineEdit_4.setText('%.6f' % self.velocidade)
                aux = self.periodo  # (Seconds)
                if self.comboBox.currentIndex() == 0:  # s
                    ui_circ.lineEdit_3.setText('%.6f' % aux)
                elif self.comboBox.currentIndex() == 1:  # h
                    aux /= 3600
                    hours = int(aux)
                    aux -= hours
                    aux *= 60
                    minutes = int(aux)
                    aux -= minutes
                    secunds = aux * 60
                    ui_circ.lineEdit_3.setText('%dh %dm %.2fs' % (hours, minutes, secunds))
                else:  # days
                    aux /= (3600 * 24)
                    ui_circ.lineEdit_3.setText('%.6f' % aux)
                planet = Planetas(planeta)
                self.make_graph(self.raio, planet.radius)
            else:
                p1 = ui_circ.lineEdit_3.text().replace(',', '.')
                if p1:
                    id = 2
                    try:
                        p1 = float(p1)
                    except Exception:
                        QMessageBox.critical(CircularWindow, "Error", "The period value is not valid")
                        return 0
                        pass
                    if ui_circ.comboBox.currentIndex() == 1:
                        p1 *= 3600
                    elif ui_circ.comboBox.currentIndex() == 2:
                        p1 *= (3600 * 24)
                    [self.altitude, self.raio, self.periodo, self.velocidade] = orbita_circular(planeta, id, p1)
                    ui_circ.lineEdit.setText('%.6f' % self.altitude)
                    ui_circ.lineEdit_2.setText('%.6f' % self.raio)
                    ui_circ.lineEdit_4.setText('%.6f' % self.velocidade)
                    planet = Planetas(planeta)
                    self.make_graph(self.raio, planet.radius)
                else:
                    p1 = ui_circ.lineEdit_4.text().replace(',', '.')
                    if p1:
                        id = 3
                        try:
                            p1 = float(p1)
                        except Exception:
                            QMessageBox.critical(CircularWindow, "Error", "The velocity value is not valid")
                            return 0
                            pass
                        [self.altitude, self.raio, self.periodo, self.velocidade] = orbita_circular(planeta, id, p1)
                        ui_circ.lineEdit.setText('%.6f' % self.altitude)
                        ui_circ.lineEdit_2.setText('%.6f' % self.raio)
                        aux = self.periodo  # (Seconds)
                        if self.comboBox.currentIndex() == 0:  # s
                            ui_circ.lineEdit_3.setText('%.6f' % aux)
                        elif self.comboBox.currentIndex() == 1:  # h
                            aux /= 3600
                            hours = int(aux)
                            aux -= hours
                            aux *= 60
                            minutes = int(aux)
                            aux -= minutes
                            secunds = aux * 60
                            ui_circ.lineEdit_3.setText('%dh %dm %.2fs' % (hours, minutes, secunds))
                        else:  # days
                            aux /= (3600 * 24)
                            ui_circ.lineEdit_3.setText('%.6f' % aux)
                        planet = Planetas(planeta)
                        self.make_graph(self.raio, planet.radius)
                    else:
                        QMessageBox.information(CircularWindow , "Error", "No input elements found")

    def on_combobox_changed(self):
        if  self.periodo:
            aux = self.periodo #(Seconds)
            if self.comboBox.currentIndex() == 0:  # s
                ui_circ.lineEdit_3.setText('%.6f' % aux)
            elif self.comboBox.currentIndex() == 1:  # h
                aux /= 3600
                hours = int(aux)
                aux -= hours
                aux *= 60
                minutes = int(aux)
                aux -= minutes
                secunds = aux * 60
                ui_circ.lineEdit_3.setText('%dh %dm %.2fs' % (hours,  minutes, secunds))
            else:  # days
                aux /= (3600*24)
                ui_circ.lineEdit_3.setText('%.6f' % aux)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    CircularWindow = QtWidgets.QMainWindow()
    ui_circ = Ui_CircularWindow()
    ui_circ.setupUi(CircularWindow)

    MainWindow.show()
    sys.exit(app.exec_())