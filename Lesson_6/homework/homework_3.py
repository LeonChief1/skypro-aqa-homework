# Шаги:

# Перейдите на сайт: https://bonigarcia.dev/selenium-webdriver-java/loading-images.html.
# Дождитесь загрузки всех картинок.
# Получите значение атрибута 
# src
#  у 3-й картинки.
# Выведите значение в консоль.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
waiter = WebDriverWait(driver, 40, 0.1)

# Перейдите на сайт: https://bonigarcia.dev/selenium-webdriver-java/loading-images.html.

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Получите значение атрибута 
# src
#  у 3-й картинки.

waiter.until(
    EC.text_to_be_present_in_element( (By.CSS_SELECTOR, "#text"), "Done")
)

images = driver.find_elements(By.CSS_SELECTOR, "img")
third_image_src = images[3].get_attribute("src")

# Выведите значение в консоль.

print(third_image_src)

driver.quit()