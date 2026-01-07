from selenium.webdriver.common.by import By
import allure

class MainPage:

    def __init__(self, driver):
        '''
        Конструктор driver.
        1. Открывает страницу https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
        2. Неявное ожидание (4 секунды)
        3. Открывает страницу на весь экран
        '''
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Указывает {seconds} в поле ввода по локатору #delay на странице https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    def input_seconds(self, seconds: str) -> None:
        '''
        Указывает время в поле ввода по локатору #delay на странице https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
        '''
     # В поле ввода по локатору #delay введите значение 45.
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(seconds)

    @allure.step("Выполняем нажатие на кнопки клавиатуры")
    def click_button(self) -> None:
            '''
            Выполняет нажатие по кнопкам клавиатуры на странице https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
            - 7
            - +
            - 8
            - =
            '''
            buttons = self._driver.find_elements(By.CSS_SELECTOR, ".keys span")

            buttons[0].click()  # 7
            buttons[3].click()  # +
            buttons[1].click()  # 8  
            buttons[14].click() # =

    