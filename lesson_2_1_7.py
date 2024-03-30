from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from kalkum import *


try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ищем элемент, у которого надо считать занчение атрибута
    field_WX = browser.find_element(By.ID, 'treasure')
    #берем значение атрибута
    valuex_value = field_WX.get_attribute("valuex")

    #считаем значение
    x = valuex_value
    print(type(x))
    print(x)
    y = calc(x)

    #Ищем текстовое поле в которое внесем значение
    field_TF = browser.find_element(By.ID, 'answer')
    field_TF.send_keys(y)

    #Отмечаем checkbox "I'm the robot"
    field_CR = browser.find_element(By.ID, 'robotCheckbox')
    field_CR.click()

    #Выбираем radiobutton "Robots rule!"
    field_RR = browser.find_element(By.ID, 'robotsRule')
    field_RR.click()

    #Нажимаем на кнопку simbit
    field_BS = browser.find_element(By.CLASS_NAME, 'btn-default')
    field_BS.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()