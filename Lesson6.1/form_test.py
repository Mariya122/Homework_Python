from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()


driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

def test_form():
    first_name = driver.find_element(By.CSS_SELECTOR, '[name=first-name]').send_keys('Иван')
    last_name = driver.find_element(By.CSS_SELECTOR, '[name=last-name]').send_keys('Петров')
    address = driver.find_element(By.CSS_SELECTOR, '[name=address]').send_keys('Ленина, 55-3')
    email = driver.find_element(By.CSS_SELECTOR, '[name=e-mail]').send_keys('test@skypro.com')
    phone_number = driver.find_element(By.CSS_SELECTOR, '[name=phone]').send_keys('+7985899998787')
    city = driver.find_element(By.CSS_SELECTOR, '[name=city]').send_keys('Москва')
    country = driver.find_element(By.CSS_SELECTOR, '[name=country]').send_keys('Россия')
    job = driver.find_element(By.CSS_SELECTOR, '[name=job-position]').send_keys('QA')
    company = driver.find_element(By.CSS_SELECTOR, '[name=company]').send_keys('SkyPro')
    button = driver.find_element(By.CSS_SELECTOR, 'button').click()

def test_color():
    green = driver.find_elements(By.CSS_SELECTOR, '.alert.py-2.alert-success')
    success = Color.from_string(green[0].value_of_css_property('background-color'))

    red = driver.find_elements(By.CSS_SELECTOR, '.alert.py-2.alert-danger')
    danger = Color.from_string(red[0].value_of_css_property('background-color'))


    assert str(success) == 'Color: ' + 'rgba(209, 231, 221, 1)'
    assert str(danger) == 'Color: ' + 'rgba(248, 215, 218, 1)'

    sleep(5)

    driver.quit()