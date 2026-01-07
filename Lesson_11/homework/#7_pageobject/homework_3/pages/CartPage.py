from selenium.webdriver.common.by import By
import allure

class CartPage:
    def __init__(self, driver):
        '''
        Конструктор открытия драйвера Chrome.
        '''
        self._driver = driver

    @allure.step("Нажатие на кнопку Checkout")
    def checkout(self) -> None:
        """
        Нажатие на кнопку Checkout
        """
        # Нажмите Checkout.
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    @allure.step("Заполнение формы {firstname}:{lastname}:{postalcode}")
    def input_form(self,firstname: str,lastname: str,postalcode: str) -> None:
        '''
        Заполнение формы:
        - имя
        - фамилия
        - почтовый индекс
        '''
        # Заполните форму своими данными:
        # имя,
        # фамилия,
        # почтовый индекс.
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(firstname)
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(lastname)
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(postalcode)

    @allure.step("Нажатие на кнопку Continue")
    def click_continue(self) -> None:
        """
        Нажатие на кнопку Continue
        """
        # Нажмите кнопку Continue
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()

    