from selenium.webdriver.common.by import By
import allure


class SecondPage:

    def __init__(self, driver):
        '''
        Конструктор открытия драйвера Chrome.
        '''
        self._driver = driver

    @allure.step("Добавление в корзину товары")
    def buy(self) -> None:
        '''
        Добавление в корзину товары: 
        - Sauce Labs Backpack
        - Sauce Labs Bolt T-Shirt
        '''
        # Добавьте в корзину товары: Sauce Labs Backpack
        # Sauce Labs Bolt T-Shirt
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()

        # Sauce Labs Onesie
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    @allure.step("Нажатие на кнопку корзины")
    def cart(self) -> None:
        '''
        Нажатие на кнопку корзины
        '''
        # Перейдите в корзину.
        self._driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()