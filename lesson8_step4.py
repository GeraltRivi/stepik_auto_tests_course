import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "[id='answer']").send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']").click()
    browser.execute_script("window.scrollBy(0, 100)")
    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("window.scrollBy(0, 150)")
    button.click()

finally:
    time.sleep(20)
    browser.quit()