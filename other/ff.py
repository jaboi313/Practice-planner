import tkinter as tk
from tkinter import ttk

# create a tkinter window
window = tk.Tk()
window.geometry("720x250")
window.title("Multiple Selection Combobox using the Listbox widget")

# define the values for the dropdown list
values = ["Value 1", "Value 2", "Value 3", "Value 4", "Value 5"]

# create a label for the combobox
label = ttk.Label(window, text="Select values:")

# create a combobox
combobox = ttk.Combobox(window, state="readonly")

# create a Listbox widget for the dropdown list
listbox = tk.Listbox(window, selectmode="multiple", exportselection=0)
for value in values:
   listbox.insert(tk.END, value)

# define a function to update the combobox when the user selects or deselects a value
def update_combobox():
   # Get selected values from the Listbox widget
   selected_values = [listbox.get(idx) for idx in listbox.curselection()]
    
   # Update the combobox with the selected values
   combobox.configure(width=40, height=7)
   combobox.set(", ".join(selected_values))
    
# bind the update_combobox function to the Listbox widget
listbox.bind("<<ListboxSelect>>", lambda _: update_combobox())

# pack the label, combobox, and Listbox widget
label.pack(side="top", anchor="w", pady=30)
combobox.pack(side="top", pady=30)
listbox.pack(side="top")

# start the main loop
window.mainloop()