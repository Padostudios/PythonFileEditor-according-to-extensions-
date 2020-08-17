# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Umut Bey/Desktop/UzantilaraGore/tasarim1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(481, 196)
        MainWindow.setMinimumSize(QtCore.QSize(481, 196))
        MainWindow.setMaximumSize(QtCore.QSize(481, 196))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/filePic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(85, 0, 0);")
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_UzantilaraGore = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_UzantilaraGore.setGeometry(QtCore.QRect(110, 120, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_UzantilaraGore.setFont(font)
        self.pushButton_UzantilaraGore.setStyleSheet("QPushButton\n"
"{background-color: rgb(255, 170, 0);\n"
"border-radius : 15px;\n"
"color: rgb(0, 0, 0);\n"
"\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: beige;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(255, 186, 11);\n"
"font-size: 14px\n"
"}\n"
"")
        self.pushButton_UzantilaraGore.setObjectName("pushButton_UzantilaraGore")
        self.pushButton_GeriAl = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_GeriAl.setGeometry(QtCore.QRect(290, 120, 160, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_GeriAl.setFont(font)
        self.pushButton_GeriAl.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 255, 0);\n"
"border-radius : 15px;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: beige;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"\n"
"background-color: rgb(98, 255, 90);\n"
"font-size: 15px;\n"
"\n"
"\n"
"\n"
"}")
        self.pushButton_GeriAl.setObjectName("pushButton_GeriAl")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 30, 331, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_gozAt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_gozAt.setGeometry(QtCore.QRect(30, 70, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_gozAt.setFont(font)
        self.pushButton_gozAt.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(255, 170, 255);\n"
"border-radius : 15px;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: beige;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(255, 187, 250);\n"
"font-size: 15px\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"")
        self.pushButton_gozAt.setObjectName("pushButton_gozAt")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 70, 341, 31))
        self.label_2.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"border-radius : 15px;\n"
"")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_Tr_flag = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Tr_flag.setGeometry(QtCore.QRect(20, 20, 32, 32))
        self.pushButton_Tr_flag.setStyleSheet("QPushButton\n"
"{border-image: url(:/icons/turkey.png);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"\n"
"}")
        self.pushButton_Tr_flag.setText("")
        self.pushButton_Tr_flag.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_Tr_flag.setObjectName("pushButton_Tr_flag")
        self.pushButton_Usa_flag = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Usa_flag.setGeometry(QtCore.QRect(60, 20, 32, 32))
        self.pushButton_Usa_flag.setStyleSheet("border-image: url(:/icons/usd.png);")
        self.pushButton_Usa_flag.setText("")
        self.pushButton_Usa_flag.setObjectName("pushButton_Usa_flag")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Klasör Düzenleyici"))
        self.pushButton_UzantilaraGore.setText(_translate("MainWindow", "Uzantıya Göre Düzenle"))
        self.pushButton_GeriAl.setText(_translate("MainWindow", "Geri Al"))
        self.label.setText(_translate("MainWindow", "Düzenlemek istediğiniz klasörü seçiniz"))
        self.pushButton_gozAt.setText(_translate("MainWindow", "..."))

import icons_rc
