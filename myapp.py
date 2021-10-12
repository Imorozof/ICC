# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BestCalc(object):
    def setupUi(self, BestCalc):
        BestCalc.setObjectName("BestCalc")
        BestCalc.resize(415, 338)
        self.centralwidget = QtWidgets.QWidget(BestCalc)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 50, 211, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 120, 211, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 190, 211, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        BestCalc.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(BestCalc)
        self.statusbar.setObjectName("statusbar")
        BestCalc.setStatusBar(self.statusbar)

        self.retranslateUi(BestCalc)
        QtCore.QMetaObject.connectSlotsByName(BestCalc)

    def retranslateUi(self, BestCalc):
        _translate = QtCore.QCoreApplication.translate
        BestCalc.setWindowTitle(_translate("BestCalc", "Автокальк"))
        self.pushButton.setText(_translate("BestCalc", "Личный кабинет"))
        self.pushButton_2.setText(_translate("BestCalc", "Новый расчёт"))
        self.pushButton_3.setText(_translate("BestCalc", "Выход"))
