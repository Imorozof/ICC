from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('C:\Python\chromedriver.exe')
driver.get("https://mafin.ru/kasko/calc")
driver.execute_script("window.open('https://forma.tinkoff.ru/insurance/');")






























