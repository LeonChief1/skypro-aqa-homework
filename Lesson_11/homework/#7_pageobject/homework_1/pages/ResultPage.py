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

    @allure.step("Проверьте (assert), что поле Zip code подсвечено красным.")
    def get_alert_danger(self) -> str:
        '''
        Проверьте (assert), что поле Zip code подсвечено красным.
        '''
        WebDriverWait(self._driver, 40, 0.1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger, .alert-success")))

        # Проверьте (assert), что поле Zip code подсвечено красным.
        zip_code_field = self._driver.find_element(By.ID, "zip-code")
        result = zip_code_field.get_attribute("class")

        return result


    @allure.step("Проверьте (assert), что остальные поля подсвечены зеленым.")
    def get_alert_success(self) -> dict:
        '''
        Проверьте (assert), что остальные поля подсвечены зеленым.
        '''
        # Проверьте (assert), что остальные поля подсвечены зеленым.

        green_fields = [
                    "first-name", "last-name", "address", "e-mail", "phone",
                    "city", "country", "job-position", "company"
        ]

        results = {}
        for field_id in green_fields:
            field = self._driver.find_element(By.ID, field_id)
            results[field_id] = field.get_attribute("class")

        return results