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


for press_blue_button in range(3):
    press_blue_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()


sleep(5)

driver.quit()
