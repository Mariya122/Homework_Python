import time
import math
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


driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

def test_calculator():
    clear_seconds = driver.find_element(By.CSS_SELECTOR, '#delay').clear()
    new_seconds = driver.find_element(By.CSS_SELECTOR, '#delay').send_keys('5')
    numbers = driver.find_elements(By.CSS_SELECTOR, '.btn.btn-outline-primary')
    seven = numbers[0].click()
    operator = driver.find_elements(By.CSS_SELECTOR, '.operator.btn.btn-outline-success')
    plus = operator[0].click()
    numbers = driver.find_elements(By.CSS_SELECTOR, '.btn.btn-outline-primary')
    eight = numbers[1].click()
    equals = driver.find_element(By.CSS_SELECTOR, '.btn.btn-outline-warning').click()
    long_time = driver.find_element(By.CSS_SELECTOR, '#delay').get_attribute('value')
    start_time = time.time()
    result = driver.find_element(By.CSS_SELECTOR, '.screen')
    waiter.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), '15')
    )
    stop_time = time.time()
    how_time = (math.trunc(stop_time - start_time))
    print(type(long_time))
    print(type(how_time))
    

    assert str(how_time) == long_time



    
    driver.quit()
    