from selenium import webdriver
import time
import math
driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/alert_accept.html')

button = driver.find_element_by_css_selector('button[type="submit"]').click()
alert = driver.switch_to.alert.accept()
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_element = driver.find_element_by_id('input_value')
x = x_element.text
y = calc(x)
field = driver.find_element_by_id('answer')
field.send_keys(y)
button = driver.find_element_by_css_selector('button[type="submit"]').click()
time.sleep(20)
driver.quit()