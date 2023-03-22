from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CLASS_NAME, "first_block .first")
    input1.send_keys("Lika")
    input2 = browser.find_element(By.CLASS_NAME, "first_block .second")
    input2.send_keys("Kasimova")
    input3 = browser.find_element(By.CLASS_NAME, "first_block .third")
    input3.send_keys("test@yandex.ru")
    input4 = browser.find_element(By.CLASS_NAME, "second_block .first")
    input4.send_keys("test@yandex.ru")
    input5 = browser.find_element(By.CLASS_NAME, "second_block .second")
    input5.send_keys("test@yandex.ru")


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()