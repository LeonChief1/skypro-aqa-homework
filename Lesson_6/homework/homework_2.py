# Шаги:

# Перейдите на сайт: http://uitestingplayground.com/textinput.
# Укажите в поле ввода текст SkyPro.
# Нажмите на синюю кнопку.
# Получите текст кнопки и выведите в консоль (“SkyPro”).


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20)


# Перейдите на сайт: http://uitestingplayground.com/textinput.

driver.get("http://uitestingplayground.com/textinput")

# Укажите в поле ввода текст SkyPro.

driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")

# Нажмите на синюю кнопку.

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

# Получите текст кнопки и выведите в консоль (“SkyPro”).

txt = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

print(txt)

driver.quit()