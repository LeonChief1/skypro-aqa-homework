from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ResultPage:
    def __init__(self, driver):
        self._driver = driver

    def get_alert_danger(self):
        WebDriverWait(self._driver, 40, 0.1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger, .alert-success")))

        # Проверьте (assert), что поле Zip code подсвечено красным.
        zip_code_field = self._driver.find_element(By.ID, "zip-code")
        zip_code_classes = zip_code_field.get_attribute("class")
        assert "alert-danger" in zip_code_classes, "Поле Zip code должно быть подсвечено красным"

    def get_alert_success(self):
        # Проверьте (assert), что остальные поля подсвечены зеленым.

        green_fields = [
                    "first-name", "last-name", "address", "e-mail", "phone",
                    "city", "country", "job-position", "company"
        ]
        
        for field_id in green_fields:
            field = self._driver.find_element(By.ID, field_id)
            field_classes = field.get_attribute("class")
            assert "alert-success" in field_classes, f"Поле {field_id} должно быть подсвечено зеленым"