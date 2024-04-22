# For Chrome

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get('http://the-internet.herokuapp.com/add_remove_elements/')

for press_button in range (5):
    press_button = driver.find_element(By.CSS_SELECTOR, "button").click()

element = driver.find_element(By.CSS_SELECTOR, "#elements")
elements = element.find_elements(By.CSS_SELECTOR, ".added-manually")

for e in elements:
    print(e.text)



print(len(elements))


sleep(5)

