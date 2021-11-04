from PyQt5 import QtWidgets, QtCore, QtGui
import myapp
import mysk
import myacc
import mydata
import searching
import tinkoffauth
import os
import sys
import requests
import time
import runpy
import csv
import multiprocessing
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
import time


# -*- coding: UTF-8 -*-


class BestCalc(QtWidgets.QMainWindow, myapp.Ui_BestCalc):  # основное окна приложения
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.acc_data)
        self.pushButton_2.clicked.connect(self.new_calc)
        self.pushButton_3.clicked.connect(self.close_program)

    def acc_data(self):  # Кнопка перехода в личный кабинет
        self.myacc = myacc()
        self.myacc.show()

    def new_calc(self):  # Кнопка Новый расчёт
        self.mydata = mydata()
        self.mydata.show()

    def close_program(self):  # Кнопка выхода
        sys.exit(app.exec_())


class myacc(QtWidgets.QMainWindow, myacc.Ui_Form):  # Меню личного кабинета
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.myacc = None
        self.save_button.clicked.connect(self.button_click)
        self.back_tomain_button.clicked.connect(self.button_2_click)

    def button_click(self):  # Кнопка "сохранить" логин и пароль b2b кабинетов + запись данных в файл
        renlogin = self.ren_login.text()
        renpass = self.ren_pass.text()
        sogllogin = self.sogl_login.text()
        soglpass = self.sogl_pass.text()
        vsklogin = self.vsk_login.text()
        vskpass = self.vsk_pass.text()
        l = [renlogin, renpass, sogllogin, soglpass, vsklogin, vskpass]
        with open(r"C:\ICC\ui\data\acc_data.txt", "w") as f:
            for line in l:
                f.write(line + '\n')
            f.close()
        self.save_button_result.setText('Успешно сохранено!')

    def button_2_click(self):  # Кнопка "На главную" из меню Личного кабинета
        self.close()
        self.BestCalc = BestCalc()
        self.BestCalc.show()


class tinkoffauth(QtWidgets.QMainWindow, tinkoffauth.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tinkoffauth = None
        self.readybutton.clicked.connect(self.ready_button_click)

    def ready_button_click(self):
        driver = webdriver.Chrome('C:\Python\chromedriver.exe')
        elem = driver.find_element_by_class_name('Button__content_TXLEK')
        elem.click()


class mydata(QtWidgets.QMainWindow, mydata.Ui_Dialog, multiprocessing.Process):  # Вызов меню анкеты
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mydata = None
        self.calc_start.clicked.connect(self.button_click)
        self.back_to_main.clicked.connect(self.button_2_click)
        self.save_data.clicked.connect(self.button_save_click)
        self.send_phone_number.clicked.connect(self.add_bypass_click)
        self.search_cl.clicked.connect(self.client_searching)
        self.driver2_add_box.stateChanged.connect(self.driver2_add)
        self.driver3_add_box.stateChanged.connect(self.driver3_add)
        self.driver4_add_box.stateChanged.connect(self.driver4_add)
        self.driver5_add_box.stateChanged.connect(self.driver5_add)

    def driver2_add(self):
        ch2 = self.driver2_add_box.isChecked()
        if ch2 is True:
            self.driver2_data.setEnabled(True)
        else:
            self.driver2_data.setEnabled(False)

    def driver3_add(self):
        ch3 = self.driver3_add_box.isChecked()
        if ch3 is True:
            self.driver3_data.setEnabled(True)
        else:
            self.driver3_data.setEnabled(False)

    def driver4_add(self):
        ch4 = self.driver4_add_box.isChecked()
        if ch4 is True:
            self.driver4_data.setEnabled(True)
        else:
            self.driver4_data.setEnabled(False)

    def driver5_add(self):
        ch5 = self.driver5_add_box.isChecked()
        if ch5 is True:
            self.driver5_data.setEnabled(True)
        else:
            self.driver5_data.setEnabled(False)

    def new_car(self):
        self.checkBox.isChecked()
        # if ch == True:

    def button_click(self):  # Меню анкеты. Старт расчёта
        abs = self.checkBox_2.isChecked()
        tinkoff = self.checkBox_3.isChecked()
        renessaince = self.checkBox_4.isChecked()
        soglasie = self.checkBox_5.isChecked()
        vsk = self.checkBox_6.isChecked()
        if abs is True:
            driver = webdriver.Chrome('C:\Python\chromedriver.exe')
            driver.get("https://mafin.ru/kasko/calc")
            elem = driver.find_element_by_id("plate-number-input")
            elem.send_keys(self.grz.text())
            elem = driver.find_element_by_class_name('cccar-data__grz-form-submit')
            elem.click()
            time.sleep(4)
            elem = driver.find_element_by_class_name('cccar-data__grz-form-submit')
            elem.click()
            elem = driver.find_element_by_id('last_name_input')
            elem.click()
            elem.send_keys(self.driver1_last_name.text())
            elem = driver.find_element_by_id('first_name_input')
            elem.click()
            elem.send_keys(self.driver1_main_name.text())
            elem = driver.find_element_by_id('middle_name_input')
            elem.click()
            elem.send_keys(self.driver1_middle_name.text())
            elem.click()
            time.sleep(1)
            elem = driver.find_element_by_id('birthday_input')
            elem.click()
            elem.send_keys(self.driver1_birthday_date.text())
            elem = driver.find_element_by_id('licence_first_year_input')
            elem.click()
            elem.send_keys(self.driver1_driver_age.text())
            elem = driver.find_element_by_class_name('cccc-drivers__button-next')
            elem.click()
            elem = driver.find_element_by_id('phone_number_input')
            elem.click()
            pn = self.phone_number.text()  # Актуально только для АС. берем номер телефона и убираем "79"
            new_phone = list(pn)  # Делаем список
            del(new_phone[0])
            del(new_phone[0])  # Удаляем первые 2 символа
            s = "".join(new_phone)  # Собираем список обратно. Было 79252679575 стало 252679575
            elem.send_keys(s)  # Передаём укороченный номер телефона обратно в форму с номером телефона
            time.sleep(1)
            elem = driver.find_element_by_class_name('cccc-contacts__submit')
            elem.click()
            time.sleep(1)
            elem = driver.find_element_by_id('smd_code_input')
            elem.click()
            elem.send_keys(u"0000")
            time.sleep(5)
            elem = driver.find_element_by_class_name('cccc-contacts__submit')
            elem.click()
        if tinkoff is True:
            driver.execute_script("window.open('https://forma.tinkoff.ru/insurance/');")
            self.tinkoffauth = tinkoffauth()
            self.tinkoffauth.show()


    def client_searching(self):  # меню поиска клиента
        self.searching = searching()
        self.searching.show()

    def button_2_click(self):  # Кнопка "Назад" меню Анкеты
        self.close()
        self.BestCalc = BestCalc()
        self.BestCalc.show()

    def button_save_click(self):  # Кнопка "сохранить" Меню анкеты клиента + запись данных в файл
        grz = str(self.grz.text())
        lastname = str(self.driver1_last_name.text())
        mainname = str(self.driver1_main_name.text())
        middlename = str(self.driver1_middle_name.text())
        birthday = str(self.driver1_birthday_date.text())
        driverage = str(self.driver1_driver_age.text())
        phonenumber = str(self.phone_number.text())
        d = [grz, lastname, mainname, middlename, birthday, driverage, phonenumber]
        f = open(r'C:\ICC\ui\data\data_client.csv', 'a', newline='')
        w = csv.writer(f, delimiter=";")
        w.writerow(d)
        f.close()
        self.bypass_result.setText('Данные сохранены!')

    def add_bypass_click(self):  # Кнопка "Добавить в Bypass" меню Анкеты
        phonenumber = str(self.phone_number.text())
        response = requests.put('https://api.mafin.ru/consent/internal/bypass/' + phonenumber)
        print(response.status_code)
        if response.status_code == 201:
            self.bypass_result.setText('Успешно добавлен!')
        elif response.status_code == 204:
            requests.delete('https://api.mafin.ru/consent/internal/bypass/' + phonenumber)
            time.sleep(3)
            requests.put('https://api.mafin.ru/consent/internal/bypass/' + phonenumber)
            self.bypass_result.setText('Успешно добавлен!')


class searching(QtWidgets.QMainWindow, searching.Ui_Searching):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.searching = None
        self.pushButton.clicked.connect(self.search_client)
        self.pushButton_3.clicked.connect(self.choose_client)

    def search_client(self):
        word = str(self.last_name.text())
        with open(r'C:\ICC\ui\data\data_client.csv') as r_file:
            reader = csv.reader(r_file, delimiter=';', quotechar=',', quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                if row[1] == word:
                    a = ' '.join(row)
                    self.textBrowser.setText(a)
                    break
                else:
                    self.textBrowser.setText('В файле нет такого клиента!')

    def choose_client(self):
        word = str(self.last_name.text())
        with open(r'C:\ICC\ui\data\data_client.csv') as r_file:
            reader = csv.reader(r_file, delimiter=';', quotechar=',', quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                ch1 = self.checkBox_3.isChecked()
                if ch1 is True:
                    if row[1] == word:
                        self.close()
                        self.mydata = mydata()
                        self.mydata.show()
                        self.mydata.grz.setText(row[0])
                        self.mydata.driver1_last_name.setText(row[1])
                        self.mydata.driver1_main_name.setText(row[2])
                        self.mydata.driver1_middle_name.setText(row[3])
                        self.mydata.driver1_birthday_date.setText(row[4])
                        self.mydata.driver1_driver_age.setText(row[5])
                        self.mydata.phone_number.setText(row[6])
                else:
                    self.textBrowser_3.setText('Клиент не выбран!')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = BestCalc()
    window.show()
    sys.exit(app.exec_())
