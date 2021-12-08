from selenium import webdriver
import math

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/find_link_text")

d = str(math.ceil(math.pow(math.pi, math.e)*10000))
link1 = driver.find_element_by_link_text(d)
link1.click()
input1 = driver.find_element_by_name("first_name")
input1.send_keys("o")
input2 = driver.find_element_by_name("last_name")
input2.send_keys("s")
input3 = driver.find_element_by_class_name("city")
input3.send_keys("l")
input4 = driver.find_element_by_id("country")
input4.send_keys("u")
button = driver.find_elements_by_css_selector("button.btn")
button.click()

pass