from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

# Atvert vietni
driver.get("https://www.prokerala.com/health/health-calculators/weight-gain-calculator.php")
time.sleep(2)

# Uzspiežam uz pogas "consent", lai piekristu cookie un personīgo datu apstrādei
consent_button = driver.find_element(By.CLASS_NAME, 'fc-cta-consent')
consent_button.click()

# Funkcija, kura izvēlas lietotāja dzimumu un pārbauda uzreiz ievades kļūdas
def select_gender():
    while True:
        gender = input("Are you male or female? ")
        if gender.lower() == 'male':
            # Selenium meklē elementu "Input", kura vērtība ir "male" vai "female" (tīmekļa vietnes kodā tas elements "input" ir klases "radio", kas principā ir poga, uz kuru var uzklikšķināt)
            driver.find_element(By.CSS_SELECTOR, 'input[value="male"]').click()
            break
        elif gender.lower() == 'female':
            driver.find_element(By.CSS_SELECTOR, 'input[value="female"]').click()
            break
        else:
            print("Invalid gender input. Please choose 'male' or 'female'.")
            continue
    return gender

def select_meal_count():
    while True:
        meal_count = input("Enter how many times do you eat during the day (3-6): ")
        if (meal_count.isnumeric() == False) or int(meal_count) < 3 or int(meal_count) > 6:
            print("Invalid meals count. Please enter valid number.")
            continue
        else:
            # Tā kā tīmekļa lapa ir pārāk gara, un programma nevarēs redzēt atbilstošus laukus, mums ir nepieciešams pārvietot lapu uz leju līdz tam brīdim, kad būs redzama atbilstoša poga
            meal_count_element = driver.find_element(By.CSS_SELECTOR, f'input[value="{meal_count}"]')
            driver.execute_script("arguments[0].scrollIntoView();", meal_count_element)
            meal_count_element.click()
            break
    return meal_count
# Funkcijas, lai paŗbaudītu pareizu lietotāja ievādi
def validate_age(age):
    if (age.isnumeric() == False) or int(age) < 0 or int(age) > 150:
        print("Invalid age. Please enter a valid age.")
        return False
    return True

def validate_weight(weight):
    if (weight.isnumeric() == False) or int(weight) < 0 or int(weight) > 250:
        print("Invalid age. Please enter a valid age.")
        return False
    return True

def validate_height(height):
    if (height.isnumeric() == False) or int(height) < 0 or int(height) > 250:
        print("Invalid age. Please enter a valid age.")
        return False
    return True

def validate_time_span(time_span):
    valid_time = ['1 week', '2 weeks', '3 weeks', '1 month', '2 months', '3 months', '4 months', '5 months', '6 months', '1 year']
    if time_span not in valid_time:
        print("Invalid time span. Please choose a valid activity level.")
        return False
    return True

def validate_exercise_mode(exercise_mode):
    valid_levels = ['Sedentary', 'Light', 'Moderate', 'Very active', 'Extreme']
    if exercise_mode not in valid_levels:
        print("Invalid activity level. Please choose a valid activity level.")
        return False
    return True


def get_info():
    # Informāciajs ievāde ar pārbaudēm
    gender = select_gender()


    age = input("Enter your age: ")
    while not validate_age(age):
        age = input("Enter your age: ")
    

    height = input("Enter your height (in cm): ")
    while not validate_height(height):
        height = input("Enter your age: ")
    

    weight = input("Enter your weight (in kg): ")
    while not validate_weight(weight):
        weight = input("Enter your age: ")
    

    goal_weight = input("Enter your goal weight (in kg): ")
    while not validate_weight(goal_weight):
        goal_weight = input("Enter your goal_weight: ")


    time_span = input("Enter time span, during which you wnat to achieve your goal: ")
    while not validate_time_span(time_span):
        time_span = input("Enter time span, during which you wnat to achieve your goal: ")


    exercise_mode = input("Enter your exercise mode (Available: Sedentary, Light, Moderate, Very active, Extreme): ")
    while not validate_exercise_mode(exercise_mode):
        exercise_mode = input("Enter your exercise mode: ")

    meal_count = select_meal_count()

    # Meklējām atbilsotšus logus, kur ierakstīt nepieciešamu informāciju par lietotāju 
    driver.find_element(By.ID, 'fin_age').send_keys(age)
    driver.find_element(By.ID, 'fin_height_cm').send_keys(height)
    driver.find_element(By.ID, 'fin_curr_weight_kg').send_keys(weight)
    driver.find_element(By.ID, 'fin_goal_weight_kg').send_keys(goal_weight)

    time_span_dropdown = Select(driver.find_element(By.ID, 'fin_goal_span'))
    time_span_dropdown.select_by_visible_text(time_span)

    # Objekts, kura klase ir Select (šī kalse ir domāta tieši darbam ar tā sauktajiem dropdown elementiem tīmekļa vietnēs, kuri sastāv no viarākam izvēles variantiem)
    exercise_dropdown = Select(driver.find_element(By.ID, 'fin_activity_modifier'))
    # Select klases objektam ir metode select_by_visible_text, kura izvēlas kādu variantu un visiem ispeājmiem pēc teksta, kurš ir rakstīts tajā
    exercise_dropdown.select_by_visible_text(exercise_mode)

    return [gender, age, height, weight, goal_weight, time_span, exercise_mode, meal_count]

def get_calculated_info():
    driver.find_element(By.CLASS_NAME, 'btn-danger').click()
    time.sleep(2)

    # Atrodam atbilstošu tabulu, tad atrodam tajā visas rindas, paņemam tikai 2. rindu un no katras šūnas rindā iegustam tekstu ar vērtībām
    table = driver.find_element(By.ID, 'tableContent')
    rows = table.find_elements(By.XPATH, './tbody/tr')
    row_for_per_day = rows[1]
    needed_cells = row_for_per_day.find_elements(By.XPATH, './td[position() > 1]')
    nutrients_per_day = [int(nutrients.text) for nutrients in needed_cells]
    nutrients_per_meal = [nutrient/4 for nutrient in nutrients_per_day]
    print(nutrients_per_day)
info_about_user = get_info()
time.sleep(2)
get_calculated_info()

time.sleep(10)
driver.close