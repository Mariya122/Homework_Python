
import time
import math
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from ExsampleClass import ExsampleClass
from Wait import Wait

def test_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    exsample = ExsampleClass(browser)
    get_time = exsample.set_timer('45')
    

    start_time = time.time()

    exsample.tap_button(0, 0, 1)

    waiter = Wait(browser)
    

    waiter.wait_result()

    stop_time = time.time()
    how_time = math.trunc(stop_time - start_time)
    how_long = exsample.long_time()
    

    assert str(how_time) == how_long


    browser.quit()


