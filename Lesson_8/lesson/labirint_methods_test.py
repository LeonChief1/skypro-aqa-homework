from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


cookie = {"name": "cookie_policy", "value": "1"}


browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def open_labirint():
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)


def serch(term):
    browser.find_element(
        By.CSS_SELECTOR, "#search-field").send_keys(term)
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()


def add_books():
    buy_buttons = browser.find_elements(
        By.CSS_SELECTOR, "a._btn.btn-tocart.buy-link")

    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1

    return counter


def go_to_cart():
    # Переходим в корзину
    browser.get("https://www.labirint.ru/cart/")


def get_cart_counter():
    # Проверяем счетчик книг. Должен быть равен числу нажатий
    txt = browser.find_element(By.ID, 'basket-default-prod-count2').text
    txt = ''.join(filter(str.isdigit, txt))
    return int(txt)


def close_driver():
    # Закрываем браузер
    browser.quit()


def test_card_counter():
    open_labirint()
    serch('python')
    added  = add_books()
    go_to_cart()
    cart_counter = get_cart_counter()
    close_driver()
    assert added  == cart_counter


def test_empty_search():
    open_labirint()
    serch("no book search term")
    txt = browser.find_element(
        By.CSS_SELECTOR, "div.search-error").find_element(By.CSS_SELECTOR, 'h1').text
    assert txt == "Мы ничего не нашли по вашему запросу! Что делать?"
    close_driver()