# Задание 7. Поле ввода

# Напишите скрипт.
# Шаги:

# Откройте страницу http://the-internet.herokuapp.com/inputs.
# Введите в поле текст 
# 1000
# .
# Очистите это поле (метод 
# clear
# ).
# Введите в это же поле текст 
# 999
# .

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
    
# Откройте страницу http://the-internet.herokuapp.com/inputs.
driver.get("http://the-internet.herokuapp.com/inputs")


# Введите в поле текст 
# 1000

search_locator = "input[type=number]"

search_input = driver.find_element(By.CSS_SELECTOR, search_locator)

search_input.send_keys("1000")

current_value = search_input.get_attribute("value")
print(f"Введено число: {current_value}")

sleep(1)

# Очистите это поле (метод 
# clear
search_input.clear()

current_value = search_input.get_attribute("value")
print(f"Введено число: {current_value}")

sleep(1)

# Введите в это же поле текст 
# 999

search_input.send_keys("999")

current_value = search_input.get_attribute("value")
print(f"Введено число: {current_value}")

sleep(1)
driver.quit()