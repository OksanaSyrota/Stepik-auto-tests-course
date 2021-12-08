from selenium import webdriver
import time
import os
driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/file_input.html')

Name = driver.find_element_by_name('firstname').send_keys('o')
last = driver.find_element_by_name('lastname').send_keys('s')
email = driver.find_element_by_name('email').send_keys('t')
choose_file = driver.find_element_by_id('file').send_keys("C:/Users/User/PycharmProjects/lesson2_1.txt")
button = driver.find_element_by_css_selector('button[type="submit"]').click()
time.sleep(20)
driver.quit()
