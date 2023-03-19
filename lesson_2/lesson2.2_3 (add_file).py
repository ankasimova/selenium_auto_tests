from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Lika")

    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Kasimova")

    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("test@1cb.kz")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'text_file_lesson2.2')

    attach_file = browser.find_element(By.CSS_SELECTOR, "[type = 'file']")
    attach_file.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()