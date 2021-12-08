from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/math.html')
people_radio = driver.find_element_by_id("peopleRule")
people_checked = people_radio.get_attribute("checked")
print(people_checked)

