from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

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
