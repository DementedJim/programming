# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\User\Documents\prog\ser.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(292, 125)
        self.SolveButton = QtWidgets.QPushButton(Dialog)
        self.SolveButton.setGeometry(QtCore.QRect(40, 50, 75, 23))
        self.SolveButton.setObjectName("SolveButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 20, 31, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(160, 20, 16, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(250, 20, 31, 21))
        self.label_3.setObjectName("label_3")
        self.CancelButton = QtWidgets.QPushButton(Dialog)
        self.CancelButton.setGeometry(QtCore.QRect(130, 50, 75, 23))
        self.CancelButton.setObjectName("CancelButton")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 80, 21, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 100, 21, 21))
        self.label_5.setObjectName("label_5")
        self.x1 = QtWidgets.QLabel(Dialog)
        self.x1.setGeometry(QtCore.QRect(60, 80, 141, 21))
        self.x1.setText("")
        self.x1.setObjectName("x1")
        self.x2 = QtWidgets.QLabel(Dialog)
        self.x2.setGeometry(QtCore.QRect(60, 100, 141, 21))
        self.x2.setText("")
        self.x2.setObjectName("x2")
        self.a = QtWidgets.QDoubleSpinBox(Dialog)
        self.a.setGeometry(QtCore.QRect(10, 20, 61, 22))
        self.a.setMinimum(-99.9)
        self.a.setProperty("value", 0.0)
        self.a.setObjectName("a")
        self.b = QtWidgets.QDoubleSpinBox(Dialog)
        self.b.setGeometry(QtCore.QRect(100, 20, 61, 22))
        self.b.setMinimum(-99.9)
        self.b.setObjectName("b")
        self.c = QtWidgets.QDoubleSpinBox(Dialog)
        self.c.setGeometry(QtCore.QRect(180, 20, 61, 22))
        self.c.setMinimum(-99.0)
        self.c.setObjectName("c")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.SolveButton.setText(_translate("Dialog", "Решить"))
        self.label.setText(_translate("Dialog", " x^2+"))
        self.label_2.setText(_translate("Dialog", " x+"))
        self.label_3.setText(_translate("Dialog", "=0"))
        self.CancelButton.setText(_translate("Dialog", "Выйти"))
        self.label_4.setText(_translate("Dialog", " x1="))
        self.label_5.setText(_translate("Dialog", " x2="))
