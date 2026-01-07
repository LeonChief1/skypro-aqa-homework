from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class ResultPage:
    def __init__(self, driver):
        '''
        Запускает driver chrome. (конструктор)
        '''
        self._driver = driver
    
    @allure.step("Ожидание результата на странице https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html со значением {number} в локаторе .screen.")
    def result_answer(self,number: str) -> str:
        '''
        Ожидание результата на странице https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html со значением 15 в локаторе .screen.
        '''
        WebDriverWait(self._driver, 46, 0.1).until(EC.text_to_be_present_in_element( (By.CSS_SELECTOR, ".screen"), number))

        result_element = self._driver.find_element(By.CSS_SELECTOR, ".screen").text

        return result_element

        # assert result_element == number, f"Получен результат {result_element}"