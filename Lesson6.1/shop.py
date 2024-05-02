from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
waiter = WebDriverWait(driver, 50)


driver.get('https://www.saucedemo.com/')

login = driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
password = driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
user_button = driver.find_element(By.CSS_SELECTOR, '#login-button').click()

backpack = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
t_shirt = driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
onesie = driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()
basket = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()
checkout = driver.find_element(By.CSS_SELECTOR, '#checkout').click()

first_name = driver.find_element(By.ID, 'first-name').send_keys('Мария')
last_name = driver.find_element(By.ID, 'last-name').send_keys('Сорокина')
zip = driver.find_element(By.ID, 'postal-code').send_keys('617073')
press_continue = driver.find_element(By.ID, 'continue').click()

total = driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
print(total)


sleep(5)
driver.quit()