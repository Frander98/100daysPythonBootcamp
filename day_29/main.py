from tkinter import *
from tkinter import messagebox
import random
import json

# TODO after creating all the project, refactor with OOP.

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
num_symbols = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'l', 'o', 'p', 'q', 'r', 's',
                 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'L', 'O', 'P', 'Q', 'R', 'S',
                 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

case = num_symbols + lower_letters + upper_letters


def pasword_gen():
    temp_var = random.sample(case, 15)
    password_txt = "".join(temp_var)
    password_entry.insert(0, password_txt)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    global web_site_entry, email_entry, password_entry
    web_site_content = web_site_entry.get()
    email_entry_content = email_entry.get()
    password_content = password_entry.get()
    new_data = {
        web_site_content: {
            "email": email_entry_content,
            "password": password_content,
        }
    }

    if len(web_site_content) == 0 or len(email_entry_content) == 0 or len(password_content) == 0:
        messagebox.showinfo(title="Can not process", message="Sorry, don't leave any of the fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=web_site_content, message=f"{web_site_content} \n {email_entry_content} "
                                                                       f"\n {password_content} \n Is it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    # Inserting data to a new file created
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                web_site_entry.delete(0, END)
                password_entry.delete(0, END)


# JSON doc : Write = json.dump(), Read = json.load(), Update = json.update()
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        error_message = "No Data File Found"
        messagebox.showinfo(title="Can not process", message=error_message)
    else:
        try:
            website_data = data[web_site_entry.get()]
        except KeyError:
            messagebox.showinfo(title="Can not process", message ="No details for the website exists.")
        else:
            messagebox.showinfo(title=f"Information about your web site",
                            message=f"Website: {web_site_entry.get()}\n"
                                    f"Email: {website_data['email']}\n "
                                    f"Password: {website_data['password']}")

# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)
window.minsize(width=350, height=350)

# Canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
web_site = Label(text="Website:")
web_site.grid(column=0, row=1)
email = Label(text="Email/Username:")
email.grid(column=0, row=2)
password = Label(text="Password")
password.grid(column=0, row=3)

# Entries
web_site_entry = Entry(width=30)
web_site_entry.grid(column=1, row=1)
web_site_entry.focus()
email_entry = Entry(width=30)
email_entry.insert(0, "franderadriel1998@gmail.com")
email_entry.grid(column=1, row=2)
password_entry = Entry(width=30)
password_entry.place(x=107, y=249)

# Buttons
generate_password = Button(text="Gen passw", command=pasword_gen)
generate_password.grid(column=2, row=3)
add_to_file = Button(text="Add", width=25, command=save)
add_to_file.place(x=107, y=275)
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
