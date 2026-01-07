from selenium.webdriver.common.by import By
import allure

class MainPage:

    def __init__(self, driver):
        '''
        Конструктор driver.
        1. Открывает страницу https://bonigarcia.dev/selenium-webdriver-java/data-types.html
        2. Неявное ожидание (4 секунды)
        3. Открывает страницу на весь экран
        '''
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Поиск локаторов, заполнение полей {name}:{lastname}:{address}:{zipcode}:{city}:{country}:{email}:{phone}:{jobposition}:{company}")
    def filling_out_the_form(self,name: str,lastname: str,address: str,zipcode: str,city: str,country: str,email: str,phone: str,jobposition: str,company: str) -> None:
        '''
        1. Поиск локаторов
        2. Заполнение полей
        '''
        self._driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys(name)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys(lastname)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys(address)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").send_keys(zipcode)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys(city)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys(country)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys(email)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys(phone)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys(jobposition)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys(company)

    @allure.step("Нажатие на кнопку")
    def click(self) -> None:
        '''
        Нажатие на кнопку
        '''
        self._driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()