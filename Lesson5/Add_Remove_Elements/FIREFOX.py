# For Firefox
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.maximize_window()

driver.get('http://the-internet.herokuapp.com/add_remove_elements/')

for press_button in range (5):
    press_button = driver.find_element(By.CSS_SELECTOR, "button").click()

element = driver.find_element(By.CSS_SELECTOR, "#elements")
elements = element.find_elements(By.CSS_SELECTOR, ".added-manually")

for e in elements:
    print(e.text)


sleep(5)
driver.close()



print(len(elements))



