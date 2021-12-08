from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time
driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/selects1.html')

number1 = driver.find_element_by_id("num1").text
number2 = driver.find_element_by_id("num2").text
suma = str(int(number1) + int(number2))
selects = Select(driver.find_element_by_tag_name("select"))
selects.select_by_value(suma)
button = driver.find_element_by_css_selector('button[type="submit"]').click()
time.sleep(30)
driver.quit()
