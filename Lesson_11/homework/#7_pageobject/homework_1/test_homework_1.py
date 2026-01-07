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
@allure.title("Проверка полей на их состояние")
@allure.description("Заполнение формы с параметрами")
@allure.severity("blocker")
def test_form_validation():

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(driver)
    main_page.filling_out_the_form("Иван","Петров","Ленина, 55-3","","Москва","Россия","test@skypro.com","+7985899998787","QA","SkyPro")
    main_page.click()

    result_page = ResultPage(driver)
    get_alert_dangert = result_page.get_alert_danger()
    assert "alert-danger" in get_alert_dangert, "Поле Zip code должно быть подсвечено красным"
    

    get_alert_success = result_page.get_alert_success()
    for field_id, field_class in get_alert_success.items():
        assert "alert-success" in field_class, f"Поле {field_id} должно быть подсвечено зеленым"

    driver.quit()