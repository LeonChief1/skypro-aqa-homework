from selenium.webdriver.common.by import By
import allure

class MainPage:

    def __init__(self, driver):
        '''
        Конструкцтор открытия сайта https://www.saucedemo.com/; неявное ожидание 20 секунд; полный экран.
        '''
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(20)
        self._driver.maximize_window()

    @allure.step("Авторизация с параметрами {login}:{password}")
    def authorization(self,login: str,password: str) -> None:
        '''
        Авторизуйтесь как пользователь standard_user
        '''
        # Авторизуйтесь как пользователь standard_user
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(login)
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()