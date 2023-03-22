from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

def sum_value(x, y):
    return str(int(x) + int(y))

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = (browser.find_element(By.ID, "num1")).text
    y = (browser.find_element(By.ID, "num2")).text

    sum_answer = sum_value(x, y)

    dropdown = browser.find_element(By.ID, "dropdown")
    dropdown.click()

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum_answer)

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
