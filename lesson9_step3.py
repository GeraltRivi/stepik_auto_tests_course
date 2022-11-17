import time

import confirm as confirm
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button").click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "[id='answer']").send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(20)
    browser.quit()