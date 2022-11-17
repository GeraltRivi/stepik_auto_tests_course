import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def sum(x, y):
  return str(int(x)+int(y))

try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "[id='num1']")
    x = x_element.text
    y_element = browser.find_element(By.CSS_SELECTOR, "[id='num2']")
    y = y_element.text
    z = sum(x, y)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(z))

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(20)
    browser.quit()