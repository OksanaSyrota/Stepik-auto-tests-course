from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/explicit_wait2.html')
test = WebDriverWait(driver, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100")
)
button = driver.find_element_by_id("book").click()
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_element = driver.find_element_by_id('input_value')
x = x_element.text
y = calc(x)
field = driver.find_element_by_id('answer')
field.send_keys(y)
button = driver.find_element_by_css_selector('button[type="submit"]')
button.click()
