from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, browser):
        self._driver = browser

    def get_cart(self):
        basket = self._driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()
        checkout = self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()