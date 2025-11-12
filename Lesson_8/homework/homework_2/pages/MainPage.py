from selenium.webdriver.common.by import By

class MainPage:

    def __init__(self, driver): 
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def input_seconds(self,seconds):
     # В поле ввода по локатору #delay введите значение 45.
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(seconds)


    def click_button(self):
            buttons = self._driver.find_elements(By.CSS_SELECTOR, ".keys span")

            buttons[0].click()  # 7
            buttons[3].click()  # +
            buttons[1].click()  # 8  
            buttons[14].click() # =

    