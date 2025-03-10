import tkinter as tk
from tkinter import ttk

# create a tkinter window
window = tk.Tk()
window.geometry("720x250")
window.title("Multiple Selection Combobox using the Checkbox Widget")

# define the values for the dropdown list
values = ["Value 1", "Value 2", "Value 3", "Value 4", "Value 5"]

# create a label for the combobox
label = ttk.Label(window, text="Select values:")

# create a combobox
combobox = ttk.Combobox(window)

# create a list of BooleanVar objects to hold the state of the Checkbuttons
checkbuttons_vars = [tk.BooleanVar() for value in values]

# create a Checkbutton widget for each value in the dropdown list
checkbuttons = []
for index, value in enumerate(values):
   checkbutton = ttk.Checkbutton(window, text=value, variable=checkbuttons_vars[index])
   checkbutton.pack(side="top", anchor="w")
   checkbuttons.append(checkbutton)

# define a function to update the combobox when the user selects or deselects a value
def update_combobox():
   selected_values = [value for value, var in zip(values, checkbuttons_vars) if var.get()]
   combobox.configure(width=40, height=7)
   combobox.delete(0, tk.END)
   combobox.insert(0, ", ".join(selected_values))

# add a button to update the combobox
update_button = ttk.Button(window, text="Update", command=update_combobox)
update_button.pack(side="bottom")

# pack the label and combobox
label.pack(side="top", anchor="w", pady=30)
combobox.pack(side="top")

# start the main loop
window.mainloop()