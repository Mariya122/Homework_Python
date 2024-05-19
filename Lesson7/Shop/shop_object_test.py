
import time
import math
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from LogPage import LogPage
from ProductPage import ProductPage
from CartPage import CartPage
from InformationPage import InformationPage
from OverviewPage import OvervPage

def test_shop():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    login = LogPage(browser)

    autorizate = login.authorization()

    prod = ProductPage(browser)
    add_product = prod.add_poduct()

    cart = CartPage(browser)
    get_cart = cart.get_cart()

    information = InformationPage(browser)
    add_info = information.add_information('Мария', 'Сорокина', '617073')

    overview = OvervPage(browser)
    total = overview.total()
    price = overview.price()

    print(total)
    print(price)

    assert total == price    


    browser.quit()