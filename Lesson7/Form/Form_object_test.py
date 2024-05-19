
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color

from MainPage import MainForm
from ResultColor import ResultColor

def test_form():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    main = MainForm(browser)
    main.add_value('Иван', 'Петров', 'Ленина, 55-3', '', 'test@skypro.com', '+7985899998787', 'Москва', 'Россия', 'QA', 'SkyPro')

    colour = ResultColor(browser)
    green = colour.green_colour()
    red = colour.red_colour()
    
    assert str(green) == 'Color: ' + 'rgba(209, 231, 221, 1)'
    assert str(red) == 'Color: ' + 'rgba(248, 215, 218, 1)'


    

    browser.quit()

