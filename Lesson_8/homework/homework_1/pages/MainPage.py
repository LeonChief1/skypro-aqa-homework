from selenium.webdriver.common.by import By

class MainPage:

    def __init__(self, driver): 
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def filling_out_the_form(self,name,lastname,address,zipcode,city,country,email,phone,jobposition,company):
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

    def click(self):
        self._driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()