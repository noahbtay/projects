#LAB 8 Problem 2 Noah Taylor

import tkinter as tk

def tax():
    actualvalue = float(value_entry.get())
    assessmentvalue = actualvalue * 0.60
    propertytax = (assessmentvalue / 100) * 0.75

    assessment_label.config(text=f"The assessment value is: ${assessmentvalue:.2f}")
    tax_label.config(text=f"The property tax is: ${propertytax:.2f}")

mainbox = tk.Tk()
mainbox.title("Noahs Property Tax Calculator")

tk.Label(mainbox, text="Enter the actual value of the property:").pack()
value_entry = tk.Entry(mainbox)
value_entry.pack()

calculate = tk.Button(mainbox, text="Calculate", command=tax)
calculate.pack()

assessment_label = tk.Label(mainbox, text="Assessment Value: $0.00")
assessment_label.pack()

tax_label = tk.Label(mainbox, text="Property tax: $0.00")
tax_label.pack()

thankyou_label = tk.Label(text="\nThanks for using Noahs property code!")
thankyou_label.pack()

mainbox.mainloop
