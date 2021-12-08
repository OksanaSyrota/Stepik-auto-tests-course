from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/find_xpath_form")
firstName = driver.find_element_by_name("first_name")
firstName.send_keys("O")
LN = driver.find_element_by_name("last_name")
LN.send_keys("S")
cit = driver.find_element_by_class_name("city")
cit.send_keys("L")
count = driver.find_element_by_id("country")
count.send_keys("Ukraine")
button = driver.find_element_by_xpath('/html/body/div/form/div[6]/button[3]')
button.click()
time.sleep(30)
driver.quit()

