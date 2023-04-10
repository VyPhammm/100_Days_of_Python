from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters= [choice(letters) for _ in range(randint(8, 10))]
    password_symbols= [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers= [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, string= password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "user": user,
            "password": password
        }
    }
    if len(website) == 0 or len(user) == 0 or len(password) == 0 :
        messagebox.showinfo(title= "Oops", message= "Please don't leave any fields empty")
    else:
        is_oke = messagebox.askokcancel(title= website, message= f"These are details entered: \n Username: {user} \n Password: {password} \nIs it ok to save? ")
        if is_oke:
            try:
                with open(r"Day29_Password-Manager\data.json", "r") as data_file :
                    data = json.load(data_file)
            except FileNotFoundError:
                with open(r"Day29_Password-Manager\data.json", "w") as data_file :
                    json.dump(new_data, data_file, indent= 4)
            else:
                data.update(new_data)
                with open(r"Day29_Password-Manager\data.json", "w") as data_file :
                    json.dump(data, data_file, indent= 4)

                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- SEARCH ------------------------------- #

def search():
    website = website_entry.get()
    try:
        with open(r"Day29_Password-Manager\data.json", "r") as data_file :
            data = json.load(data_file)
    except FileNotFoundError:
         messagebox.showinfo(title= "Oops", message= "No data file found.")
    else:
        if website in data:
            user = data[website]["user"]
            password = data[website]["password"]
            messagebox.showinfo(title= website, message= (f"User: {user} \nPassword: {password}"))
        else:
            messagebox.showinfo(title= website, message= f"No detail for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx= 50, pady= 50)

#Logo
canvas = Canvas(width= 200, height= 200)
logo_image = PhotoImage(file= r"D:\100_Days_of_Python\Day29_Password-Manager\logo.png")
canvas.create_image(100, 100, image= logo_image)
canvas.grid(column= 1, row= 0)

#Row 1:
website_label = Label(text="Website: ")
website_label.grid(column= 0, row= 1)

website_entry = Entry(width=30, highlightthickness= 0)
website_entry.grid(column= 1, row= 1, columnspan=2, sticky=W)
website_entry.focus()

search_button = Button(width= 14, text="Search", command= search)
search_button.grid(column= 2, row= 1, sticky= E)

#Row 2:
user_label = Label(text="Email/Username: ")
user_label.grid(column= 0, row= 2)

user_entry = Entry(width=52, highlightthickness= 0)
user_entry.grid(column= 1, row= 2, columnspan=2, sticky=W)
user_entry.insert(0, "phamvy@gmail.com")

#Row 3:
password_label = Label(text="Password: ")
password_label.grid(column= 0, row= 3)

password_entry = Entry(width=30)
password_entry.insert(END, string="")
password_entry.grid(column= 1, row= 3, sticky=W)

generate_button = Button(text="Generate Password", command= password_generator)
generate_button.grid(column= 2, row= 3, sticky=E)

#Row 4:
add_button = Button(text="Add", width=44, highlightthickness= 0, command= save_data)
add_button.grid(column= 1, row= 4, columnspan= 2, sticky=W)


window.mainloop()