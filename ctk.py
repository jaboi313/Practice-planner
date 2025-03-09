import customtkinter
from ttkwidgets.autocomplete import AutocompleteEntry

customtkinter.set_appearance_mode("system")  # Appearance: system (standard), "dark", "light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

def button_callback():
    print("button clicked")

app = customtkinter.CTk()
app.geometry("400x400")
app.title("Trainings rooster maker")

def segmented_button_callback(value):
    print("segmented button clicked:", value)

segemented_button = customtkinter.CTkSegmentedButton(app, values=["Value 1", "Value 2", "Value 3"],
                                                     command=segmented_button_callback)
segemented_button.set("Value 1")
segemented_button.pack(padx=20, pady=20)

def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

optionmenu = customtkinter.CTkOptionMenu(app, values=["option 1", "option 2"],
                                         command=optionmenu_callback)
optionmenu.set("option 2")
optionmenu.pack(padx=20, pady=20)

def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

combobox = customtkinter.CTkComboBox(app, values=["option 1", "option 2"],
                                     command=combobox_callback)
combobox.set("option 2")
combobox.pack(padx=20, pady=20)

button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.pack(padx=20, pady=20)

countries = [
        'Antigua and Barbuda', 'Bahamas','Barbados','Belize', 'Canada',
        'Costa Rica ', 'Cuba', 'Dominica', 'Dominican Republic', 'El Salvador ',
        'Grenada', 'Guatemala ', 'Haiti', 'Honduras ', 'Jamaica', 'Mexico',
        'Nicaragua', 'Saint Kitts and Nevis', 'Panama ', 'Saint Lucia', 
        'Saint Vincent and the Grenadines', 'Trinidad and Tobago', 'United States of America'
        ]

entry = customtkinter.CTkEntry(app, placeholder_text="CTkEntry")
d = AutocompleteEntry(app, completevalues=countries)
entry.pack(padx=20, pady=20)
d.pack(padx=20, pady=20)

app.mainloop()