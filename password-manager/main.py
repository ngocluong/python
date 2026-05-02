import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def search_pass():
    data = {}
    with open("data.json", "r") as data_file:
        try:
            data = json.load(data_file)
            data_entry = data[website_entry.get()]
            if data_entry:
                messagebox.showinfo("Password Found", f"{data_entry}")
        except(FileNotFoundError, KeyError):
            messagebox.showerror("Error", "Cannot find the data")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    password = password_entry.get()
    website = website_entry.get()
    email = email_entry.get()
    new_data = { website: {
        'email': email,
        'password': password,
    } }
    if len(password) == 0 or len(website) == 0 or len(email) == 0:
        messagebox.showerror("Error", "Please fill all fields")
        return
    out = messagebox.askokcancel("Confirm Password", "Confirm Password?")
    if out:
        data = {}
        with open("data.json", "r") as data_file:
            try:
                data = json.load(data_file)
            except json.decoder.JSONDecodeError:
                pass
            finally:
                data.update(new_data)
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo(title="Password Manager", message="Password Manager has been saved")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pasword Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)


website_label = Label(text="Website")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/username")
email_label.grid(column=0, row=2)

password_label = Label(text="Password")
password_label.grid(column=0, row=3)

website_entry = Entry(width=22)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_button = Button(text="Search", command=search_pass)
search_button.grid(column=2, row=1)

email_entry = Entry(width=39)
email_entry.grid(column=1, columnspan=2, row=2)
email_entry.insert(0, "tracy.leung.1991@gmail.com")

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add Password", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()