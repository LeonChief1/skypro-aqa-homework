# Задание 8. Форма авторизации

# Напишите скрипт.
# Шаги:

# Откройте страницу http://the-internet.herokuapp.com/login.
# В поле username введите значение 
# tomsmith
# .
# В поле password введите значение 
# SuperSecretPassword!
# .
# Нажмите кнопку 
# Login
# .

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
    
# Откройте страницу http://the-internet.herokuapp.com/login.
driver.get("http://the-internet.herokuapp.com/login")

# В поле username введите значение 
# tomsmith

username_locator = "input#username"

username_input = driver.find_element(By.CSS_SELECTOR, username_locator)

username_input.send_keys("tomsmith")

current_value = username_input.get_attribute("value")
print(f"Введено: {current_value}")

# В поле password введите значение 
# SuperSecretPassword!

password_locator = "input#password"

password_input = driver.find_element(By.CSS_SELECTOR, password_locator)

password_input.send_keys("SuperSecretPassword!")

current_value = password_input.get_attribute("value")
print(f"Введено: {current_value}")

# Нажмите кнопку 
# Login
try:
    button_locator = "button.radius"

    button_click = driver.find_element(By.CSS_SELECTOR, button_locator)

    ActionChains(driver) \
        .click(button_click) \
        .perform()
    print("Клик успешен")

except:
    
    print("Клик не успешен")

sleep(3)