from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.config(padx=20, pady=20)
window.minsize(width=250, height=100)

in_value = Entry(width=10)
in_value.grid(row=1, column=2)

miles = Label(text='Miles')
miles.grid(row=1, column=3)
miles.config(padx=5)

km = Label(text='Km')
km.grid(row=2, column=3)

km_value = Label(text='0')
km_value.grid(row=2, column=2)

equal = Label(text='is equal to')
equal.grid(row=2, column=1)


def on_calc():
    km_value.config(text=float(in_value.get()) * 1.609)


calc = Button(text='Calculate', command=on_calc)
calc.grid(row=3, column=2)


window.mainloop()