import tkinter
from tkinter import *
from tkinter import messagebox
import pyperclip
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
root = Tk()
root.title("Password Manager")
root.geometry("500x500")
passwrd = StringVar()
passlen = IntVar()


def generate_password():
    characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
                  "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6",
                  "7", "8", "9", "0", ".", ",",
                  "!", "?", "/", ":", ";", "A", "B", "C", "D", "E", "F", "G", "H", "I",
                  "J", "K", "L", "M", "N", "O", "P","Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                  "(", ")", "@", "£", "$", "%", "^", "&", "*", "-", "_", "=", "+"]
    password = ""
    for x in range(passlen.get()):
        password = password + random.choice(characters)
    passwrd.set(password)


def copy_to_clipboard():
    random_password = passwrd.get()
    pyperclip.copy(random_password)
    generated_password["text"] = "Copied!"
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    password_input_chars = input_field
    ready_pass_field = ready_password
    if len(password) == 0:
        messagebox.showwarning(message="No password? Please enter a number of characters and click on 'Generate Password' to get a password:)")

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please do not leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username}"
                                                              f"\nPassword: {password}\nDo you want to save it?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"Website: {website}, Username/Email: {username}, Password: {password}\n")
                website_entry.delete(0, END)
                username_entry.delete(0, END)
                password_entry.delete(0, END)
                password_input_chars.delete(0, END)
                ready_pass_field.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(110, 105, image=logo_img)
canvas.grid(column=1, row=0)

label_website = tkinter.Label(text="Website:")
label_website.grid(column=0, row=1)
label_username = tkinter.Label(text="Email/Username:")
label_username.grid(column=0, row=2)
label_password = tkinter.Label(text="Password:")
label_password.grid(column=0, row=3)

website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.get()
website_entry.config(width=38)

username_entry = Entry()
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.get()
username_entry.config(width=38)

password_entry = Entry()
password_entry.grid(row=3, column=1, columnspan =2)
password_entry.get()
password_entry.config(width=38)


button_generate_password = tkinter.Button(text="Generate Password", command=generate_password)
button_generate_password.grid(row=7, column=1, columnspan=2)

button_add = tkinter.Button(text="Add", command=save)
button_add.grid(row=4,column=1, columnspan=2)
button_add.config(width=36)

generated_password = tkinter.Label(text="Generated password:")
generated_password.grid(column=1, row=6, columnspan=2)

ready_password = Entry(textvariable=passwrd)
ready_password.grid(column=1, row=8, columnspan=2)

copy_to = tkinter.Button(text="Copy", command=copy_to_clipboard)
copy_to.grid(column=1, row=9, columnspan=2)

label = tkinter.Label(text="How many characters would you like your password to be?")
label.grid(column=1, row=5, columnspan=2)

input_field = Entry(textvariable=passlen)
input_field.grid(column=1, row=6, columnspan=2)
input_field.get()

root.mainloop()