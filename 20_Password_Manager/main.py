from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip, json

EMAIL = 'rav.cod3r@gmail.com'


# Search Json FIle
def search_website():
    website = website_entry.get().title()
    try:
        with open('data.json', 'r') as data_file:
            website_date = json.load(data_file)
            email = website_date[website]['email']
            password = website_date[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email} \n"
                                                       f"Password: {password}")
    except FileNotFoundError as msg:
        messagebox.showerror(title='Oops', message=msg)
    except KeyError as msg:  # Could do "if website in data", no need to use exception if "if/else" can handle it
        messagebox.showerror(title='Oops', message=f'No entry associated with {msg}')
    finally:
        website_entry.delete(0, END)


# Random Password Gen
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list.extend([choice(symbols) for _ in range(randint(2, 4))])
    password_list.extend([choice(numbers) for _ in range(randint(2, 4))])

    shuffle(password_list)
    password = ''.join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# Save Password, Validation
def save_info():
    website = website_entry.get().title()
    email = email_entry.get()
    pass_ = pass_entry.get()

    new_data = {
        website: {
            'email': email,
            'password': pass_,
        }
    }

    if len(website) == 0 or len(pass_) == 0:
        messagebox.showerror(title='Oops', message='Please do not leave any fields empty.')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f' Details entered: \n '
                                                              f'Email: {email} \n '
                                                              f'Password: {pass_} \n '
                                                              f'Do you want to proceed?')

        if is_ok:
            # with open('data.txt', mode='a') as data_file:
            #     data_file.write(f"{website} | {email} | {pass_}")
            #     data_file.write('\n')
            try:
                with open('data.json', 'r') as data_file:
                    data = json.load(data_file)
                    # print(data)
                    data.update(new_data)
            except FileNotFoundError:
                data = new_data
            finally:
                with open('data.json', 'w') as data_file:
                    # json.dump(new_data, data_file, indent=4)
                    json.dump(data, data_file, indent=4)

            website_entry.delete(0, END)
            pass_entry.delete(0, END)


# UI
window = Tk()
window.title('Password Manager')
# window.config(width=200, height=200)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(row=1, column=2)

website_text = Label(text='Website:')
website_text.grid(row=2, column=1)

email_text = Label(text="Email/Username:")
email_text.grid(row=3, column=1)

pass_text = Label(text='Password:')
pass_text.grid(row=4, column=1)

website_entry = Entry(width=22)
website_entry.grid(row=2, column=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.insert(0, EMAIL)
email_entry.grid(row=3, column=2, columnspan=2)

pass_entry = Entry(width=22)
pass_entry.grid(row=4, column=2)

search_B = Button(text='Search', width=10, command=search_website)
search_B.grid(row=2, column=3)

generate_B = Button(text='Generate', width=10, command=gen_password)
generate_B.grid(row=4, column=3)

add_B = Button(text='Add', width=30, command=save_info)
add_B.grid(row=5, column=2, columnspan=2)

window.mainloop()
