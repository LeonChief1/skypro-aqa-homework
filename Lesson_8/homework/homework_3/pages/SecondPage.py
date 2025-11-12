from selenium.webdriver.common.by import By


class SecondPage:

    def __init__(self, driver):
        self._driver = driver

    def buy(self):
        # Добавьте в корзину товары: Sauce Labs Backpack
        # Sauce Labs Bolt T-Shirt
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()

        # Sauce Labs Onesie
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    def cart(self):
        # Перейдите в корзину.
        self._driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()