from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.maximize_window()

driver.get('http://the-internet.herokuapp.com/inputs')

number = driver.find_element(By.CSS_SELECTOR, "[type=number]")
number.send_keys('1000')

sleep(2)

number.clear()
number.send_keys('999')



sleep(5)
driver.close()