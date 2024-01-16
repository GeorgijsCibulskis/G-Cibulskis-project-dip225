import customtkinter
from tkinter import messagebox
from threading import Thread

import fitness_plan_creating
import searching
import expanding

# Funkcija, kura pārbauda visas ievadītas vērtības (pārnests no fitness_plan_creating.py)
def validate_entries_for_plan_creating(age, weight, goal_weight, height):
    if (age.isnumeric() == False) or int(age) < 0 or int(age) > 110:
        return False
    if (weight.isnumeric() == False) or int(weight) < 30 or int(weight) > 360:
        return False
    if (goal_weight.isnumeric() == False) or int(goal_weight) < int(weight) or int(weight) > 360:
        return False
    if (height.isnumeric() == False) or int(height) < 20 or int(height) > 300:
        return False
    return True

# Ja viss ir pareizi ievadīts, tad izsaucam failu un izveidojam fitness plānu
def create_plan_if_valid(age, weight, goal_weight, height, time_span, exercise_mode, meal_count, gender, name, progressbar):
    if validate_entries_for_plan_creating(age, weight, goal_weight, height):

        # Sākam rādīt progresu lietotājam
        progressbar.pack(pady = 5, padx = 5)
        progressbar.start()

        # Šīs ir vajadzīgs, lai izvairītos no tā, ka, kamēr fails fitness_plan_creating.py ir darbībā, pats user interface paliek 'sasaldēts' un 'Not responding'
        # tāpēc vajag izmantot vēl vienu 'plūsmu' (thread), kurā arī notiks visa cita faila darbība, bet pats UI paliks galvenā plūsmā
        Thread(target = fitness_plan_creating.main, args = (age, weight, goal_weight, height, time_span, exercise_mode, meal_count, gender, name, progressbar)).start()
    else:

        # customtkinter nav tādas funkcijas messagebox, tāpēc vajadzēja importēt parasto tkinter
        messagebox.showerror("Error", "Invalid input. Please check your entries.")

# Funkcija, kura meklē ievadīto produktu un izsauc searching.py
def searching_product(textbox, product_name, progressbar):
    
    # Pārbaude vai kaut kas tika ievadīts
    if product_name == '':
        messagebox.showerror("Error", "Please enter a product")
        return
    
    # Katrā meklēšanā ir jānotīra teksta kaste
    textbox.delete(1.0, 'end')
    progressbar.pack(pady = 5, padx = 5)
    progressbar.start()
    Thread(target = searching.main, args = (textbox, product_name, progressbar)).start()

# Funkcija, kura pārbauda vai tika izvēlēts pareizais produkts un izsauc expanding.py
def expanding_excel_with_product(name, product, mass, textbox_info, end_of_day, progressbar):
    
    # Iegustām katru rindu no teksta kastes (no produktiem, kuri tika atrasti) 
    products_in_textbox = textbox_info.split('\n')

    # Dažkārt sarakstā var parādīties tukšie elementi, tāpēc tie arī ir jāizdzēš
    products_in_textbox = [product for product in products_in_textbox if product != '']
    
    # Tā kā katras rindas sākumā ir "- ", tad tie 2 elementi ir jāizņem ārā no katra elementa sarakstā
    for i in range(len(products_in_textbox)):
        products_in_textbox[i] = products_in_textbox[i][2:].strip()

    if product.strip() in products_in_textbox:
        progressbar.pack(pady = 5, padx = 5)
        progressbar.start()
        Thread(target = expanding.main, args = (name, product, mass, end_of_day, progressbar)).start()
    else:
        messagebox.showerror("Error", "No such product in the list")

def setting_start():

    # Kā izskatīsies logs
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("dark-blue")

    # Loga parametri
    root = customtkinter.CTk()
    root.geometry("1000x950")
    root.title("NutriBoost")

    # Fons nosaukumam pašā augšā
    frame = customtkinter.CTkFrame(master = root, height = 50, width = 780)
    frame.pack_propagate(False) # Šīs ir vajadzīgs, lai fons nemainītu savu izmēru, balstoties uz to, kādā izmēra ir teksts, kurš tiks ierakstīts tajā fonā
    frame.pack(side = "top")

    # Programmas nosaukums pašā augšā
    label_title = customtkinter.CTkLabel(master = frame, text = "NutriBoost", font = customtkinter.CTkFont(size = 34, weight = "bold"))
    label_title.pack(expand = True)

    # Fons galvenajām kolonnām
    frame_background = customtkinter.CTkFrame(master = root)
    frame_background.pack(side = "top", fill = "both", expand = True, pady = 20, padx = 10)

    # Kreisā kolonna, kura domāta, lai izveidotu jauno failu ar fitness plānu
    frame1 = customtkinter.CTkFrame(master = frame_background)
    frame1.pack(side = "left", fill = "both", expand = True, pady = 20, padx = 10)
    frame1_label = customtkinter.CTkLabel(master = frame1, text = "Create New Fitness Plan", font=customtkinter.CTkFont(size = 28, weight = "bold"))
    frame1_label.pack(pady = 15)

    # Dzimuma izvēle
    gender_label = customtkinter.CTkLabel(master = frame1, text = "Gender", font = customtkinter.CTkFont(size = 16, weight = "bold"))
    gender_label.pack()

    # Šeit ir nepieciešams izveidot mainīgo gender, jo tas glabās sevī vērtību, kuru izvēlēsies lietotājs, jo tālāk 'radio' pogu argumentos ir 'variable', kas ir mainīgais, kurā tiks
    # saglabātā pogas 'value', ja uz tas ir uzspiests
    gender = customtkinter.StringVar(value = "")
    male_button = customtkinter.CTkRadioButton(master = frame1, text = "Male", variable = gender, value = "Male")
    female_button = customtkinter.CTkRadioButton(master = frame1, text = "Female", variable = gender, value = "Female")
    male_button.pack(pady=5)
    female_button.pack(pady=5)

    # Ievades lauki
    labels_for_entries = ["Name Surname", "Age", "Current weight", "Goal weight", "Height"]

    # Tā kā ievades lauki ir veidoti ciklā, tad, lai pēc tam no tiem dabūtu ārā vērtību, vajag izveidot sarakstu ar tiem ievades laukiem, indeksus kuriem var ērti saprast no nosaukumu saraksta rindā augstāk
    many_entries = []
    for label_text in labels_for_entries:
        entry = customtkinter.CTkEntry(master = frame1, placeholder_text = label_text)
        entry.pack(pady = 5)
        many_entries.append(entry)

    # Saraksts, uz kuru var uzspiest un izvēlēties atbilstošu variantu
    time_span_label = customtkinter.CTkLabel(master = frame1, text = "Time Span", font = customtkinter.CTkFont(size = 16, weight = "bold"))
    time_span_label.pack()

    # Kādi varianti ir pieejami
    time_span_options = ["1 week", "2 weeks", "3 weeks", "1 month", "2 months", "3 months", "4 months", "5 months", "6 months", "1 year"]

    # Atkal mainīgais, kurš sevī glabās vērtību par laika periodu
    time_span = customtkinter.StringVar(value = "1 week")
    time_span_menu = customtkinter.CTkOptionMenu(master = frame1, values = time_span_options, variable = time_span)
    time_span_menu.pack(pady = 5)

    # Saraksts ar aktivitātes līmeņiem
    exercise_mode_label = customtkinter.CTkLabel(master = frame1, text = "Exercise Level", font = customtkinter.CTkFont(size = 16, weight = "bold"))
    exercise_mode_label.pack()
    exercise_mode_options = ["Sedentary", "Light", "Moderate", "Very Active", "Extreme"]
    exercise_mode = customtkinter.StringVar(value = "Sedentary")
    exercise_mode_menu = customtkinter.CTkOptionMenu(master = frame1, values = exercise_mode_options, variable = exercise_mode)
    exercise_mode_menu.pack(pady = 5)

    # Daudz 'radio' pogu ar izvēli, cik reizes lietotājs ēd dienā
    meals_per_day_label = customtkinter.CTkLabel(master = frame1, text = "Meals per day", font = customtkinter.CTkFont(size = 16, weight = "bold"))
    meals_per_day_label.pack()
    meals_per_day = customtkinter.StringVar(value = "3")
    meals_3_radio = customtkinter.CTkRadioButton(master = frame1, text = "3", variable = meals_per_day, value = "3")
    meals_4_radio = customtkinter.CTkRadioButton(master = frame1, text = "4", variable = meals_per_day, value = "4")
    meals_5_radio = customtkinter.CTkRadioButton(master = frame1, text = "5", variable = meals_per_day, value = "5")
    meals_6_radio = customtkinter.CTkRadioButton(master = frame1, text = "6", variable = meals_per_day, value = "6")
    meals_3_radio.pack(pady = 5)
    meals_4_radio.pack(pady = 5)
    meals_5_radio.pack(pady = 5)
    meals_6_radio.pack(pady = 5)

    # Poga, lai izveidotu jauno failu un izsaukt failu (fitness_plan_creating.py)
    # lambda ir nepieciešama, lai izsauktu funkciju create_plan_if_valid ar atbilstošiem argumentiem, jo citādāk to izdarīt nevar
    # - ja izsauks bez lambda (command=create_plan_if_valid(/argumenti\)), tad tā funkcija izsauksies uzreiz, kad python implimentēs šo rindu, bet ievades laukos vēl nekā nebūs => nav piemērots
    # - ja izkaukt funkciju bez iekavām kā atsauci uz funkciju (command = create_plan_if_valid), tad tajā nevarēs ierakstīt argumentus
    # tāpēc ir vajadzīga anonīma funkcija lambda, kuras 'arguments' ir īsta funkcija
    button_create_plan = customtkinter.CTkButton(master = frame1, text = "Create Plan", command = lambda:create_plan_if_valid(many_entries[1].get(), many_entries[2].get(), many_entries[3].get(), many_entries[4].get(), time_span.get(), exercise_mode.get(), meals_per_day.get(), gender.get(), many_entries[0].get(), progressbar1))
    button_create_plan.pack(pady = 10)

    # Progresa rādītājs
    progressbar1 = customtkinter.CTkProgressBar(master = frame1)

    # 2. kolonna, kura domāta, lai pievienotu barības vielas jau eksistējošam plānam
    frame2 = customtkinter.CTkFrame(master=frame_background)
    frame2.pack(side = "left", fill = "both", expand = True, pady = 20, padx = 10)
    frame2_label = customtkinter.CTkLabel(master = frame2, text = "Choose New Product", font = customtkinter.CTkFont(size = 28, weight = "bold"))
    frame2_label.pack(pady = 15)

    product_label = customtkinter.CTkLabel(master = frame2, text = "Enter product", font = customtkinter.CTkFont(size = 16, weight = "bold"))
    product_label.pack(pady = 5)

    # Ievades lauks, lai ievadītu produkta nosaukumu
    product_entry = customtkinter.CTkEntry(master = frame2, placeholder_text = "Product")
    product_entry.pack(pady = 5)

    # Poga, lai atrastu produktu (izsauks failu searching.py)
    button_find_product = customtkinter.CTkButton(master = frame2, text = "Find product", command = lambda:searching_product(textbox_found_products, product_entry.get(), progressbar2))
    button_find_product.pack(pady = 5)

    progressbar2 = customtkinter.CTkProgressBar(master = frame2)

    label_found_products = customtkinter.CTkLabel(master = frame2, text = "List of found products", font = customtkinter.CTkFont(size = 16, weight="bold"))
    label_found_products.pack(pady = 5)

    # Teksta lauks, kurā tiks izvadīts saraksts ar visiem atrastiem produktiem
    textbox_found_products = customtkinter.CTkTextbox(master = frame2, width = 420, height = 300)
    textbox_found_products.pack(pady=5)

    # Lietotājs var izvēlēties produktu no saraksta
    final_product_entry = customtkinter.CTkEntry(master = frame2, placeholder_text = "Final Product")
    final_product_entry.pack(pady = 5)

    # Jāievada produkta masa
    product_mass_entry = customtkinter.CTkEntry(master = frame2, placeholder_text = "Product's mass (in g)")
    product_mass_entry.pack(pady = 5)

    # Jāievada savs vārds un uzvārds
    name_entry = customtkinter.CTkEntry(master = frame2, placeholder_text = "Name Surname")
    name_entry.pack(pady = 5)

    label_end_of_day = customtkinter.CTkLabel(master = frame2, text = "Is this the end of meals for today?", font = customtkinter.CTkFont(size = 16, weight = "bold"))
    label_end_of_day.pack(pady = 5)

    # Jāatzīmē, vai tā ir dienas beigas (būs vajadzīgs, lai sekotu līdzi excel kolonnām)
    end_of_day = customtkinter.StringVar(value = "No")
    meals_3_radio = customtkinter.CTkRadioButton(master = frame2, text = "No", variable = end_of_day, value = "No")
    meals_4_radio = customtkinter.CTkRadioButton(master = frame2, text = "Yes", variable = end_of_day, value = "Yes")
    meals_3_radio.pack(pady = 5)
    meals_4_radio.pack(pady = 5)

    # Poga, kura saglabās visu excelī (izsauks expanding.py)
    button_send_data = customtkinter.CTkButton(master = frame2, text = "Send data to plan", command = lambda:expanding_excel_with_product(name_entry.get(), final_product_entry.get(), product_mass_entry.get(), textbox_found_products.get(1.0, 'end'), end_of_day.get(), progressbar2))
    button_send_data.pack(pady = 10)

    root.mainloop()

def main():
    setting_start()

if __name__ == "__main__":
    main()