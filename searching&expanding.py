from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

driver.get("https://www.nutritionvalue.org")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, 'input[value="Accept"]').click()
time.sleep(1)

def search_for_product():
    # Lietotājs ievada kādu productu un tad programma to ievada meklēšana laukā
    while True:
        product_name = input("Please enter product's name: ")
        driver.find_element(By.CSS_SELECTOR, "a[onclick='toggleSearchBox();return false;']").click()
        driver.find_element(By.ID, 'search-box').send_keys(product_name)
        driver.find_element(By.ID, 'search-box').send_keys(Keys.ENTER)
        # Pārbaudam vai produkts eksistē vietnē
        if validate_search():
            print("Please enter valid product's name (no such product found in databse)!")
            continue
        break

# Šī funkcija pārbauda vai tīmekļa lapā ir paragrafs, ar tekstu 'No matching foods found.'. Ja tāds ir, tad tas produkts, kuru ievādīja lietotājs ir nepareizs vai neeksistē vietnē
def validate_search():
    try:
        check = driver.find_element(By.XPATH, "//p[text()='No matching foods found.']")
        return True

    except NoSuchElementException:
        return False

def choice_list():
    # Šajā vietā ērti lietot CSS_SELECTOR XPATH vietā, jo katrai šūnai ir klase 'left'
    # Tātad programma atrod visas tabulas rindas un nokopē no tiem tekstu, kas principā ir garš saraksts ar ēdienu nosaukumiem, kuri tika atrasti pēc lietotāja ievādīta vārda
    cells = driver.find_elements(By.CSS_SELECTOR, "td.left")
    text_from_cells = [cell.text for cell in cells]
    text_from_cells = text_from_cells[1::]
    # Izvadam visus produktus
    print(f"Here is the list of food, which is connected with your choice: ")
    for food in text_from_cells:
        print(food)
    while True:
        # Lietotājs var izvēlēties no saraksta kādu konkrēto ēdienu
        next_step = input("If you want to choose something from the list, just write it, if you want to end search, write 'The end': ").capitalize()
        if next_step == 'The end':
            return
        elif next_step != 'The end' and next_step in text_from_cells:
            # Jā tāds produkts ir sarakstā, tad uzspipiežam uz to
            true_product = driver.find_element(By.CSS_SELECTOR, f'a[title="{next_step}"]')
            driver.execute_script("arguments[0].scrollIntoView();", true_product)
            true_product.click()
            time.sleep(2)
            # Ar kalorijām viss ir ērti - vietnē tiem ir atsevišķa ID
            calories = float(driver.find_element(By.ID, 'calories').text)
            # Ar taukiem un ogļhidrātiem jau ir sarežģītāk - vajadzēja atrast tabulu un tad konkrēto pēc kārtas rindu un no tās dabūt tekstu un to apstrādāt līdz float vērtībai
            fat_full_text = driver.find_element(By.XPATH, "//table[@class='center zero']/tbody/tr[10]").text
            fat = (fat_full_text.split(" "))[2][:-1]
            fat = float(fat)
            carbs_full_text = driver.find_element(By.XPATH, "//table[@class='center zero']/tbody/tr[18]").text
            carbs = (carbs_full_text.split(" "))[2][:-1]
            carbs = float(carbs)
            # Ar olbaltumvielām viss ir ļoti sarežģīti, jo dažiem produktiem to rinda tabulā mainās un šūnai ir klase 'left', kura ir arī visām pārējam šūnām, tāpēc pēc klases mēklēt nevar
            # Tad izlēmu mēklēt peč <b> elementa, kurā ir rakstīt 'Protein', taču no tā es nevaru dabūt olbaltumvielu daudzumu ar metodi .text, jo tā atgriež tekstu no <b> elementa, kas ir
            # 'Protein', tāpēc mēklēju to <b> elementu, tad no to meklēju vecāka šūnu (parent td element) un tad jau no tās šūna (td) ieguvu tekstu ar olbaltumvielu daudzumu
            protein_b_element = driver.find_element(By.XPATH, "//b[text()='Protein']")
            protein_parent_td_element = protein_b_element.find_element(By.XPATH, "./parent::td")
            protein = protein_parent_td_element.text.split(" ")[1][:-1]
            protein = float(protein)
            print(calories, carbs, protein, fat)

search_for_product()
choice_list()
driver.close()