from selenium import webdriver
import time

try:
    driver = webdriver.Chrome()
    driver.get('http://suninjuly.github.io/registration2.html')
    input1 = driver.find_element_by_class_name('first')
    input1.send_keys("Oksana")
    input2 = driver.find_element_by_css_selector('input[placeholder="Input your last name"]')
    input2.send_keys("Syrota")
    input3 = driver.find_element_by_class_name('third')
    input3.send_keys("test@test.test")
    button = driver.find_element_by_css_selector('button[type="submit"]')
    button.click()
    time.sleep(5)
    welcome_text_elt = driver.find_element_by_tag_name('h1')
    welcome_text = welcome_text_elt.text #welcome_text надаємо значення попереднього елементу
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(15)
    driver.quit()


