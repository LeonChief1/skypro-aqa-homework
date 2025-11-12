from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pages.MainPage import MainPage
from pages.ResultPage import ResultPage
from pages.CartPage import CartPage


def test_cart_counter(): 
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #Открываем браузер
    main_page = MainPage(browser) #Переменная хранит экземпляр класса MainPage
    main_page.set_cookie_policy() #Вызываем метод set_cookie_policy из MainPage
    main_page.serch('python') #Вызываем метод serch из MainPage

    result_page = ResultPage(browser)
    # result_page.switch_to_table()  #Используем только в видео
    to_be = result_page.add_books()

    cart_page = CartPage(browser)
    cart_page.get() #Переход на страницу с корзиной
    as_is = cart_page.get_counter() #Текущее значение счетчика на странице 

    assert as_is == to_be #Сравниваем значения счетчика с вернувшимся кол-вом книг
    browser.quit()


def test_empty_search():
    browser = webdriver.Chrome()
    main_page = MainPage(browser) 
    main_page.set_cookie_policy()
    main_page.serch("no book search term")

    result_page = ResultPage(browser)
    msg = result_page.get_empty_result_message()
    assert msg == "Мы ничего не нашли по вашему запросу! Что делать?"
    browser.quit()