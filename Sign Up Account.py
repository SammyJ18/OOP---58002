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

    with open("Signing Up an Account", "a") as f:
        f.write(f"{name},{gender},{contact},{birthdate},{email}\n")

    messagebox.showinfo("Success", "Your account is successfully signed up!")

name_label = tk.Label(window, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)

gender_label = tk.Label(window, text="Gender:")
gender_label.grid(row=1, column=0)
gender_var = tk.StringVar()
male_radio = tk.Radiobutton(window, text="Male", variable=gender_var, value="Male")
male_radio.grid(row=1, column=1)
female_radio = tk.Radiobutton(window, text="Female", variable=gender_var, value="Female")
female_radio.grid(row=1, column=2)

contact_label = tk.Label(window, text="Contact Information:")
contact_label.grid(row=2, column=0)
contact_entry = tk.Entry(window)
contact_entry.grid(row=2, column=1)

birthdate_label = tk.Label(window, text="Birthdate (DD/MM/YYYY):")
birthdate_label.grid(row=3, column=0)
birthdate_entry = tk.Entry(window)
birthdate_entry.grid(row=3, column=1)

email_label = tk.Label(window, text="Email Address:")
email_label.grid(row=4, column=0)
email_entry = tk.Entry(window)
email_entry.grid(row=4, column=1)

submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.grid(row=5, column=1)

window.mainloop()

submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack()


window.mainloop()
