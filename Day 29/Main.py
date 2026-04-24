from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password="".join(password_list)
    passwd_box.delete(0,END)
    passwd_box.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
file=open("C:/Users/Rudraksh Sharma/Documents/100-days/Day 29/data.txt",mode="a")
def add_data(website_box,username_box,passwd_box): 
    passwrd= passwd_box.get()
    web=website_box.get()
    email=username_box.get()
    if passwrd ==""or email=="" or web == "":
        messagebox.showinfo(title="Error", message="You cannot leave spaces empty.")
    else:
        is_ok=messagebox.askokcancel(title="Saved", message=f"These are the details you've entered: \nEmail: {email}\nPassword: {passwrd} \nIs it okay to save?")
        if is_ok:
            file.write(f"{web} | {email} | {passwrd}\n")
            
    website_box.delete(0,END)
    passwd_box.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)
canvas=Canvas(width=200,height=200)
logo = PhotoImage(file="C:/Users/Rudraksh Sharma/Documents/100-days/Day 29/logo.png")
website= Label(text="Website:",font=("Arial",10,"bold"))
website.grid(column=0,row=1)
website_box=Entry(width=35)
website_box.focus()
website_box.grid(row=1,column=1,columnspan=2)
username= Label(text="Email/Username:",font=("Arial",10,"bold"))
username.grid(column=0,row=2)
username_box=Entry(width=35)
username_box.grid(row=2,column=1,columnspan=2)
passwd=Label(text="Password:",font=("Arial",10,"bold"))
passwd.grid(row=3,column=0)
passwd_box=Entry(width=24)
passwd_box.grid(row=3,column=1,columnspan=1,padx=(0, 2),sticky="e")
username_box.insert(0,"rudr.sh08@gmail.com")
generate=Button(text="Generate Password",height=1,width=15,command=generate_pass)
generate.grid(column=2,row=3,padx=(0,0))
add=Button(text="Add",height=1,width=21,command=lambda: add_data(website_box, username_box, passwd_box))
add.grid(column=1,row=4)
canvas.create_image(80,100,image=logo)
canvas.grid(column=1, row=0)
window.mainloop()
file.close()
