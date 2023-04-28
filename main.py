from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_list = []
    [password_list.append(choice(letters)) for char in range(randint(8, 10))]
    [password_list.append(choice(numbers)) for char in range(randint(2, 4))]
    [password_list.append(choice(symbols)) for char in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)

    password_e.delete(0, END)
    password_e.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_e.get()
    email = email_e.get()
    password = password_e.get()
    data = f"{website} , ID: {email} , Password: {password} \n"

    if website == "" or password == "" or email == "":
        messagebox.showerror(title="Invalid Data", message="Done leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Confirm the detail entered \n \nWebsite: {website} \nEmail: {email} \nPassword: {password} \n\nDo you want to Save")

        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(data)

            website_e.delete(0, END)
            password_e.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Password Manager")
window.minsize(200, 200)
window.config(padx=20, pady=20)

photo = PhotoImage(file="logo.png")

canvas = Canvas(height=200, width=200, highlightthickness=0)
canvas.create_image(100, 100, image=photo)

website_l = Label(text="website", pady=10)
email_l = Label(text="Email/Username", pady=10)
password_l = Label(text="password", pady=10)

website_e = Entry(width=40)
website_e.focus()
email_e = Entry(width=40)
email_e.insert(0, "yaitsmethiyagu@gmail.com")
password_e = Entry(width=21)

generate_b = Button(text="Generate Password", command=generate_password)
add_b = Button(text="Add", width=36, command=save)

canvas.grid(column=0, row=0, columnspan=3)
website_l.grid(column=0, row=1)
email_l.grid(column=0, row=2)
password_l.grid(column=0, row=3)

website_e.grid(columnspan=2, column=1, row=1)
email_e.grid(columnspan=2, column=1, row=2)
password_e.grid(column=1, row=3)
generate_b.grid(column=2, row=3)
add_b.grid(column=1, columnspan=2, row=4, pady=10)

window.mainloop()
