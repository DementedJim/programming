# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\User\Documents\prog\maket.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(382, 225)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(50, 130, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 60, 21, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(190, 60, 21, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(130, 60, 31, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(60, 160, 21, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(150, 160, 21, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(30, 10, 171, 16))
        self.label_9.setObjectName("label_9")
        self.answ1 = QtWidgets.QLineEdit(Dialog)
        self.answ1.setEnabled(False)
        self.answ1.setGeometry(QtCore.QRect(90, 160, 41, 20))
        self.answ1.setObjectName("answ1")
        self.answ2 = QtWidgets.QLineEdit(Dialog)
        self.answ2.setEnabled(False)
        self.answ2.setGeometry(QtCore.QRect(180, 160, 41, 20))
        self.answ2.setObjectName("answ2")
        self.x11 = QtWidgets.QDoubleSpinBox(Dialog)
        self.x11.setGeometry(QtCore.QRect(20, 60, 62, 22))
        self.x11.setMinimum(-99.9)
        self.x11.setObjectName("x11")
        self.x12 = QtWidgets.QDoubleSpinBox(Dialog)
        self.x12.setGeometry(QtCore.QRect(120, 60, 62, 22))
        self.x12.setMinimum(-99.9)
        self.x12.setObjectName("x12")
        self.b1 = QtWidgets.QDoubleSpinBox(Dialog)
        self.b1.setGeometry(QtCore.QRect(220, 60, 62, 22))
        self.b1.setMinimum(-99.9)
        self.b1.setObjectName("b1")
        self.x22 = QtWidgets.QDoubleSpinBox(Dialog)
        self.x22.setGeometry(QtCore.QRect(120, 90, 62, 22))
        self.x22.setMinimum(-99.9)
        self.x22.setObjectName("x22")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(190, 90, 21, 16))
        self.label_5.setObjectName("label_5")
        self.x21 = QtWidgets.QDoubleSpinBox(Dialog)
        self.x21.setGeometry(QtCore.QRect(20, 90, 62, 22))
        self.x21.setMinimum(-99.9)
        self.x21.setObjectName("x21")
        self.b2 = QtWidgets.QDoubleSpinBox(Dialog)
        self.b2.setGeometry(QtCore.QRect(220, 90, 62, 22))
        self.b2.setMinimum(-99.9)
        self.b2.setObjectName("b2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(90, 90, 21, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Решить"))
        self.label.setText(_translate("Dialog", "x1+"))
        self.label_2.setText(_translate("Dialog", "x2="))
        self.label_7.setText(_translate("Dialog", "x1="))
        self.label_8.setText(_translate("Dialog", "x2="))
        self.label_9.setText(_translate("Dialog", "Система линейных уравнений:"))
        self.label_5.setText(_translate("Dialog", "x2="))
        self.label_6.setText(_translate("Dialog", "x1+"))
