from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ya.ru")

txt = driver.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').text

tag = driver.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').tag_name

id = driver.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').id

href = driver.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').get_attribute("href")

ff = driver.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').value_of_css_property("font-family")

print(txt)
print(tag)
print(id)
print(href)
print(ff)

driver.quit()