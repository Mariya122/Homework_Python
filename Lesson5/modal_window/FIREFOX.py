from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.maximize_window()

driver.get('https://the-internet.herokuapp.com/entry_ad')


close = driver.find_element(By.CSS_SELECTOR, '.modal-footer').click

sleep(5)
driver.close()