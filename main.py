from selenium.webdriver.common.by import By
import selenium
from selenium import webdriver

driver = webdriver.Edge()

driver.get("https://www.kurs1.kz/city?name=astana")

currency_element = driver.find_elements(By.CLASS_NAME, "buy best_course")

for i in currency_element:
    print(f"Курс валюты: {currency_element.text}")

driver.quit()