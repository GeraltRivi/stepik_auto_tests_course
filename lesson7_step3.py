from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input1.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']").click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
  
finally:
    time.sleep(20)
    browser.quit()