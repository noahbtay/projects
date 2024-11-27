#LAB 8 Problem 3 Noah Taylor

import tkinter as tk
from tkinter import messagebox

#allows for input of number
def calculate_charge():
    minutes = float(minutes_entry.get())
    
#shows different rates and prices for each
    rate = rate_var.get()
    if rate == "Daytime":
        charge = minutes * 0.20
    elif rate == "Evening":
        charge = minutes * 0.15
    elif rate == "Offpeak":
        charge = minutes * 0.10
# for box that pops up when 'calculate' button is pressed
    messagebox.showinfo("Charge", f"The charge for the call is: ${charge:.2f}")

mainbox = tk.Tk()
mainbox.title("Noahs long distance calling calculator")

tk.Label(mainbox, text="Minutes:").pack()
minutes_entry = tk.Entry(mainbox)
minutes_entry.pack()

rate_var = tk.StringVar(value="Daytime")
#allows for the selection of the three choices
tk.Radiobutton(mainbox, text="Daytime", variable=rate_var, value="Daytime").pack()
tk.Radiobutton(mainbox, text="Evening", variable=rate_var, value="Evening").pack()
tk.Radiobutton(mainbox, text="Offpeak", variable=rate_var, value="Offpeak").pack()

tk.Button(mainbox, text="Calculate price", command=calculate_charge).pack()

thankyou_label = tk.Label(text="\nThank you for calling using Noahs Long call!")
thankyou_label.pack()

mainbox.mainloop()
