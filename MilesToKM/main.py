from tkinter import *


def button_click():
    m = float(miles_text.get())
    k = m * 1.609
    km_text.config(text=k)


window = Tk()
window.title("Miles to KM Converter")
window.config(padx=30, pady=30)

miles_text = Entry(width=3, font=("Arial", 16))
miles_text.grid(column=1, row=0)

miles = Label(text="miles", font=("Arial", 16))
miles.grid(column=2, row=0)

is_equal_to = Label(text="is equal to", font=("Arial", 16))
is_equal_to.grid(column=0, row=1)

km_text = Label(text="0", font=("Arial", 16))
km_text.grid(column=1, row=1)

km = Label(text="Km", font=("Arial", 16))
km.grid(column=2, row=1)

calculate = Button(text="Calculate", command=button_click)
calculate.grid(column=1, row=2)


window.mainloop()
