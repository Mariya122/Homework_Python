from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.maximize_window()

driver.get('http://the-internet.herokuapp.com/login')

login = driver.find_element(By.ID, 'username')
login.send_keys('tomsmith')
password = driver.find_element(By.ID, 'password')
password.send_keys('SuperSecretPassword!', Keys.RETURN)



sleep(5)
driver.close()
