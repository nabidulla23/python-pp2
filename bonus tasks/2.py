import re
import tkinter as tk


email_regex = re.compile(r"[^@]+@(gmail|mail)\.com$")


def register():
    
    email = email_entry.get()
    login = login_entry.get()
    password = password_entry.get()

    
    if not email_regex.match(email):
        error_label.config(text="Invalid email address")
        return

    
    with open("database.txt", "r") as f:
        for line in f:
            existing_login = line.split()[1]
            if existing_login == login:
                error_label.config(text="Login already taken")
                return

    
    with open("database.txt", "a") as f:
        f.write(f"{email} {login} {password}\n")


    email_entry.delete(0, tk.END)
    login_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    error_label.config(text="Registration successful")