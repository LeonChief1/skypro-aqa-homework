# Задание 3. Клик по кнопке

# Напишите скрипт.
# Шаги:

# Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/.
# Пять раз кликните на кнопку 
# Add Element
# .
# Соберите со страницы список кнопок 
# Delete
# .
# Выведите на экран размер списка.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/.

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Пять раз кликните на кнопку 
# Add Element

button_locator = "button"

button_click = driver.find_element(By.CSS_SELECTOR, button_locator)

for click in range(5):
    clickable = driver.find_element(By.CSS_SELECTOR, button_click)
    ActionChains(driver) \
        .click(clickable) \
        .perform()
    sleep(0.3)
    
# Соберите со страницы список кнопок 
# Delete

deletes_block = "button.added-manually"

deletebutton = driver.find_elements(By.CSS_SELECTOR, deletes_block)


print(f"Найдено кнопок delete: {len(deletebutton)}")


driver.quit()