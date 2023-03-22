import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_value = (browser.find_element(By.ID, "input_value")).text
    x = calc(x_value)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(x)

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()