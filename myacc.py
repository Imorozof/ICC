# -*- coding: utf-8 -*-


# -*- coding: UTF-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(696, 338)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(200, 30, 281, 51))
        self.textBrowser.setObjectName("textBrowser")
        renlogin = QtWidgets.QLineEdit()
        self.ren_login = QtWidgets.QLineEdit(Form)
        self.ren_login.setGeometry(QtCore.QRect(90, 140, 131, 22))
        self.ren_login.setObjectName("ren_login")
        self.ren_login.setMaxLength(20)
        self.ren_pass = QtWidgets.QLineEdit(Form)
        self.ren_pass.setGeometry(QtCore.QRect(90, 190, 131, 22))
        self.ren_pass.setObjectName("ren_pass")
        self.sogl_login = QtWidgets.QLineEdit(Form)
        self.sogl_login.setGeometry(QtCore.QRect(290, 190, 141, 22))
        self.sogl_login.setObjectName("sogl_login")
        self.sogl_pass = QtWidgets.QLineEdit(Form)
        self.sogl_pass.setGeometry(QtCore.QRect(290, 140, 141, 22))
        self.sogl_pass.setObjectName("sogl_pass")
        self.vsk_pass = QtWidgets.QLineEdit(Form)
        self.vsk_pass.setGeometry(QtCore.QRect(500, 190, 161, 22))
        self.vsk_pass.setObjectName("vsk_login")
        self.vsk_login = QtWidgets.QLineEdit(Form)
        self.vsk_login.setGeometry(QtCore.QRect(500, 140, 161, 22))
        self.vsk_login.setObjectName("vsk_pass")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 110, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(320, 110, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(540, 110, 71, 16))
        self.label_3.setObjectName("label_3")
        self.save_button = QtWidgets.QPushButton(Form)
        self.save_button.setGeometry(QtCore.QRect(70, 250, 231, 41))
        self.save_button.setObjectName("pushButton")
        self.back_tomain_button = QtWidgets.QPushButton(Form)
        self.back_tomain_button.setGeometry(QtCore.QRect(360, 250, 231, 41))
        self.back_tomain_button.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 140, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 190, 51, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(440, 140, 55, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(230, 140, 55, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(440, 190, 51, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(230, 190, 51, 16))
        self.label_9.setObjectName("label_9")
        self.save_button_result = QtWidgets.QTextBrowser(Form)
        self.save_button_result.setGeometry(QtCore.QRect(70, 300, 231, 31))
        self.save_button_result.setObjectName("textBrowser_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Введите логины и пароли от b2b кабинетов и нажмите &quot;Сохранить&quot;</p></body></html>"))
        self.label.setText(_translate("Form", "Ренессанс"))
        self.label_2.setText(_translate("Form", "Согласие"))
        self.label_3.setText(_translate("Form", "ВСК"))
        self.save_button.setText(_translate("Form", "Сохранить"))
        self.back_tomain_button.setText(_translate("Form", "На главную"))
        self.label_4.setText(_translate("Form", "Логин"))
        self.label_5.setText(_translate("Form", "Пароль"))
        self.label_6.setText(_translate("Form", "Логин"))
        self.label_7.setText(_translate("Form", "Логин"))
        self.label_8.setText(_translate("Form", "Пароль"))
        self.label_9.setText(_translate("Form", "Пароль"))
