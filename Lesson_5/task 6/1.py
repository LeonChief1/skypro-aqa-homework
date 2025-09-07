# Задание 6. Модальное окно

# Напишите скрипт.
# Шаги:

# Откройте страницу http://the-internet.herokuapp.com/entry_ad.
# В модальном окне нажмите на кнопку 
# Сlose
# .

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
    
# Откройте страницу http://the-internet.herokuapp.com/entry_ad.
driver.get("http://the-internet.herokuapp.com/entry_ad")

# В модальном окне нажмите на кнопку 
# Сlose
try:
    modal = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.modal")))
    print("Модальное окно найдено")
    
    close_button = modal.find_element(By.XPATH, ".//p[text()='Close']")
    close_button.click()
    print("Клик выполнен")
    
    WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.modal")))
    print("Модальное окно успешно закрыто")
    
except:
    print("Ошибка")

finally:
    sleep(2)
    driver.quit()