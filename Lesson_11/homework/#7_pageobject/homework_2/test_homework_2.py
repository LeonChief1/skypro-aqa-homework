from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.MainPage import MainPage
from pages.ResultPage import ResultPage
import allure

@allure.story("Форма Валидации") 
@allure.feature("WRITE")
@allure.title("Проверка получение результата от калькулятора через 45 секунд")
@allure.description("Нажатие кнопок на клавиатуре: 7 + 8 = ")
@allure.severity("blocker")
def test_form_validation():

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(driver)
    main_page.input_seconds("45")
    main_page.click_button()

    result_page = ResultPage(driver)
    result_element = result_page.result_answer("15")
    with allure.step("Сравнение результата калькулятора через 45 секунд."):
        assert result_element == "15", f"Получен результат {result_element}"

    driver.quit()