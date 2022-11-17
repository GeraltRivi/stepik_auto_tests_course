import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter first name']").send_keys("Ganz")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']").send_keys("Muller")
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys("example@ex.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element(By.CSS_SELECTOR, "[accept='.txt']")
    element.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(20)
    browser.quit()