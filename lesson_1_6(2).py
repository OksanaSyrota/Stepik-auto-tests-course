from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
import time

try:
    browser.get('http://suninjuly.github.io/simple_form_find_task.html')
    input1 = browser.find_element(By.TAG_NAME, 'input').send_keys('O')
    input2 = browser.find_element(By.NAME, 'last_name').send_keys('S')
    input3 = browser.find_element(By.CLASS_NAME, 'city').send_keys('L')
    input4 = browser.find_element(By.ID, 'country').send_keys('U')
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    time.sleep(10)
    browser.quit()
