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
    driver.implicitly_wait(20)

    try:
        
        # Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html.

        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # В поле ввода по локатору #delay введите значение 45.
        driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

        # Нажмите на кнопки:
        # 7
        # +
        # 8
        # =
        
        buttons = driver.find_elements(By.CSS_SELECTOR, ".keys span")

        buttons[0].click()  # 7
        buttons[3].click()  # +
        buttons[1].click()  # 8  
        buttons[14].click() # =

        WebDriverWait(driver, 46, 0.1).until(EC.text_to_be_present_in_element( (By.CSS_SELECTOR, ".screen"), "15"))

        result_element = driver.find_element(By.CSS_SELECTOR, ".screen")

        assert result_element.text == "15", f"Получен результат {result_element.text}"

    finally:

        driver.quit()
