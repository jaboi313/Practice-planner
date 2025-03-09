from tkinter import *

def login():        
    master = Tk()
    i=IntVar()
    variable = StringVar(master)
    w = OptionMenu(master, variable, "myaccount1", "myacc", "myaccount1", "myaccount2", "Dyrbart konto")
    c = Checkbutton(master, text = "Yes, I want to change account", variable=i)
    w.pack()
    c.pack()
    b = Button(master,text="Login",command=login)
    b.pack()
    master.geometry("400x400+120+120")
    master.mainloop()
        
login()