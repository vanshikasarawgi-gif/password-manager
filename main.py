from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list  = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)   # Convert the list of characters into a single string

    password_entry.delete(0, END)  # Clear the Entry box before inserting new password
    password_entry.insert(0,password)  # Insert the newly generated password

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any field empty")

    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered\nEmail:{email}\n"
                                                             f"Password: {password} \n Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data:    #a = append mode
                data.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,END)  #removes text from the entry box 0 from starting point to end
                password_entry.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=70,pady=50)

canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(120,100,image=logo_img)
canvas.grid(row=0,column=1)

#label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#entry

website_entry = Entry(width=50)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus() #focuses cursor in the entry box

email_entry = Entry(width=50)
email_entry.grid(row=2,column=1,columnspan=2)

password_entry = Entry(width=31)
password_entry.grid(row=3,column=1)

#button

generate_pass_button = Button(text="Generate Password",command=password_generator)
generate_pass_button.grid(row=3,column=2)

add_button = Button(text="Add",width=45,command=save)
add_button.grid(row=4,column=1,columnspan=2)



window.mainloop()