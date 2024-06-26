from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.maximize_window()

driver.get('http://uitestingplayground.com/classattr')

sleep (5)

blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
blue_button.click()

alert = driver.switch_to.alert
alert.accept()

for _ in range(3):
    blue_button.click()
    alert = driver.switch_to.alert
    alert.accept()


sleep(5)

driver.quit()