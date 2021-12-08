from selenium import webdriver
import math
import time
driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/math.html')


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_element = driver.find_element_by_id('input_value')
x = x_element.text
y = calc(x)
field = driver.find_element_by_id('answer')
field.send_keys(y)
box = driver.find_element_by_id('robotCheckbox').click()
radio = driver.find_element_by_id('robotsRule').click()
button = driver.find_element_by_css_selector('button[type="submit"]').click()
time.sleep(30)
driver.quit()
