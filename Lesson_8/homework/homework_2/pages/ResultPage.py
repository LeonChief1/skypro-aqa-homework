from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ResultPage:
    def __init__(self, driver):
        self._driver = driver
    
    def result_answer(self,number):
        WebDriverWait(self._driver, 46, 0.1).until(EC.text_to_be_present_in_element( (By.CSS_SELECTOR, ".screen"), number))

        result_element = self._driver.find_element(By.CSS_SELECTOR, ".screen")

        assert result_element.text == number, f"Получен результат {result_element.text}"