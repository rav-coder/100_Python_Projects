from tkinter import *

window = Tk()
window.title('Testing')
window.minsize(width=500, height=500)
window.config(padx=30, pady=30)

# Label
my_label = Label(text='This is a label', font=('Arial', 20, 'bold'))
my_label.grid(column=0, row=0)
my_label.config(padx=30, pady=30)
# my_label.pack(side='left', expand=2)  # side = bottom, right, tom
# my_label.place(x=100, y=200)  # place is for precise values


# my_label['text'] = 'New Text'
# my_label.config(text='Text 3')

def on_calculate():
    # my_label.config(text='Button clicked')
    my_label.config(text=in_value.get())
    # print("here")


button = Button(text='Calculate', command=on_calculate)
button.grid(row=1, column=3)

# Entry
in_value = Entry(width=10)
in_value.grid(row=1, column=2)

window.mainloop()
