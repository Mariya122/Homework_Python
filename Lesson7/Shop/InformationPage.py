from selenium.webdriver.common.by import By

class InformationPage:
    def __init__(self, browser):
        self._driver = browser

    def add_information(self, first_name, last_name, zip_code):
        first_name = self._driver.find_element(By.ID, 'first-name').send_keys(first_name)
        last_name = self._driver.find_element(By.ID, 'last-name').send_keys(last_name)
        zip = self._driver.find_element(By.ID, 'postal-code').send_keys(zip_code)
        press_continue = self._driver.find_element(By.ID, 'continue').click()