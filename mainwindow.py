#
# MISSION PLANNER
#
# This is a software that helps user to determine orbits and oyher orbital mechanics parameters
#
# Programmed by Mario Gabriel Campos
#
# Interface created by: PyQt5 UI code generator 5.6 (pyuic5)
#

from __future__ import unicode_literals
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget, QLabel, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from functions import *
from julian_date_util import *
from functools import partial
from math import *
import sys
import numpy as np
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.cbook as cbook
import matplotlib.image as mpimg
import os.path

class Ui_MainWindow(object):
    def __init__(self):
        self.planet_radius, self.planet_names, self.planet_u = functions()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1181, 522)
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
        for x in self.planet_radius:
            self.comboBox.addItem('')
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
        self.pushButton_4.clicked.connect(self.bt_hyperbolic_cicked)
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
        self.pushButton_3.clicked.connect(self.bt_parabolic_cicked)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.bt_eliptical_cicked)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 160, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.bt_type_unknown_clicked)
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
        self.pushButton_6.clicked.connect(self.bt_julian)
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
        self.pushButton_9.clicked.connect(self.bt_plane_changes)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Mission Design Tool"))
        self.groupBox.setTitle(_translate("MainWindow", "Central Body"))
        i = 0
        for x in self.planet_names:
            self.comboBox.setItemText(i, _translate("MainWindow", x))
            i += 1
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
        planets_available = ['Earth', 'Moon', 'Sun', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus',
                             'Neptune', 'Pluto']

        if self.planet_names[value] in planets_available:
            self.pixmap100 = QPixmap(self.planet_names[value] + '-small.png')
            if self.planet_names[value] == 'Saturn':
                self.label100.setGeometry(QtCore.QRect(62, 250, 321, 261))
        else:
            self.pixmap100 = QPixmap('Pluto-small.png')

        self.label100.setPixmap(self.pixmap100)

    def bt_circulares_clicked(self):
        ui_circ.setupUi(CircularWindow)
        CircularWindow.show()

    def bt_type_unknown_clicked(self):
        TypeUnknown.show()

    def bt_eliptical_cicked(self):
        ui_elipt.setupUi(ElipticalWindow)
        ElipticalWindow.show()

    def bt_parabolic_cicked(self):
        ui_parab.setupUi(ParabolicWindow)
        ParabolicWindow.show()

    def bt_hyperbolic_cicked(self):
        ui_hyper.setupUi(HyperbolicWindow)
        HyperbolicWindow.show()

    def bt_plane_changes(self):
        ui_plane_changes.setupUi(PlaneChanges)
        PlaneChanges.show()

    def bt_julian(self):
        ui_julian.setupUi(JulianDates)
        JulianDates.show()


class Ui_CircularWindow(object):
    def __init__(self):
        self.periodo = 0  # periodo em segundos
        self.periodo_unit = 0 # tipo 0 que é segundos
        self.altitude = 0
        self.raio = 0
        self.velocidade = 0
        self.exists_graph = 0
        self.planeta = ui.comboBox.currentIndex()
        self.planeta_obj = Planetas(self.planeta)
        self.given_element = ''

    def setupUi(self, CircularWindow):
        CircularWindow.setObjectName("CircularWindow")
        CircularWindow.setFixedSize(1172, 534)
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
        self.pushButton_6.clicked.connect(self.bt_export)
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
        self.pushButton_8.clicked.connect(self.bt_graph)
        CircularWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CircularWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1172, 26))
        self.menubar.setObjectName("menubar")
        CircularWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CircularWindow)
        self.statusbar.setObjectName("statusbar")
        CircularWindow.setStatusBar(self.statusbar)
        #------------Gráfico-------------------------------------------
        self.sc = MyDynamicMplCanvas(self.centralwidget) #, width=5, height=4, dpi=100
        self.sc.setGeometry(QtCore.QRect(600, 10, 500, 500)) #550, 40, 575, 450
        self.sc.setObjectName('graph')

        self.retranslateUi(CircularWindow)
        QtCore.QMetaObject.connectSlotsByName(CircularWindow)

    def retranslateUi(self, CircularWindow):
        self.planeta = ui.comboBox.currentIndex()
        self.planeta_obj = Planetas(self.planeta)
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
        self.label_7.setText(_translate("CircularWindow", "Given element:"))
        self.pushButton_3.setText(_translate("CircularWindow", "Calculate"))
        self.pushButton_5.setText(_translate("CircularWindow", "Exit"))
        self.label_9.setText(_translate("CircularWindow", "Circular " + self.planeta_obj.name + " Orbit"))
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
        self.sc.clear_figure()
        self.label_7.setText('Given element: ')

    def bt_exit(self):
        CircularWindow.close()

    def make_graph(self):
        self.sc.update_figure(self.raio, self.raio, self.planeta)

    def bt_calculate(self):
        p1 = ui_circ.lineEdit.text().replace(',', '.')
        planeta = self.planeta
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
            self.make_graph()
            self.given_element = 'Altitude'
            self.label_7.setText('Given element: ' + self.given_element)
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
                self.make_graph()
                self.given_element = 'Radius'
                self.label_7.setText('Given element: ' + self.given_element)
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
                    self.make_graph()
                    self.given_element = 'Period'
                    self.label_7.setText('Given element: ' + self.given_element)
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
                        self.make_graph()
                        self.given_element = 'Velocity'
                        self.label_7.setText('Given element: ' + self.given_element)
                    else:
                        QMessageBox.information(CircularWindow , "Error", "No input elements found")

    def on_combobox_changed(self):
        self.periodo_unit = self.comboBox.currentIndex()
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

    def bt_export(self):
        #self.planeta = ui.comboBox.currentIndex()
        #planeta = self.planeta_obj
        print_dic = {
            'orbit_type': 'circular',
            'planet_name': self.planeta_obj.name,
            'planet_radius': self.planeta_obj.radius,
            'planet_u': self.planeta_obj.u,
            'orbit_altitude': self.altitude,
            'orbit_radius': self.raio,
            'orbit_period': self.periodo,
            'orbit_period_unit': self.periodo_unit,
            'orbit_velocity': self.velocidade,
            'given_element' : self.given_element
        }
        ex = SaveFile()
        ex.saveFileDialog(print_dic)

    def bt_graph(self):
        #self.sc.save_figure_to_png()
        ex2 = SaveFile()
        ex2.saveFigureDialog(self.sc)

    def recive_data(self, radius):
        self.raio = radius
        self.lineEdit_2.setText('%.6f' % self.raio)


class Ui_ElipticalWindow(object):
    def __init__(self):
        self.planeta = ui.comboBox.currentIndex()
        self.planeta_obj = Planetas(self.planeta)
        self.periodo_unit = 0
        self.h_perigeu = 0
        self.r_perigeu = 0
        self.excentricidade = 0
        self.semi_eixo_maior = 0
        self.periodo = 0
        self.h_apgeu = 0
        self.r_apogeu = 0
        self.v_perigeu = 0
        self.v_apogeu = 0

    def setupUi(self, ElipticalWindow):
        ElipticalWindow.setObjectName("ElipticalWindow")
        ElipticalWindow.setFixedSize(1047, 609)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("MDS-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ElipticalWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(ElipticalWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 80, 401, 371))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 50, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(60, 210, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 250, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(260, 50, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(140, 50, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 90, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 210, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 250, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(260, 90, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(260, 250, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(260, 210, 73, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.currentIndexChanged.connect(self.on_combobox_changed, self.comboBox.currentIndex())
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(30, 340, 271, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(260, 170, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 170, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(30, 170, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(60, 130, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_6.setGeometry(QtCore.QRect(140, 130, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(260, 290, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_7.setGeometry(QtCore.QRect(140, 290, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(30, 290, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 480, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.bt_export)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 480, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.bt_graph)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 480, 121, 31))
        self.pushButton_5.clicked.connect(self.bt_clear)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(540, 160, 471, 401))
        self.graphicsView.setObjectName("graphicsView")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 30, 551, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(270, 530, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.bt_calculate)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(60, 530, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.bt_exit)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(540, 20, 471, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(20, 40, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setGeometry(QtCore.QRect(20, 80, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setGeometry(QtCore.QRect(260, 40, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(140, 40, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(140, 80, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setGeometry(QtCore.QRect(260, 80, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        ElipticalWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ElipticalWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1047, 21))
        self.menubar.setObjectName("menubar")
        ElipticalWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ElipticalWindow)
        self.statusbar.setObjectName("statusbar")
        ElipticalWindow.setStatusBar(self.statusbar)
        self.sc = MyDynamicMplCanvas(self.centralwidget)  # , width=5, height=4, dpi=100
        self.sc.setGeometry(QtCore.QRect(540, 160, 471, 401))  # 550, 40, 575, 450
        self.sc.setObjectName('graph')

        self.retranslateUi(ElipticalWindow)
        QtCore.QMetaObject.connectSlotsByName(ElipticalWindow)

    def retranslateUi(self, ElipticalWindow):
        self.planeta = ui.comboBox.currentIndex()
        self.planeta_obj = Planetas(self.planeta)
        _translate = QtCore.QCoreApplication.translate
        ElipticalWindow.setWindowTitle(_translate("ElipticalWindow", "Elliptical Orbit"))
        self.groupBox.setTitle(_translate("ElipticalWindow", "Input Two Element"))
        self.label.setText(_translate("ElipticalWindow", "Periapsis Altitude:"))
        self.label_2.setText(_translate("ElipticalWindow", "Periapsis Radius:"))
        self.label_3.setText(_translate("ElipticalWindow", "Period:"))
        self.label_4.setText(_translate("ElipticalWindow", "Apoapsis Altitude:"))
        self.label_5.setText(_translate("ElipticalWindow", "[Km]"))
        self.label_6.setText(_translate("ElipticalWindow", "[Km]"))
        self.label_8.setText(_translate("ElipticalWindow", "[Km]"))
        self.comboBox.setItemText(0, _translate("ElipticalWindow", "[s]"))
        self.comboBox.setItemText(1, _translate("ElipticalWindow", "[h]"))
        self.comboBox.setItemText(2, _translate("ElipticalWindow", "[days]"))
        self.label_7.setText(_translate("ElipticalWindow", "Given elements were:"))
        self.label_10.setText(_translate("ElipticalWindow", "[Km]"))
        self.label_11.setText(_translate("ElipticalWindow", "Semimajor Axis:"))
        self.label_12.setText(_translate("ElipticalWindow", "Eccentricity:"))
        self.label_14.setText(_translate("ElipticalWindow", "[Km]"))
        self.label_15.setText(_translate("ElipticalWindow", "Apoapsis Radius:"))
        self.pushButton_3.setText(_translate("ElipticalWindow", "Export Data"))
        self.pushButton_4.setText(_translate("ElipticalWindow", "Graph Settings"))
        self.pushButton_5.setText(_translate("ElipticalWindow", "Clear"))
        self.label_9.setText(_translate("ElipticalWindow", "Eliptical " + self.planeta_obj.name  + " Orbit"))
        self.pushButton_6.setText(_translate("ElipticalWindow", "Calculate"))
        self.pushButton_7.setText(_translate("ElipticalWindow", "Exit"))
        self.groupBox_2.setTitle(_translate("ElipticalWindow", "Velocities"))
        self.label_13.setText(_translate("ElipticalWindow", "Periapsis Velocity:"))
        self.label_16.setText(_translate("ElipticalWindow", "Apoapsis Velocity:"))
        self.label_19.setText(_translate("ElipticalWindow", "[Km/s]"))
        self.label_20.setText(_translate("ElipticalWindow", "[Km/s]"))

    def make_graph(self):
        b = self.semi_eixo_maior * np.sqrt(1 - self.excentricidade ** 2)
        x_correct = self.r_apogeu - self.semi_eixo_maior
        self.sc.update_figure(self.semi_eixo_maior, b, self.planeta, x_correct)

    def bt_calculate(self):
        num_inputs = 0
        p1 = ui_elipt.lineEdit.text().replace(',', '.')
        p11 = 0
        if p1:
            id = 0
            try:
                if p11:
                    p2 = float(p1)
                    id2 = 0
                else:
                    p11 = float(p1)
                    id1 = 0
            except Exception:
                QMessageBox.critical(ElipticalWindow, "Error", "The " + self.label.text().replace(':', '').lower() +
                                     " value is not valid")
                return 0
                pass
            num_inputs += 1
        p1 = ui_elipt.lineEdit_2.text().replace(',', '.')
        if p1:
            id = 0
            try:
                if p11:
                    p2 = float(p1)
                    id2 = 1
                else:
                    p11 = float(p1)
                    id1 = 1
            except Exception:
                QMessageBox.critical(ElipticalWindow, "Error", "The " + self.label_2.text().replace(':', '').lower() +
                                     " value is not valid")
                return 0
                pass
            num_inputs += 1
        p1 = ui_elipt.lineEdit_3.text().replace(',', '.')   # Period
        if p1:
            id = 0
            try:
                if p11:
                    p2 = float(p1)
                    if ui_elipt.comboBox.currentIndex() == 1:
                        p2 *= 3600
                    elif ui_elipt.comboBox.currentIndex() == 2:
                        p2 *= (3600 * 24)
                    id2 = 4
                else:
                    p11 = float(p1)
                    if ui_elipt.comboBox.currentIndex() == 1:
                        p11 *= 3600
                    elif ui_elipt.comboBox.currentIndex() == 2:
                        p11 *= (3600 * 24)
                    id1 = 4
            except Exception:
                QMessageBox.critical(ElipticalWindow, "Error", "The " + self.label_3.text().replace(':', '').lower() +
                                     " value is not valid")
                return 0
                pass
            num_inputs += 1
        p1 = ui_elipt.lineEdit_4.text().replace(',', '.')
        if p1:
            id = 0
            try:
                if p11:
                    p2 = float(p1)
                    id2 = 5
                else:
                    p11 = float(p1)
                    id1 = 5
            except Exception:
                QMessageBox.critical(ElipticalWindow, "Error", "The " + self.label_4.text().replace(':', '').lower() +
                                     " value is not valid")
                return 0
                pass
            num_inputs += 1
        p1 = ui_elipt.lineEdit_5.text().replace(',', '.')
        if p1:
            id = 0
            try:
                if p11:
                    p2 = float(p1)
                    id2 = 3
                else:
                    p11 = float(p1)
                    id1 = 3
            except Exception:
                QMessageBox.critical(ElipticalWindow, "Error", "The " + self.label_11.text().replace(':', '').lower() +
                                     " value is not valid")
                return 0
                pass
            num_inputs += 1
        p1 = ui_elipt.lineEdit_6.text().replace(',', '.')
        if p1:
            id = 0
            try:
                if p11:
                    p2 = float(p1)
                    id2 = 2
                else:
                    p11 = float(p1)
                    id1 = 2
            except Exception:
                QMessageBox.critical(ElipticalWindow, "Error", "The " + self.label_12.text().replace(':', '').lower() +
                                     " value is not valid")
                return 0
                pass
            num_inputs += 1
        p1 = ui_elipt.lineEdit_7.text().replace(',', '.')
        if p1:
            id = 0
            try:
                if p11:
                    p2 = float(p1)
                    id2 = 6
                else:
                    p11 = float(p1)
                    id1 = 6
            except Exception:
                QMessageBox.critical(ElipticalWindow, "Error", "The " + self.label_15.text().replace(':', '').lower() +
                                     " value is not valid")
                return 0
                pass
            num_inputs += 1

        if num_inputs != 2:
            QMessageBox.critical(ElipticalWindow, "Error", 'This function requires exactly two elements')
            return 0
        else:
            [self.h_perigeu, self.r_perigeu, self.excentricidade, self.semi_eixo_maior, self.periodo, self.h_apgeu,
             self.r_apogeu, self.v_perigeu, self.v_apogeu] = orbita_eliptica(self.planeta , id1, p11, id2, p2)
            ui_elipt.lineEdit.setText('%.4f' % self.h_perigeu)
            ui_elipt.lineEdit_2.setText('%.4f' % self.r_perigeu)
            ui_elipt.lineEdit_3.setText('%.6f' % self.periodo)
            ui_elipt.lineEdit_4.setText('%.4f' % self.h_apgeu)
            ui_elipt.lineEdit_5.setText('%.6f' % self.semi_eixo_maior)
            ui_elipt.lineEdit_6.setText('%.10f' % self.excentricidade)
            ui_elipt.lineEdit_7.setText('%.4f' % self.r_apogeu)
            ui_elipt.lineEdit_8.setText('%.6f' % self.v_perigeu)
            ui_elipt.lineEdit_9.setText('%.6f' % self.v_apogeu)
            self.on_combobox_changed()
            self.make_graph()

    def bt_clear(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        self.lineEdit_9.clear()
        self.sc.clear_figure()
        #self.label_7.setText('Given element: ')

    def on_combobox_changed(self):
        self.periodo_unit = self.comboBox.currentIndex()
        if  self.periodo:
            aux = self.periodo #(Seconds)
            if self.comboBox.currentIndex() == 0:  # s
                ui_elipt.lineEdit_3.setText('%.6f' % aux)
            elif self.comboBox.currentIndex() == 1:  # h
                aux /= 3600
                hours = int(aux)
                aux -= hours
                aux *= 60
                minutes = int(aux)
                aux -= minutes
                secunds = aux * 60
                ui_elipt.lineEdit_3.setText('%dh %dm %.2fs' % (hours,  minutes, secunds))
            else:  # days
                aux /= (3600*24)
                ui_elipt.lineEdit_3.setText('%.6f' % aux)

    def bt_exit(self):
        ElipticalWindow.close()

    def bt_export(self):
        #self.planeta = ui.comboBox.currentIndex()
        #planeta = self.planeta_obj
        print_dic = {
            'orbit_type': 'elliptical',
            'planet_name': self.planeta_obj.name,
            'planet_radius': self.planeta_obj.radius,
            'planet_u': self.planeta_obj.u,
            'orbit_p_altitude': self.h_perigeu,
            'orbit_p_radius': self.r_perigeu,
            'orbit_a_altitude': self.h_apgeu,
            'orbit_a_radius': self.r_apogeu,
            'orbit_period': self.periodo,
            'orbit_period_unit': self.periodo_unit,
            'orbit_eccentricity': self.excentricidade,
            'orbit_semimajor_axis': self.semi_eixo_maior,
            'orbit_p_velocity': self.v_perigeu,
            'orbit_a_velocity': self.v_apogeu
            #'given_element' : self.given_element
        }
        ex = SaveFile()
        ex.saveFileDialog(print_dic)

    def bt_graph(self):
        #self.sc.save_figure_to_png()
        ex2 = SaveFile()
        ex2.saveFigureDialog(self.sc)

    def recive_data(self, a, e):
        self.semi_eixo_maior = a
        self.excentricidade = e
        self.lineEdit_5.setText('%.6f' % self.semi_eixo_maior)
        self.lineEdit_6.setText('%.10f' % self.excentricidade)


class Ui_ParabolicWindow(object):
    def __init__(self):
        self.p = 0  # semi-latus rectum
        self.altitude_perigeu = 0
        self.raio_perigeu = 0
        self.velocidade_perigeu = 0
        self.planeta = ui.comboBox.currentIndex()
        self.planeta_obj = Planetas(self.planeta)
        self.given_element = ''

    def setupUi(self, ParabolicWindow):
        ParabolicWindow.setObjectName("ParabolicWindow")
        ParabolicWindow.setFixedSize(1172, 534)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("MDS-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ParabolicWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(CircularWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(80, 90, 371, 241))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 50, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 91, 21))
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
        self.label_88 = QtWidgets.QLabel(self.groupBox)
        self.label_88.setGeometry(QtCore.QRect(250, 130, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_88.setFont(font)
        self.label_88.setObjectName("label_8")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(250, 170, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
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
        self.pushButton_6.clicked.connect(self.bt_export)
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
        self.pushButton_8.clicked.connect(self.bt_graph)
        ParabolicWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ParabolicWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1172, 26))
        self.menubar.setObjectName("menubar")
        ParabolicWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ParabolicWindow)
        self.statusbar.setObjectName("statusbar")
        ParabolicWindow.setStatusBar(self.statusbar)
        #------------Gráfico-------------------------------------------
        self.sc = MyDynamicMplCanvas(self.centralwidget) #, width=5, height=4, dpi=100
        self.sc.setGeometry(QtCore.QRect(600, 10, 500, 500)) #550, 40, 575, 450
        self.sc.setObjectName('graph')

        self.retranslateUi(ParabolicWindow)
        QtCore.QMetaObject.connectSlotsByName(ParabolicWindow)

    def retranslateUi(self, ParabolicWindow):
        self.planeta = ui.comboBox.currentIndex()
        self.planeta_obj = Planetas(self.planeta)
        _translate = QtCore.QCoreApplication.translate
        ParabolicWindow.setWindowTitle(_translate("ParabolicWindow", "Parabolic Orbit"))
        self.groupBox.setTitle(_translate("ParabolicWindow", "Input any Element"))
        self.label.setText(_translate("ParabolicWindow", "Periapsis altitude:"))
        self.label_2.setText(_translate("ParabolicWindow", "Periapsis Radius:"))
        self.label_3.setText(_translate("ParabolicWindow", "Semilatus Rectum:"))
        self.label_4.setText(_translate("ParabolicWindow", "Periapsis Velocity:"))
        self.label_5.setText(_translate("ParabolicWindow", "[Km]"))
        self.label_6.setText(_translate("ParabolicWindow", "[Km]"))
        self.label_88.setText(_translate("ParabolicWindow", "[Km]"))
        self.label_8.setText(_translate("ParabolicWindow", "[Km/s]"))
        self.label_7.setText(_translate("ParabolicWindow", "Given element:"))
        self.pushButton_3.setText(_translate("ParabolicWindow", "Calculate"))
        self.pushButton_5.setText(_translate("ParabolicWindow", "Exit"))
        self.label_9.setText(_translate("ParabolicWindow", "Parabolic " + self.planeta_obj.name + " Orbit"))
        self.pushButton_6.setText(_translate("ParabolicWindow", "Export Data"))
        self.pushButton_7.setText(_translate("ParabolicWindow", "Clear"))
        self.pushButton_8.setText(_translate("ParabolicWindow", "Graph Settings"))

    def bt_clear(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.sc.clear_figure()
        self.label_7.setText('Given element: ')
        self.p = 0  # semi-latus rectum
        self.altitude = 0
        self.raio_perigeu = 0
        self.velocidade_perigeu = 0

    def bt_exit(self):
        ParabolicWindow.close()

    def make_graph(self):
        x_correct = -self.p
        self.sc.update_figure(self.raio_perigeu, 0, self.planeta, x_correct=x_correct, infinite=1)
        pass

    def bt_calculate(self):
        p1 = ui_parab.lineEdit.text().replace(',', '.')
        planeta = self.planeta
        if p1:
            id = 0
            try:
                p1 = float(p1)
            except Exception:
                QMessageBox.critical(CircularWindow, "Error", "The altitude value is not valid")
                return 0
                pass
            [self.altitude_perigeu, self.raio_perigeu, self.p, self.velocidade_perigeu] = orbita_parabolica(planeta,
                                                                                                            id, p1)
            self.lineEdit_2.setText('%.6f' % self.raio_perigeu)
            self.lineEdit_4.setText('%.6f' % self.velocidade_perigeu)
            self.lineEdit_3.setText('%.6f' % self.p)
            self.make_graph()
            self.given_element = 'Periapsis altitude'
            self.label_7.setText('Given element: ' + self.given_element)
        else:
            p1 = ui_parab.lineEdit_2.text().replace(',', '.')
            if p1:
                id = 1
                try:
                    p1 = float(p1)
                except Exception:
                    QMessageBox.critical(CircularWindow, "Error", "The radius value is not valid")
                    return 0
                    pass
                [self.altitude_perigeu, self.raio_perigeu, self.p, self.velocidade_perigeu] = orbita_parabolica(planeta,
                                                                                                                id, p1)
                self.lineEdit.setText('%.6f' % self.altitude_perigeu)
                self.lineEdit_4.setText('%.6f' % self.velocidade_perigeu)
                self.lineEdit_3.setText('%.6f' % self.p)
                self.make_graph()
                self.given_element = 'Periapsis radius'
                self.label_7.setText('Given element: ' + self.given_element)
            else:
                p1 = ui_parab.lineEdit_3.text().replace(',', '.')
                if p1:
                    id = 2
                    try:
                        p1 = float(p1)
                    except Exception:
                        QMessageBox.critical(CircularWindow, "Error", "The semilatus rectum value is not valid")
                        return 0
                        pass
                    [self.altitude_perigeu, self.raio_perigeu, self.p, self.velocidade_perigeu] = orbita_parabolica(
                        planeta,
                        id, p1)
                    self.lineEdit.setText('%.6f' % self.altitude_perigeu)
                    self.lineEdit_4.setText('%.6f' % self.velocidade_perigeu)
                    self.lineEdit_2.setText('%.6f' % self.raio_perigeu)
                    self.make_graph()
                    self.given_element = 'Semilatus rectum'
                    self.label_7.setText('Given element: ' + self.given_element)
                else:
                    p1 = ui_parab.lineEdit_4.text().replace(',', '.')
                    if p1:
                        id = 3
                        try:
                            p1 = float(p1)
                        except Exception:
                            QMessageBox.critical(CircularWindow, "Error", "The velocity value is not valid")
                            return 0
                            pass
                        [self.altitude_perigeu, self.raio_perigeu, self.p, self.velocidade_perigeu] = orbita_parabolica(
                            planeta,
                            id, p1)
                        self.lineEdit.setText('%.6f' % self.altitude_perigeu)
                        self.lineEdit_3.setText('%.6f' % self.p)
                        self.lineEdit_2.setText('%.6f' % self.raio_perigeu)
                        self.make_graph()
                        self.given_element = 'Periapsis velocity'
                        self.label_7.setText('Given element: ' + self.given_element)
                    else:
                        QMessageBox.information(CircularWindow, "Error", "No input elements found")

    def bt_export(self):
        #self.planeta = ui.comboBox.currentIndex()
        #planeta = self.planeta_obj
        print_dic = {
            'orbit_type': 'parabolic',
            'planet_name': self.planeta_obj.name,
            'planet_radius': self.planeta_obj.radius,
            'planet_u': self.planeta_obj.u,
            'orbit_p_altitude': self.altitude_perigeu,
            'orbit_p_radius': self.raio_perigeu,
            'orbit_p': self.p,
            'orbit_p_velocity': self.velocidade_perigeu,
            'given_element' : self.given_element
        }
        ex = SaveFile()
        ex.saveFileDialog(print_dic)

    def bt_graph(self):
        #self.sc.save_figure_to_png()
        ex2 = SaveFile()
        ex2.saveFigureDialog(self.sc)

    def recive_data(self, radius):
        self.raio_perigeu = radius
        self.lineEdit_2.setText('%.6f' % self.raio_perigeu)


class Ui_HyperbolicWindow(object):
    def __init__(self):
        self.planeta = ui.comboBox.currentIndex()
        self.planeta_obj = Planetas(self.planeta)
        self.h_periapsis = 0
        self.r_periapsis = 0
        self.excentricidade = 0
        self.semi_eixo_maior = 0
        self.semi_eixo_menor = 0
        self.v_periapsis = 0
        self.v_infinity = 0
        self.c3 = 0
        self.angle = 0

    def setupUi(self, HyperbolicWindow):
        HyperbolicWindow.setObjectName("HyperbolicWindow")
        HyperbolicWindow.setFixedSize(1047, 588)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("MDS-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HyperbolicWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(HyperbolicWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 80, 401, 451))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 50, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_1 = QtWidgets.QLabel(self.groupBox)
        self.label_1.setGeometry(QtCore.QRect(30, 90, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_1.setFont(font)
        self.label_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_1.setObjectName("label_1")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 210, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 250, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_55 = QtWidgets.QLabel(self.groupBox)
        self.label_55.setGeometry(QtCore.QRect(260, 50, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(140, 50, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_1.setGeometry(QtCore.QRect(140, 90, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 210, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 250, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_56 = QtWidgets.QLabel(self.groupBox)
        self.label_56.setGeometry(QtCore.QRect(260, 90, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_56.setFont(font)
        self.label_56.setObjectName("label_56")
        self.label_58 = QtWidgets.QLabel(self.groupBox)
        self.label_58.setGeometry(QtCore.QRect(260, 250, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_58.setFont(font)
        self.label_58.setObjectName("label_58")
        self.label_47 = QtWidgets.QLabel(self.groupBox)
        self.label_47.setGeometry(QtCore.QRect(30, 420, 271, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(260, 170, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 170, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 170, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(60, 130, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 130, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(260, 290, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_6.setGeometry(QtCore.QRect(140, 290, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 290, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(260, 210, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_7.setGeometry(QtCore.QRect(140, 330, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_8.setGeometry(QtCore.QRect(140, 370, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 370, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(260, 330, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 330, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(260, 370, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(840, 470, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(700, 470, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(560, 470, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(520, 40, 471, 401))
        self.graphicsView.setObjectName("graphicsView")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 30, 551, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(770, 510, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(560, 510, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        HyperbolicWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HyperbolicWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1047, 21))
        self.menubar.setObjectName("menubar")
        HyperbolicWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HyperbolicWindow)
        self.statusbar.setObjectName("statusbar")
        HyperbolicWindow.setStatusBar(self.statusbar)
        self.sc = MyDynamicMplCanvas(self.centralwidget)  # , width=5, height=4, dpi=100
        self.sc.setGeometry(QtCore.QRect(520, 40, 471, 401))  # 550, 40, 575, 450
        self.sc.setObjectName('graph')

        self.retranslateUi(HyperbolicWindow)
        QtCore.QMetaObject.connectSlotsByName(HyperbolicWindow)

    def retranslateUi(self, HyperbolicWindow):
        self.planeta = ui.comboBox.currentIndex()
        self.planeta_obj = Planetas(self.planeta)
        _translate = QtCore.QCoreApplication.translate
        HyperbolicWindow.setWindowTitle(_translate("HyperbolicWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("HyperbolicWindow", "Input Two Element"))
        self.label.setText(_translate("HyperbolicWindow", "Periapsis Altitude:"))
        self.label_1.setText(_translate("HyperbolicWindow", "Periapsis Radius:"))
        self.label_4.setText(_translate("HyperbolicWindow", "Semiminor Axis:"))
        self.label_5.setText(_translate("HyperbolicWindow", "Periapsis Velocity:"))
        self.label_55.setText(_translate("HyperbolicWindow", "[Km]"))
        self.label_56.setText(_translate("HyperbolicWindow", "[Km]"))
        self.label_58.setText(_translate("HyperbolicWindow", "[Km/s]"))
        self.label_47.setText(_translate("HyperbolicWindow", "Given elements were:"))
        self.label_10.setText(_translate("HyperbolicWindow", "[Km]"))
        self.label_3.setText(_translate("HyperbolicWindow", "Semimajor Axis:"))
        self.label_2.setText(_translate("HyperbolicWindow", "Eccentricity:"))
        self.label_14.setText(_translate("HyperbolicWindow", "[Km/s]"))
        self.label_6.setText(_translate("HyperbolicWindow", "Velocity at Infinity:"))
        self.label_17.setText(_translate("HyperbolicWindow", "[Km]"))
        self.label_8.setText(_translate("HyperbolicWindow", "Asymptote Angle:"))
        self.label_19.setText(_translate("HyperbolicWindow", "[Km^2/s^2]"))
        self.label_7.setText(_translate("HyperbolicWindow", "C3:"))
        self.label_20.setText(_translate("HyperbolicWindow", "[deg]"))
        self.pushButton_3.setText(_translate("HyperbolicWindow", "Export Data"))
        self.pushButton_4.setText(_translate("HyperbolicWindow", "Graph Settings"))
        self.pushButton_5.setText(_translate("HyperbolicWindow", "Clear"))
        self.label_9.setText(_translate("HyperbolicWindow", "Hyperbolic " + self.planeta_obj.name + " Orbit"))
        self.pushButton_6.setText(_translate("HyperbolicWindow", "Calculate"))
        self.pushButton_7.setText(_translate("HyperbolicWindow", "Exit"))





class Ui_TypeUnknown(object):
    def setupUi(self, TypeUnknown):
        TypeUnknown.setObjectName("TypeUnknown")
        TypeUnknown.setFixedSize(522, 348)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("MDS-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TypeUnknown.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(TypeUnknown)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 40, 441, 181))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 50, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(90, 90, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(90, 130, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(310, 50, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(170, 50, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 90, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 130, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(310, 90, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(310, 130, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 260, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.bt_determine_orbit)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 260, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.bt_exit)
        TypeUnknown.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TypeUnknown)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 522, 26))
        self.menubar.setObjectName("menubar")
        TypeUnknown.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TypeUnknown)
        self.statusbar.setObjectName("statusbar")
        TypeUnknown.setStatusBar(self.statusbar)

        self.retranslateUi(TypeUnknown)
        QtCore.QMetaObject.connectSlotsByName(TypeUnknown)

    def retranslateUi(self, TypeUnknown):
        _translate = QtCore.QCoreApplication.translate
        TypeUnknown.setWindowTitle(_translate("TypeUnknown", "Type Unknown"))
        self.groupBox.setTitle(_translate("TypeUnknown", "Input parameters at a point"))
        self.label.setText(_translate("TypeUnknown", "Flight path angle:"))
        self.label_2.setText(_translate("TypeUnknown", "Radius:"))
        self.label_4.setText(_translate("TypeUnknown", "Velocity:"))
        self.label_5.setText(_translate("TypeUnknown", "[degrees]"))
        self.label_6.setText(_translate("TypeUnknown", "[Km]"))
        self.label_8.setText(_translate("TypeUnknown", "[Km/s]"))
        self.pushButton_3.setText(_translate("TypeUnknown", "Determine Orbit"))
        self.pushButton_5.setText(_translate("TypeUnknown", "Exit"))

    def bt_exit(self):
        TypeUnknown.close()

    def bt_determine_orbit(self):
        planeta = ui.comboBox.currentIndex()

        gama = ui_type_unknown.lineEdit.text().replace(',', '.')
        try:
            gama = float(gama)
        except Exception:
            QMessageBox.critical(CircularWindow, "Error", "The flight path angle value is not valid")
            return 0
            pass

        r = ui_type_unknown.lineEdit_2.text().replace(',', '.')
        try:
            r = float(r)
        except Exception:
            QMessageBox.critical(CircularWindow, "Error", "The radius value is not valid")
            return 0
            pass

        v = ui_type_unknown.lineEdit_4.text().replace(',', '.')
        try:
            v = float(v)
        except Exception:
            QMessageBox.critical(CircularWindow, "Error", "The velocity value is not valid")
            return 0
            pass


        [a, e] = orbita_desconhecida(planeta, r, v, gama)

        msgbox = QMessageBox()
        msgbox.setText("Which orbit do you want to proceed ?")
        msgbox.setInformativeText("e = %.8f" % e)
        msgbox.setWindowTitle("Type Unknown")

        bt_clicked = 0

        if e < 0.00000000001:
            msgbox.addButton('Circular Orbit', QMessageBox.YesRole)
        elif e < 1:
            bt_clicked = 1
            msgbox.addButton('Eliptical Orbit', QMessageBox.NoRole)
        elif e == 1:
            bt_clicked = 2
            msgbox.addButton('Parabiloc Orbit', QMessageBox.RejectRole)
        else:
            bt_clicked = 3
            msgbox.addButton('Hyperbolic Orbit', QMessageBox.AcceptRole)

        ret = msgbox.exec_()
        orbit = ret + bt_clicked #0-circ 1-elip 2-para 3-hyper
        self.lineEdit_2.clear()
        self.lineEdit.clear()
        self.lineEdit_4.clear()
        TypeUnknown.close()
        if bt_clicked == 0:
            ui_circ.setupUi(CircularWindow)
            CircularWindow.show()
            ui_circ.recive_data(a)

        elif bt_clicked == 1:
            ui_elipt.setupUi(ElipticalWindow)
            ElipticalWindow.show()
            ui_elipt.recive_data(a, e)
        elif bt_clicked == 2:
            ui_parab.setupUi(ParabolicWindow)
            ParabolicWindow.show()
            ui_circ.recive_data(a)
        else:
            pass


class Ui_PlaneChanges(object):
    def setupUi(self, PlaneChanges):
        PlaneChanges.setObjectName("PlaneChanges")
        PlaneChanges.setFixedSize(522, 348)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("MDS-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PlaneChanges.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(PlaneChanges)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 40, 441, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 50, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(310, 50, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(170, 50, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 90, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(310, 90, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 260, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.bt_calculate)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 260, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.bt_clear)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(350, 200, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 200, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(210, 200, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        PlaneChanges.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PlaneChanges)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 522, 21))
        self.menubar.setObjectName("menubar")
        PlaneChanges.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PlaneChanges)
        self.statusbar.setObjectName("statusbar")
        PlaneChanges.setStatusBar(self.statusbar)

        self.retranslateUi(PlaneChanges)
        QtCore.QMetaObject.connectSlotsByName(PlaneChanges)

    def retranslateUi(self, PlaneChanges):
        _translate = QtCore.QCoreApplication.translate
        PlaneChanges.setWindowTitle(_translate("PlaneChanges", "Type Unknown"))
        self.groupBox.setTitle(_translate("PlaneChanges", "Input both parameters"))
        self.label.setText(_translate("PlaneChanges", "Velocity:"))
        self.label_2.setText(_translate("PlaneChanges", "Plane Change Angle:"))
        self.label_5.setText(_translate("PlaneChanges", "[Km/s]"))
        self.label_6.setText(_translate("PlaneChanges", "[degrees]"))
        self.pushButton_3.setText(_translate("PlaneChanges", "Calculate"))
        self.pushButton_5.setText(_translate("PlaneChanges", "Clear"))
        self.label_8.setText(_translate("PlaneChanges", "[Km/s]"))
        self.label_4.setText(_translate("PlaneChanges", "Delta Velocity Required:"))

    def bt_calculate(self):
        p1 = self.lineEdit.text().replace(',', '.')
        p2 = self.lineEdit_2.text().replace(',', '.')
        try:
            p1 = float(p1)
            p2 = float(p2)
        except Exception:
            QMessageBox.critical(PlaneChanges, "Error", "The values inserted are not valid")
            return 0
            pass

        v = plane_changes(p1, p2)
        self.lineEdit_4.setText('%.8f' % v)

    def bt_clear(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_4.clear()


class Ui_JulianDates(object):
    def setupUi(self, JulianDates):
        JulianDates.setObjectName("JulianDates")
        JulianDates.setFixedSize(751, 518)
        self.centralwidget = QtWidgets.QWidget(JulianDates)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 40, 651, 201))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 70, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(100, 70, 71, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 110, 71, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(40, 30, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 150, 71, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(40, 150, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(290, 40, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(440, 40, 141, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(290, 80, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(440, 80, 141, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(460, 140, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.bt_julian_gregorian_calculate)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(270, 140, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.bt_julian_gragorian_clear)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 270, 651, 201))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(40, 70, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(40, 110, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(100, 70, 71, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(100, 110, 71, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(40, 30, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(100, 150, 71, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(40, 150, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(460, 140, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.bt_between_dates_calculate)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_7.setGeometry(QtCore.QRect(460, 100, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.bt_between_dates_clear)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(270, 150, 71, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(210, 110, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(270, 70, 71, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(210, 70, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(210, 150, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_11.setGeometry(QtCore.QRect(270, 110, 71, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(210, 30, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_12.setGeometry(QtCore.QRect(460, 60, 141, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setText("")
        self.lineEdit_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(470, 30, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        JulianDates.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(JulianDates)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 751, 21))
        self.menubar.setObjectName("menubar")
        JulianDates.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(JulianDates)
        self.statusbar.setObjectName("statusbar")
        JulianDates.setStatusBar(self.statusbar)

        self.retranslateUi(JulianDates)
        QtCore.QMetaObject.connectSlotsByName(JulianDates)

    def retranslateUi(self, JulianDates):
        _translate = QtCore.QCoreApplication.translate
        JulianDates.setWindowTitle(_translate("JulianDates", "Type Unknown"))
        self.groupBox.setTitle(_translate("JulianDates", "Julian Dates"))
        self.label.setText(_translate("JulianDates", "Day:"))
        self.label_2.setText(_translate("JulianDates", "Month:"))
        self.label_3.setText(_translate("JulianDates", "Gregorian Calendar Date"))
        self.label_4.setText(_translate("JulianDates", "Year:"))
        self.label_5.setText(_translate("JulianDates", "Julian Date:"))
        self.label_6.setText(_translate("JulianDates", "Modified Julian Date:"))
        self.pushButton_4.setText(_translate("JulianDates", "Calculate"))
        self.pushButton_6.setText(_translate("JulianDates", "Clear"))
        self.groupBox_2.setTitle(_translate("JulianDates", "Days Between Dates"))
        self.label_7.setText(_translate("JulianDates", "Day:"))
        self.label_8.setText(_translate("JulianDates", "Month:"))
        self.label_9.setText(_translate("JulianDates", "Initial Date"))
        self.label_10.setText(_translate("JulianDates", "Year:"))
        self.pushButton_5.setText(_translate("JulianDates", "Calculate"))
        self.pushButton_7.setText(_translate("JulianDates", "Clear"))
        self.label_11.setText(_translate("JulianDates", "Month:"))
        self.label_12.setText(_translate("JulianDates", "Day:"))
        self.label_13.setText(_translate("JulianDates", "Year:"))
        self.label_14.setText(_translate("JulianDates", "Ending Date"))
        self.label_15.setText(_translate("JulianDates", "Days Between"))

    def bt_julian_gregorian_calculate(self):
        p1 = self.lineEdit.text().replace(',', '.')
        if p1:
            p2 = self.lineEdit_2.text().replace(',', '.')
            p3 = self.lineEdit_4.text().replace(',', '.')
            try:
                p1 = float(p1)
                p2 = float(p2)
                p3 = float(p3)
            except Exception:
                QMessageBox.critical(JulianDates, "Error", "The gregorian date inserted is not valid")
                return 0
                pass
            day = p1
            month = p2
            year = p3
            date_julian = date_to_jd(year, month, day)
            self.lineEdit_3.setText('%.2f' % date_julian)
            date_julian_modified = date_julian - 2400000.5
            self.lineEdit_5.setText('%.2f' % date_julian_modified)

        else:
            p1 = self.lineEdit_3.text().replace(',', '.')
            if p1:
                try:
                    p1 = float(p1)
                except Exception:
                    QMessageBox.critical(JulianDates, "Error", "The julian inserted date is no valid")
                    return 0
                    pass
                date_julian = p1
                date_julian_modified = date_julian - 2400000.5
                self.lineEdit_5.setText('%.2f' % date_julian_modified)
                [year, month, day] = jd_to_date(date_julian)
                self.lineEdit.setText('%.2f' % day)
                self.lineEdit_2.setText('%d' % month)
                self.lineEdit_4.setText('%d' % year)
            else:
                p1 = self.lineEdit_5.text().replace(',', '.')
                if p1:
                    try:
                        p1 = float(p1)
                    except Exception:
                        QMessageBox.critical(JulianDates, "Error", "The vmodified julian date inserted is not valid")
                        return 0
                        pass
                    date_julian_modified = p1
                    date_julian = date_julian_modified + 2400000.5
                    self.lineEdit_3.setText('%.2f' % date_julian)
                    [year, month, day] = jd_to_date(date_julian)
                    self.lineEdit.setText('%.2f' % day)
                    self.lineEdit_2.setText('%d' % month)
                    self.lineEdit_4.setText('%d' % year)
                else:
                    QMessageBox.critical(JulianDates, "Error", "No dates found")

    def bt_julian_gragorian_clear(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_4.clear()
        self.lineEdit_3.clear()
        self.lineEdit_5.clear()

    def bt_between_dates_calculate(self):
        p1 = self.lineEdit_6.text().replace(',', '.')
        p2 = self.lineEdit_7.text().replace(',', '.')
        p3 = self.lineEdit_8.text().replace(',', '.')
        p4 = self.lineEdit_10.text().replace(',', '.')
        p5 = self.lineEdit_11.text().replace(',', '.')
        p6 = self.lineEdit_9.text().replace(',', '.')
        try:
            p1 = float(p1)
            p2 = float(p2)
            p3 = float(p3)
            p4 = float(p4)
            p5 = float(p5)
            p6 = float(p6)
        except Exception:
            QMessageBox.critical(JulianDates, "Error", "The dates inserted are not valid")
            return 0
            pass
        initial_date_julian = date_to_jd(p3, p2, p1)
        final_date_julian = date_to_jd(p6, p5, p4)
        days_interval = final_date_julian - initial_date_julian
        self.lineEdit_12.setText('%.2f' % days_interval)

    def bt_between_dates_clear(self):
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        self.lineEdit_9.clear()
        self.lineEdit_10.clear()
        self.lineEdit_11.clear()
        self.lineEdit_12.clear()


class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig = fig
        self.axes = fig.add_subplot(111)
        self.axes.grid(color='black', linestyle=':', linewidth=0.2)
        self.axes.axis('equal')

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass

    def save_figure_to_png(self, url):
        self.fig.savefig(url, dpi=300)


class MyDynamicMplCanvas(MyMplCanvas):
    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)

    def compute_initial_figure(self):
        pass

    def update_figure(self, a, b, planeta, x_correct=0, infinite=0):
        planet = Planetas(planeta)

        planets_available = ['Earth', 'Moon', 'Sun', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus',
                             'Neptune', 'Pluto']

        if planet.name in planets_available:
            image = plt.imread(planet.name + '-small.png')
        else:
            image = plt.imread('Pluto-small.png')

        raio = planet.radius
        if planet.name == 'Saturn':
            im = self.axes.imshow(image, extent=(-2.14285714 * 1.2 * raio, 2.14285714 * 1.2 * raio, -1.2 * raio,
                                                 1.2 * raio), alpha=1)
        else:
            im = self.axes.imshow(image, extent=(-raio,raio,-raio,raio), alpha=1)

        if infinite == 0:

            a = a
            b = b
            limit = 1.1 * a
            x = -a * np.sin(np.linspace(0, 2 * np.pi, 1000))
            x -= x_correct
            y = b * np.cos(np.linspace(0, 2 * np.pi, 1000))
        elif infinite == 1: #a-periapsis_radius b-planet_radius
            limit = 3.5 * planet.radius
            x = np.linspace(-limit, limit, 1000)
            y = np.linspace(-limit, limit, 1000)
            alfa = 1 / (4 * a)
            for i in range(0, len(x)):
                x[i] = -alfa * y[i] ** 2 - a
            x -= x_correct

        self.axes.cla()
        self.axes.grid(color='black', linestyle=':', linewidth=0.2)
        self.axes.axis('equal')
        self.axes.add_image(im)
        self.axes.plot(x, y)
        self.draw()

    def clear_figure(self):
        self.axes.cla()
        self.axes.grid(color='black', linestyle=':', linewidth=0.2)
        self.axes.axis('equal')
        self.draw()


class SaveFile(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #self.openFileNameDialog()
        #self.openFileNamesDialog()
        #self.saveFileDialog()

        #self.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)

    def saveFileDialog(self, print_dic):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "Text Files (*.txt)", options=options)
        if fileName:
            print(fileName + '.txt')
            file = open(fileName + '.txt', 'w')
            file.write('############################################################\n')
            file.write('#                                                          #\n')
            file.write('#                 MISSION DESIGN TOOL                      #\n')
            file.write('#                                                          #\n')
            file.write('#                Orbit Definition Tool                     #\n')
            file.write('#                                                          #\n')
            file.write('############################################################\n\n')
            file.write('===| Central Body |=========================================\n\n')
            file.write('Name: ' + print_dic['planet_name'] +'\n')
            file.write('Radius: ' + str(print_dic['planet_radius']) +' [Km]\n')
            file.write('Gravitational parameter: ' + str(print_dic['planet_u']) +' [Km^3/s^2]\n\n')
            file.write('===| Orbit Data |===========================================\n\n')
            if print_dic['orbit_type'] == 'circular':
                file.write('Type: Circular\n')
                file.write('Elements:\n')
                file.write('  -> Altitude: ' + str(print_dic['orbit_altitude']) +' [Km]\n')
                file.write('  -> Radius: ' + str(print_dic['orbit_radius']) +' [Km]\n')
                if print_dic['orbit_period_unit'] == 0:  # s
                    file.write('  -> Period: %.6f [s]\n' % print_dic['orbit_period'])
                elif print_dic['orbit_period_unit'] == 1:  # h
                    aux = print_dic['orbit_period']
                    aux /= 3600
                    hours = int(aux)
                    aux -= hours
                    aux *= 60
                    minutes = int(aux)
                    aux -= minutes
                    secunds = aux * 60
                    file.write('  -> Period: %dh %dm %.2fs \n' % (hours, minutes, secunds))
                else:  # days
                    aux = print_dic['orbit_period']
                    aux /= (3600 * 24)
                    file.write('  -> Period: %.6f [days]\n' % aux)
                file.write('  -> Velocity: ' + str(print_dic['orbit_velocity']) +' [Km/s]\n\n')
                file.write('The given element was ' + print_dic['given_element'] + '\n\n\n')
            elif print_dic['orbit_type'] == 'elliptical':
                file.write('Type: Elliptical\n')
                file.write('Orbital Elements:\n')
                file.write('  -> Periapsis altitude: ' + str(print_dic['orbit_p_altitude']) + ' [Km]\n')
                file.write('  -> Periapsis radius: ' + str(print_dic['orbit_p_radius']) + ' [Km]\n')
                file.write('  -> Eccentricity: ' + str(print_dic['orbit_eccentricity']) + '\n')
                file.write('  -> Semimajor Axis: ' + str(print_dic['orbit_semimajor_axis']) + ' [Km]\n')
                if print_dic['orbit_period_unit'] == 0:  # s
                    file.write('  -> Period: %.6f [s]\n' % print_dic['orbit_period'])
                elif print_dic['orbit_period_unit'] == 1:  # h
                    aux = print_dic['orbit_period']
                    aux /= 3600
                    hours = int(aux)
                    aux -= hours
                    aux *= 60
                    minutes = int(aux)
                    aux -= minutes
                    secunds = aux * 60
                    file.write('  -> Period: %dh %dm %.2fs \n' % (hours, minutes, secunds))
                else:  # days
                    aux = print_dic['orbit_period']
                    aux /= (3600 * 24)
                    file.write('  -> Period: %.6f [days]\n' % aux)
                file.write('  -> Apoapsis altitude: ' + str(print_dic['orbit_a_altitude']) + ' [Km]\n')
                file.write('  -> Apoapsis radius: ' + str(print_dic['orbit_a_radius']) + ' [Km]\n')
                file.write('Velocities:\n')
                file.write('  -> Periapsis velocity: ' + str(print_dic['orbit_p_velocity']) + ' [Km/s]\n')
                file.write('  -> Aposapsis velocity: ' + str(print_dic['orbit_a_velocity']) + ' [Km/s]\n\n')
                #file.write('The given element was ' + print_dic['given_element'] + '\n\n\n')
            elif print_dic['orbit_type'] == 'parabolic':
                file.write('Type: Parabolic\n')
                file.write('Orbital Elements:\n')
                file.write('  -> Periapsis altitude: ' + str(print_dic['orbit_p_altitude']) + ' [Km]\n')
                file.write('  -> Periapsis radius: ' + str(print_dic['orbit_p_radius']) + ' [Km]\n')
                file.write('  -> Semilatus rectum: ' + str(print_dic['orbit_p']) + '[Km]\n')
                file.write('  -> Periapsis velocity: ' + str(print_dic['orbit_p_velocity']) + ' [Km/s]\n\n')
                file.write('The given element was ' + print_dic['given_element'] + '\n\n\n')
            file.write('____________________________________________________________\n')
            file.write('')
            file.close()

    def saveFigureDialog(self, sc):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "PNG image (*.png)", options=options)
        if fileName:
            url = fileName
            sc.save_figure_to_png(url)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    CircularWindow = QtWidgets.QMainWindow()
    ui_circ = Ui_CircularWindow()
    ui_circ.setupUi(CircularWindow)

    TypeUnknown = QtWidgets.QMainWindow()
    ui_type_unknown = Ui_TypeUnknown()
    ui_type_unknown.setupUi(TypeUnknown)

    ElipticalWindow = QtWidgets.QMainWindow()
    ui_elipt = Ui_ElipticalWindow()
    ui_elipt.setupUi(ElipticalWindow)

    ParabolicWindow = QtWidgets.QMainWindow()
    ui_parab = Ui_ParabolicWindow()
    ui_parab.setupUi(ParabolicWindow)

    HyperbolicWindow = QtWidgets.QMainWindow()
    ui_hyper = Ui_HyperbolicWindow()
    ui_hyper.setupUi(HyperbolicWindow)

    PlaneChanges = QtWidgets.QMainWindow()
    ui_plane_changes = Ui_PlaneChanges()
    ui_plane_changes.setupUi(PlaneChanges)

    JulianDates = QtWidgets.QMainWindow()
    ui_julian = Ui_JulianDates()
    ui_julian.setupUi(JulianDates)


    MainWindow.show()
    sys.exit(app.exec_())

# Adicionar:
#   X Data from txt (horizons NASA)
#   - About
#   - grey circle for other planet
#   - option to add planets from txt
#   - pre determined planets
#   - txt output add coment character
#   - Saturn issue
#   - Acrscentar B0 (beta 0)