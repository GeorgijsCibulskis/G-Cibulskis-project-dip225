import time
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from fitness_plan_creating import start_driver


def consent(driver):
    driver.find_element(By.CSS_SELECTOR, 'input[value="Accept"]').click()


def search_for_product(driver, textbox, product_name, progressbar):
        # Lietotājs ievada kādu produktu un tad programma to ievada meklēšana laukā
        driver.find_element(By.CSS_SELECTOR, "a[onclick='toggleSearchBox();return false;']").click()
        driver.find_element(By.ID, 'search-box').send_keys(product_name)
        driver.find_element(By.ID, 'search-box').send_keys(Keys.ENTER)
        
        # Pārbaudam vai produkts eksistē vietnē
        if validate_search(driver):
            progressbar.pack_forget()
            messagebox.showerror("Search Error", "Invalid input. No such product has been found")
        else:
            # Atrodam pogu '40', kura uzreiz radīs 40 populārakus un piemērotākus produktus pēc meklēšanas
            page_expansion = driver.find_element(By.CSS_SELECTOR, "a[title='40 results per page']")
            driver.execute_script("arguments[0].scrollIntoView();", page_expansion)
            page_expansion.click()
            time.sleep(2)

            # Kad produkti tika atrasti, tad mēs papildinām teksta kasti ar visiem iespējamām izvēles variantiem
            cells = driver.find_elements(By.CSS_SELECTOR, "td.left")
            text_from_cells = [cell.text for cell in cells]

            # Izlaižam pirmo tabulas rindu, jo tas vienmēr ir tabulas 'heading'
            text_from_cells = text_from_cells[1::]

            for food in text_from_cells:
                textbox.insert('end', f"- {food}\n")
            progressbar.pack_forget()

# Šī funkcija pārbauda vai tīmekļa lapā ir paragrafs, ar tekstu 'No matching foods found.'. Ja tāds ir, tad tas produkts, kuru ievādīja lietotājs ir nepareizs vai neeksistē vietnē
def validate_search(driver):
    try:
        check = driver.find_element(By.XPATH, "//table[@id='main']/tbody//tr/td/p[text()='No matching foods found.']")
        return True

    except NoSuchElementException:
        return False

def main(textbox, product_name, progressbar):
    driver = start_driver()
    driver.get("https://www.nutritionvalue.org")
    time.sleep(2)

    consent(driver)

    search_for_product(driver, textbox, product_name, progressbar)
    driver.close()

if __name__ == "__main__":
    main()