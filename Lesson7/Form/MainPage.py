from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class MainForm:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    def add_value(self, first_name, last_name, address, zip_code, email, phone_number, city, country, job, company):
        self._driver.find_element(By.CSS_SELECTOR, '[name=first-name]').send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR, '[name=last-name]').send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, '[name=address]').send_keys(address)
        self._driver.find_element(By.CSS_SELECTOR, '[name=zip-code]').send_keys(zip_code)
        self._driver.find_element(By.CSS_SELECTOR, '[name=e-mail]').send_keys(email)
        self._driver.find_element(By.CSS_SELECTOR, '[name=phone]').send_keys(phone_number)
        self._driver.find_element(By.CSS_SELECTOR, '[name=city]').send_keys(city)
        self._driver.find_element(By.CSS_SELECTOR, '[name=country]').send_keys(country)
        self._driver.find_element(By.CSS_SELECTOR, '[name=job-position]').send_keys(job)
        self._driver.find_element(By.CSS_SELECTOR, '[name=company]').send_keys(company)
        self._driver.find_element(By.CSS_SELECTOR, 'button').click()

    



    