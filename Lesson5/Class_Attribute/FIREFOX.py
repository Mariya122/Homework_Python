from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.maximize_window()

driver.get('http://uitestingplayground.com/classattr')


for press_blue_button in range(3):
    press_blue_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()


sleep(5)

driver.quit()