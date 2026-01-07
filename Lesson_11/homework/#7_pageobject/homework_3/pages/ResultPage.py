from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class ResultPage:
    def __init__(self, driver):
        '''
        Конструктор открытия драйвера Chrome.
        '''
        self._driver = driver

    @allure.step("Получение со страницы итоговой стоимости (Total)")
    def result_total(self) -> str:
        '''
        Получение со страницы итоговую стоимость (Total).
        '''

        # Прочитайте со страницы итоговую стоимость (Total).

        Total = self._driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text

        return Total

        # # Проверьте, что итоговая сумма равна $58.29.
        
        # assert Total == "Total: $58.29", f"Ожидалась сумма $58.29, но получена {Total}"
        
        # print(f"Тест пройден! Итоговая сумма: {Total}")