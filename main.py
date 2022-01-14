from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
FONT_SIZE = 10
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_letters = [random.choice(letters) for _ in range(nr_letters)]
  password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
  password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
  password_list = password_letters + password_symbols + password_numbers
  random.shuffle(password_list)

  pass_word = "".join(password_list)
  password_entry.insert(0, pass_word)
  pyperclip.copy(pass_word)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def saving_pass():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    new_data = {
        website:{
            "email":email,
            "password":password
        }
    }
    if len(website) != 0 and len(password) != 0 and len(email) != 0:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            print("Adding new data to file.")
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()
    else:
        messagebox.showinfo(title="ERROR", message="Please don't leave any fields empty.")

# --------------------------- SEARCHING FOR PASSWORD ----------------------------- #
def searching():
    search = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR!!", message="No Data File Found")
    except KeyError:
        messagebox.showinfo(title="ERROR!!", message="No details for the website exists")
    else:
        emails = data[search]["email"]
        passwords = data[search]["password"]
        messagebox.showinfo(title="Information", message=f"Email:{emails}\nPassword:{passwords}")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
image_png = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=image_png)
canvas.grid(column=1, row=0)
website_label = Label(text="Website:", font=("Arial", FONT_SIZE, "normal"))
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", font=("Arial", FONT_SIZE, "normal"))
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=("Arial", FONT_SIZE, "normal"))
password_label.grid(column=0, row=3)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=1, sticky="ew")
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="ew")
password_button = Button(text="Generate Password", command=password_generator)
password_button.grid(column=2, row=3, sticky="ew")
add_button = Button(text="Add", width=36, command=saving_pass)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")
search_button = Button(text="Search", command=searching)
search_button.grid(column=2, row=1, sticky="ew")




window.mainloop()