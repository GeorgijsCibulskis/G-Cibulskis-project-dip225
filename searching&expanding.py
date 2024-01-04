from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)
time.sleep(1)

driver.get("https://www.nutritionvalue.org")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, 'input[value="Accept"]').click()

def search_for_product():
    while True:
        product_name = input("Please enter product's name: ")
        driver.find_element(By.ID, 'food_query').send_keys(product_name)
        driver.find_element(By.CSS_SELECTOR, 'input[value="Search"]').click()
        if validate_search():
            print("Please enter valid product's name (no such product found in databse)!")
            driver.find_element(By.ID, 'food_query').clear()
            continue
        break

def validate_search():
    try:
        check = driver.find_element(By.XPATH, "//p[text()='No matching foods found.']")
        return True

    except NoSuchElementException:
        return False

def choice_list():
    rows = driver.find_elements(By.XPATH, "//table[@class='full_width results zero']/tbody/tr")
    # FINISHED HERE!!! (NOT COMPLETED - CONTINUE NEXT TIME)
search_for_product()
    
time.sleep(10)
driver.close()

