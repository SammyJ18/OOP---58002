import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Signing Up an Account")

def submit():
    name = name_entry.get()
    gender = gender_var.get()
    contact = contact_entry.get()
    birthdate = birthdate_entry.get()
    email = email_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    # Check for empty fields
    if name == "":
        messagebox.showerror("Error", "Please enter your name")
        return
    if gender == "":
        messagebox.showerror("Error", "Please select your gender")
        return
    if contact == "":
        messagebox.showerror("Error", "Please enter your contact information")
        return
    if birthdate == "":
        messagebox.showerror("Error", "Please enter your birthdate")
        return
    if email == "":
        messagebox.showerror("Error", "Please enter your email address")
        return
    if username == "":
        messagebox.showerror("Error", "Please enter a username")
        return
    if password == "":
        messagebox.showerror("Error", "Please enter a password")
        return
    if confirm_password == "":
        messagebox.showerror("Error", "Please confirm your password")
        return

    # Check if username is unique
    with open("accounts.txt", "r") as f:
        accounts = f.readlines()
        for account in accounts:
            if username == account.split(',')[0]:
                messagebox.showerror("Error", "Username already in use. Please choose another username.")
                return

    # Check if password and confirm password match
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match. Please try again.")
        return

    account_info = f"Name: {name}\nGender: {gender}\nContact Information: {contact}\nBirthdate: {birthdate}\nEmail Address: {email}\nUsername: {username}\nPassword: {password}\n\n"

    with open("accounts.txt", "a") as f:
        f.write(account_info)

    messagebox.showinfo("Success", "Your account is successfully signed up!")
    clear_fields()

def clear_fields():
    name_entry.delete(0, tk.END)
    gender_var.set("")
    contact_entry.delete(0, tk.END)
    birthdate_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    confirm_password_entry.delete(0, tk.END)

def view_accounts():
    with open("Signing up an account", "r") as f:
        accounts = f.read()
        if accounts == "":
            messagebox.showinfo("View Accounts", "No accounts to show")
        else:
            messagebox.showinfo("View Accounts", accounts)

# Custom theme
window.config(bg="Light Blue")

# Labels and Entries
name_label = tk.Label(window, text="Name:", bg="Light Blue")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)

gender_label = tk.Label(window, text="Gender:", bg="Light Blue")
gender_label.grid(row=1, column=0)
gender_var = tk.StringVar()
male_radio = tk.Radiobutton(window, text="Male", variable=gender_var, value="Male", bg="Light Blue")
male_radio.grid(row=1, column=1)
female_radio = tk.Radiobutton(window, text="Female", variable=gender_var, value="Female", bg="Light Blue")
female_radio.grid(row=1, column=2)

contact_label = tk.Label(window, text="Contact Information:", bg="Light Blue")
contact_label.grid(row=2, column=0)
contact_entry = tk.Entry(window)
contact_entry.grid(row=2, column=1)

birthdate_label = tk.Label(window, text="Birthdate (MM/DD/YYYY):", bg="Light Blue")
birthdate_label.grid(row=3, column=0)
birthdate_entry = tk.Entry(window)
birthdate_entry.grid(row=3, column=1)

email_label = tk.Label(window, text="Email Address:", bg="Light Blue")
email_label.grid(row=4, column=0)
email_entry = tk.Entry(window)
email_entry.grid(row=4, column=1)

password_label = tk.Label(window, text="Password:", bg="Light Blue")
password_label.grid(row=5, column=0)
password_entry = tk.Entry(window, show="*")
password_entry.grid(row=5, column=1)

confirm_password_label = tk.Label(window, text="Confirm Password:", bg="Light Blue")
confirm_password_label.grid(row=6, column=0)
confirm_password_entry = tk.Entry(window, show="*")
confirm_password_entry.grid(row=6, column=1)

username_label = tk.Label(window, text="Username:", bg="Light Blue")
username_label.grid(row=7, column=0)
username_entry = tk.Entry(window)
username_entry.grid(row=7, column=1)

submit_button = tk.Button(window, text="Submit", command=submit, bg = "light gray")
submit_button.grid(row=8, column=1)

view_accounts_button = tk.Button(window, text="View Accounts", command=view_accounts, bg = "light gray")
view_accounts_button.grid(row=8, column=0)

window.mainloop()
