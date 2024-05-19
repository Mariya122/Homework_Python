from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color

class ResultColor:
    def __init__(self, browser):
        self._driver = browser

    def green_colour(self):
        green = self._driver.find_elements(By.CSS_SELECTOR, '.alert.py-2.alert-success')
        if green:
            success = Color.from_string(green[0].value_of_css_property('background-color'))
            return(success)
    
    def red_colour(self):
        red = self._driver.find_elements(By.CSS_SELECTOR, '.alert.py-2.alert-danger')
        if red:
            danger = Color.from_string(red[0].value_of_css_property('background-color'))
            return(danger)
            