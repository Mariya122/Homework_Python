from selenium.webdriver.common.by import By

class OvervPage:
    def __init__(self, browser):
        self._driver = browser

    def total(self):
        total = self._driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
        total_int = total.replace('Total: $', '')
        return(total_int)
    
    def price(self):
        prices = self._driver.find_elements(By.CSS_SELECTOR, '.inventory_item_price')
        if prices:
            price_text1 = prices[0].text
            price_text2 = prices[1].text
            price_text3 = prices[2].text
        
            let_price_text1 = price_text1.replace('$', '')
            let_price_text2 = price_text2.replace('$', '')
            let_price_text3 = price_text3.replace('$', '')
        
            let_price1 = float(let_price_text1)
            let_price2 = float(let_price_text2)
            let_price3 = float(let_price_text3)
        
            sum = let_price1 + let_price2 + let_price3
            return(sum)
        
            print(sum)
        else:
            print('цена не найдена')
    