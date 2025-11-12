from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, browser):
        self.driver = browser

    def get(self):
        self.driver.get("https://www.labirint.ru/cart/")

    def get_counter(self):
        txt = self.driver.find_element(By.ID, 'basket-default-prod-count2').text
        txt = ''.join(filter(str.isdigit, txt))
        return int(txt)