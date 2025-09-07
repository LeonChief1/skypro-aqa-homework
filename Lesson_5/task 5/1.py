# Задание 5. Клик по кнопке с CSS-классом

# Напишите скрипт.
# Шаги:

# Откройте страницу http://uitestingplayground.com/classattr.
# Кликните на синюю кнопку.
# Запустите скрипт 3 раза подряд. Убедитесь, что он отработает одинаково.


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Запустите скрипт 3 раза подряд. Убедитесь, что он отработает одинаково.
for attempt in range(3):
    print(f"\n=== Попытка #{attempt + 1} ===")
    
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    
    try:
        # Откройте страницу http://uitestingplayground.com/classattr.

        driver.get("http://uitestingplayground.com/classattr")
        
        # Кликните на синюю кнопку.
        button_locator = "button.btn-primary"
        blue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, button_locator))
        )
        
        ActionChains(driver) \
            .click(blue_button) \
            .perform()
        
        print("Клик по синей кнопке выполнен успешно") 
        sleep(1)
        
    except:
        print("Ошибка")
    
    finally:
        driver.quit()
        sleep(1)