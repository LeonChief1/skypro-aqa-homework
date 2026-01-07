from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.MainPage import MainPage
from pages.SecondPage import SecondPage
from pages.CartPage import CartPage
from pages.ResultPage import ResultPage
import allure


@allure.story("Форма Валидации") 
@allure.feature("WRITE")
@allure.title("Проверка истоговой стоимости корзины c ожидаемой $58.29")
@allure.description("Используется аргумент --incognito")
@allure.severity("blocker")
def test_form_validation():

    chrome_options = Options() 
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)
    main_page = MainPage(driver)
    main_page.authorization("standard_user","secret_sauce")

    second_page = SecondPage(driver)
    second_page.buy()
    second_page.cart()

    cart_page = CartPage(driver)
    cart_page.checkout()
    cart_page.input_form("Mys","Mis","444111")
    cart_page.click_continue()

    result_page = ResultPage(driver)
    total_value = result_page.result_total()
    # Проверьте, что итоговая сумма равна $58.29.
    
    with allure.step("Сравнение сумму корзины с ожидаемым результатом"):
        assert total_value == "Total: $58.29", f"Ожидалась сумма $58.29, но получена {total_value}"
        
    print(f"Тест пройден! Итоговая сумма: {total_value}")
    
    driver.quit()