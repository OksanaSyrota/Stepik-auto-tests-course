from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/simple_form_find_task.html")

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
driver.quit()