from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_field.delete(0, 'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
    password_numbers = [choice(numbers) for number in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_field.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    website = website_field.get()
    username = username_field.get()
    password = password_field.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }
    if website == "" or password == "":
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_field.delete(0, 'end')
            password_field.delete(0, 'end')

# -------------------------- FIND PASSWORD ------------------------------ #


def find_password():
    with open("data.json", "r") as file:
        data = json.load(file)
        try:
            website = data[website_field.get()]
        except FileNotFoundError:
            messagebox.showinfo(title="Not found", message="No Data File found.")
        else:
            if website in data:
                messagebox.showinfo(title=website, message=f"Username: {website['username']}\nPassword: {website['password']}")
            else:
                messagebox.showinfo(title="Not found", message="No details for the website found.")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0, sticky="EW")

# Labels
website_text = Label(text="Website:")
website_text.grid(column=0, row=1, sticky="EW")
username_text = Label(text="Email/Username:")
username_text.grid(column=0, row=2, sticky="EW")
password_text = Label(text="Password:")
password_text.grid(column=0, row=3, sticky="EW")

# Entry fields
website_field = Entry()
website_field.grid(column=1, row=1, sticky="EW")
website_field.focus()
username_field = Entry()
username_field.grid(column=1, row=2, columnspan=2, sticky="EW")
username_field.insert(0, "email@email.com")
password_field = Entry()
password_field.grid(column=1, row=3, sticky="EW")

# Buttons
search = Button(text="Search", command=find_password)
search.grid(column=2, row=1, sticky="EW")
generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(column=2, row=3, sticky="EW")
add_button = Button(text="Add", command=add_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
