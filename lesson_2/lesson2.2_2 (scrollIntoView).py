import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_value = (browser.find_element(By.ID, "input_value")).text
    x_total = calc(x_value)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(x_total)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radio = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    submit = browser.find_element(By.CLASS_NAME, "btn")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()







