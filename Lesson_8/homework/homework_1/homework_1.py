from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.MainPage import MainPage
from pages.ResultPage import ResultPage


def test_form_validation():

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(driver)
    main_page.filling_out_the_form("Иван","Петров","Ленина, 55-3","","Москва","Россия","test@skypro.com","+7985899998787","QA","SkyPro")
    main_page.click()

    result_page = ResultPage(driver)
    result_page.get_alert_danger()
    result_page.get_alert_success()

    driver.quit()