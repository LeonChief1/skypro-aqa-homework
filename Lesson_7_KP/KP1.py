import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # driver.implicitly_wait(20)

    try:
        
        # Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/data-types.html.

        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # Заполните форму значениями:

        driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
        driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
        driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
        driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").send_keys("")
        driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
        driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
        driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
        driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
        driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
        driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")

        # Нажмите кнопку Submit.

        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Проверьте (assert), что поле Zip code подсвечено красным.

        WebDriverWait(driver, 40, 0.1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger, .alert-success")))

        zip_code_field = driver.find_element(By.ID, "zip-code")
        zip_code_classes = zip_code_field.get_attribute("class")
        assert "alert-danger" in zip_code_classes, "Поле Zip code должно быть подсвечено красным"

        # Проверьте (assert), что остальные поля подсвечены зеленым.

        green_fields = [
                    "first-name", "last-name", "address", "e-mail", "phone",
                    "city", "country", "job-position", "company"
        ]
        
        for field_id in green_fields:
            field = driver.find_element(By.ID, field_id)
            field_classes = field.get_attribute("class")
            assert "alert-success" in field_classes, f"Поле {field_id} должно быть подсвечено зеленым"

    finally:

        driver.quit()