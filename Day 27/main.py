from tkinter import *

window = Tk()
window.title("Meow")
window.config(padx=20, pady=20)

#Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

zero_label = Label(text="0")
zero_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

#button
def action():
    miles = miles_input.get()
    km = float(miles) * 1.609
    zero_label.config(text=km)

calculate_button = Button(text="Calculate", command=action)
calculate_button.grid(column=1, row=3)

#input

miles_input = Entry()
miles_input.grid(column=1, row=0)


window.mainloop()
