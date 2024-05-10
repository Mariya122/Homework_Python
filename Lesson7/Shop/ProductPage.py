from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, browser):
        self._driver = browser

    def add_poduct(self):
        backpack = self._driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
        t_shirt = self._driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
        onesie = self._driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()
    
    