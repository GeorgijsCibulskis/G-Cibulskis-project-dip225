import fitness_plan_creating
import searching_expanding
import customtkinter


def setting_start():
    # Kā izskatīsies logs
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("dark-blue")

    # Loga paramatri
    root = customtkinter.CTk()
    root.geometry("1000x900")
    root.title("NutriBoost")

    # Fons nosaukumam pašā augšā
    frame = customtkinter.CTkFrame(master = root, height = 50, width = 780)
    frame.pack_propagate(False) # Šīs ir vajadzīgs, lai fons nemainītu savu izmēru, balstoties uz to, kādā izmēra ir teksts, kurš tiks ierakstīts tajā fonā
    frame.pack(side = "top")

    # Programmas nosaukums pašā augšā
    label_title = customtkinter.CTkLabel(master = frame, text = "NutriBoost", font = customtkinter.CTkFont(size = 34, weight = "bold"))
    label_title.pack(expand = True)

    # Fons galvenajām kolonnam
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
    # saglābāta pogas 'value', ja uz tas ir uzspiests
    gender = customtkinter.StringVar(value = "")
    male_button = customtkinter.CTkRadioButton(master = frame1, text = "Male", variable = gender, value = "Male")
    female_button = customtkinter.CTkRadioButton(master = frame1, text = "Female", variable = gender, value = "Female")
    male_button.pack(pady=5)
    female_button.pack(pady=5)

    # Ievades lauki
    labels_for_entries = ["Name Surname", "Age", "Height", "Current weight", "Goal weight"]
    for label_text in labels_for_entries:
        entry = customtkinter.CTkEntry(master = frame1, placeholder_text = label_text)
        entry.pack(pady = 5)

    # Saraksts, uz kuru var uzspiest un izvēlēties atbilsošu variantu
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
    exercise_mode_options = ["Sedentary", "Light", "Moderate", "Very active", "Extreme"]
    exercise_mode = customtkinter.StringVar(value = "Sedentary")
    exercise_mode_menu = customtkinter.CTkOptionMenu(master = frame1, values = exercise_mode_options, variable = exercise_mode)
    exercise_mode_menu.pack(pady = 5)

    # Daudz 'radio' pogu ar izvēli, cik reizes lietotājs ēd dienā
    meals_per_day_label = customtkinter.CTkLabel(master = frame1, text = "Meals per day", font = customtkinter.CTkFont(size = 16, weight = "bold"))
    meals_per_day_label.pack()
    meals_per_day_var = customtkinter.StringVar(value = "3")
    meals_3_radio = customtkinter.CTkRadioButton(master = frame1, text = "3", variable = meals_per_day_var, value = "3")
    meals_4_radio = customtkinter.CTkRadioButton(master = frame1, text = "4", variable = meals_per_day_var, value = "4")
    meals_5_radio = customtkinter.CTkRadioButton(master = frame1, text = "5", variable = meals_per_day_var, value = "5")
    meals_6_radio = customtkinter.CTkRadioButton(master = frame1, text = "6", variable = meals_per_day_var, value = "6")
    meals_3_radio.pack(pady = 5)
    meals_4_radio.pack(pady = 5)
    meals_5_radio.pack(pady = 5)
    meals_6_radio.pack(pady = 5)

    # Poga, lai izveidotu jauno failu un izsaukt failu (fitness_pla_creating.py)
    button_create_plan = customtkinter.CTkButton(master = frame1, text = "Create Plan")
    button_create_plan.pack(pady = 10)

    # 2. kolonna, kura domāta, lai pievienotu barības vielas jau eksistējošam plānam
    frame2 = customtkinter.CTkFrame(master=frame_background)
    frame2.pack(side = "left", fill = "both", expand = True, pady = 20, padx = 10)
    frame2_label = customtkinter.CTkLabel(master = frame2, text = "Choose New Product", font = customtkinter.CTkFont(size = 28, weight = "bold"))
    frame2_label.pack(pady = 15)

    # Ievades lauks, lai ievadītu produkta nosaukumu
    product_entry = customtkinter.CTkEntry(master = frame2, placeholder_text = "Product")
    product_entry.pack(pady = 5)

    # Poga, lai atrastu produktu (izsauks failu searching&expanding.py)
    button_find_product = customtkinter.CTkButton(master = frame2, text = "Find product")
    button_find_product.pack(pady = 5)

    label_found_products = customtkinter.CTkLabel(master = frame2, text = "List of found products", font = customtkinter.CTkFont(size = 16, weight="bold"))
    label_found_products.pack(pady = 5)

    # teksta lauks, kurā tiks izvadīts saraksts ar viesiem atrastiem produktiem
    textbox_found_products = customtkinter.CTkTextbox(master = frame2, width = 350, height = 300)
    textbox_found_products.pack(pady=5)

    # Lietotājs var izvēlēties produktu no saraksta
    final_product_entry = customtkinter.CTkEntry(master = frame2, placeholder_text = "Final Product")
    final_product_entry.pack(pady = 5)

    # Jāievada produkta masa
    product_mass_entry = customtkinter.CTkEntry(master = frame2, placeholder_text = "Product's mass")
    product_mass_entry.pack(pady = 5)

    # Jāievada savs vārds un uzvārds
    name_entry = customtkinter.CTkEntry(master = frame2, placeholder_text = "Name Surname")
    name_entry.pack(pady = 5)

    label_end_of_day = customtkinter.CTkLabel(master = frame2, text = "Is this the end of the day?", font = customtkinter.CTkFont(size = 16, weight = "bold"))
    label_end_of_day.pack(pady = 5)

    # Jāatzīmē, vai tā ir dienas beigas (būs vajdzīgs, lai sekotu līdzi excel kolonnam)
    end_of_day_list = ["No", "Yes"]
    end_of_day = customtkinter.StringVar(value = "No")
    end_of_day_menu = customtkinter.CTkOptionMenu(master = frame2, values = end_of_day_list, variable = end_of_day)
    end_of_day_menu.pack(pady = 5)

    # Poga, kura saglabās visu excelī (izsauks searching&expanding.py)
    button_send_data = customtkinter.CTkButton(master = frame2, text = "Send data to plan")
    button_send_data.pack(pady = 5)

    root.mainloop()

setting_start()
