from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self._driver = driver

    def checkout(self):
        # Нажмите Checkout.
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    def input_form(self,firstname,lastname,postalcode):
        # Заполните форму своими данными:
        # имя,
        # фамилия,
        # почтовый индекс.
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(firstname)
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(lastname)
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(postalcode)

    def click_continue(self):
        # Нажмите кнопку Continue
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()

    