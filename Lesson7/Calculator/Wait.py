from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Wait:
    def __init__(self, browser):
        self._driver = browser

    def wait_result(self):
        waiter = WebDriverWait(self._driver, 60)
        waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), '15'))
    

