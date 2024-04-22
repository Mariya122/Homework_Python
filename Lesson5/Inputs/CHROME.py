from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get('http://the-internet.herokuapp.com/inputs')

number = driver.find_element(By.CSS_SELECTOR, "[type=number]")
number.send_keys('1000')

sleep(2)

number.clear()
number.send_keys('999')



sleep(5)
