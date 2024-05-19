
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class ExsampleClass:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    def set_timer(self, time):
        clear_timer = self._driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        new_times = self._driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(time)
    
        
    def tap_button(self, number_index_1, operator_index, number_index_2):
        numbers = self._driver.find_elements(By.CSS_SELECTOR, '.btn.btn-outline-primary')
        number_1 = numbers[number_index_1].click()
        operator = self._driver.find_elements(By.CSS_SELECTOR, '.operator.btn.btn-outline-success')
        operator_1 = operator[operator_index].click()
        number_2 = numbers[number_index_2].click()
        equals = self._driver.find_element(By.CSS_SELECTOR, '.btn.btn-outline-warning').click()

    def long_time(self):
        value = self._driver.find_element(By.CSS_SELECTOR, '#delay').get_attribute('value')
        return(value)

  
