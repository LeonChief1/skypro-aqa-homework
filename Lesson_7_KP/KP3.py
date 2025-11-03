import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():

    chrome_options = Options() 
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)
    driver.implicitly_wait(20)

    try:
        
        # Откройте сайт магазина: https://www.saucedemo.com/.

        driver.get("https://www.saucedemo.com/")

        # Авторизуйтесь как пользователь standard_user

        driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        driver.find_element(By.CSS_SELECTOR, "#login-button").click()

        # Добавьте в корзину товары: Sauce Labs Backpack
        # Sauce Labs Bolt T-Shirt
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()

        # Sauce Labs Onesie
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

        # Перейдите в корзину.

        driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()

        # Нажмите Checkout.

        driver.find_element(By.CSS_SELECTOR, "#checkout").click()
        
        # Заполните форму своими данными:
        # имя,
        # фамилия,
        # почтовый индекс.
        driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Mys")
        driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Mis")
        driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("444111")
        
        # Нажмите кнопку Continue.

        driver.find_element(By.CSS_SELECTOR, "#continue").click()
        
        # Прочитайте со страницы итоговую стоимость (Total).

        Total = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text

        # Проверьте, что итоговая сумма равна $58.29.
        
        assert Total == "Total: $58.29", f"Ожидалась сумма $58.29, но получена {Total}"
        
        print(f"Тест пройден! Итоговая сумма: {Total}")

    finally:
        
        driver.quit()