
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.implicitly_wait(40)

driver.get('http://uitestingplayground.com/ajax')

button = driver.find_element(By.CSS_SELECTOR, '#ajaxButton'). click()

content = driver.find_element(By.CSS_SELECTOR, '#content')
txt = content.find_element(By.CSS_SELECTOR, '.bg-success').text
print(txt)
driver.quit()