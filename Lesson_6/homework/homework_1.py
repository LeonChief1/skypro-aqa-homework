# Шаги:

# Перейдите на страницу http://uitestingplayground.com/ajax.
# Нажмите на синюю кнопку.
# Получите текст из зеленой плашки.
# Выведите его в консоль (”Data loaded with AJAX get request.”).

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20)


# Перейдите на страницу http://uitestingplayground.com/ajax.

driver.get("http://uitestingplayground.com/ajax")

# Нажмите на синюю кнопку.

driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

# Получите текст из зеленой плашки.

content = driver.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text


# Выведите его в консоль (”Data loaded with AJAX get request.”).
print(txt)

driver.quit()