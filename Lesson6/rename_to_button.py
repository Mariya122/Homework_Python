
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.implicitly_wait(40)

driver.get('http://uitestingplayground.com/textinput')

search_input = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
search_input.send_keys('SkyPro')
blue_button = driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()
result = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text
print(result)


driver.quit()