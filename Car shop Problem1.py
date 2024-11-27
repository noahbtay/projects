#LAB 8 Noah Taylor 
#Problem 1

import tkinter as tk

def totalprice():
    total = 0 #starts it at 0
    if oil_var.get():
        total += 30.00
    if lube_var.get():
        total += 20.00
    if radiator_var.get():
        total += 40.00
    if trans_var.get():
        total += 100.00
    if inspection_var.get():
        total += 35.00
    if muffler_var.get():
        total += 200.00
    if tire_var.get():
        total += 20.00
    total_label.config(text=f"Total: ${total:.2f}")
#creates main box of tkinter
mainbox = tk.Tk()
mainbox.title("Joes Automotive")

#defines buttons
oil_var = tk.IntVar()
lube_var = tk.IntVar()
radiator_var = tk.IntVar()
trans_var = tk.IntVar()
inspection_var = tk.IntVar()
muffler_var = tk.IntVar()
tire_var = tk.IntVar()

#creates the check button for each car issue
oil_check = tk.Checkbutton(mainbox, text="Oil change - $30.00", variable=oil_var)
oil_check.pack()
lube_check = tk.Checkbutton(mainbox, text="Lube check - $20.00", variable=lube_var)
lube_check.pack()
radiator_check = tk.Checkbutton(mainbox, text="Radiator flush - $40.00", variable=radiator_var)
radiator_check.pack()
transmission_check = tk.Checkbutton(mainbox, text="Transmission flush - $100.00", variable=trans_var)
transmission_check.pack()
inspection_check = tk.Checkbutton(mainbox, text="Inspection - $35.00", variable=inspection_var)
inspection_check.pack()
muffler_check = tk.Checkbutton(mainbox, text="Muffler Replacement - $200.00", variable=muffler_var)
muffler_check.pack()
tire_check = tk.Checkbutton(mainbox, text="Tire rotation - $20.00", variable=tire_var)

#creates button to calculate total
calculate = tk.Button(mainbox, text="Calculate total for today", command=totalprice)
calculate.pack()

total_label = tk.Label(mainbox, text="Total: $0.00")
total_label.pack()

thankyou_label = tk.Label(text="Thank you for using Noahs code!")
thankyou_label.pack()

mainbox.mainloop()
