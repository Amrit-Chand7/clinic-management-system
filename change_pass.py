import sqlite3
from tkinter import *
from tkinter import messagebox

# Function to handle password update
def change_password():
    # Main window
    password_window = Toplevel()
    password_window.title("Change Password")
    password_window.geometry("500x400")
    password_window.configure(bg="light blue")
    password_window.resizable(False, False)

    # Labels and Entry fields
    num1_label = Label(password_window, text="Number:", bg="light blue", font=("Arial", 15),fg="black")
    num1_label.place(x=65, y=20)
    num1_entry = Entry(password_window, font=("Arial", 12),bg="white", fg="black", width=25)
    num1_entry.place(x=225, y=20)


    old_label = Label(password_window, text="Old Password:", bg="light blue", font=("Arial", 15),fg="black")
    old_label.place(x=50, y=60)
    old_pass_entry = Entry(password_window, font=("Arial", 12),bg="white", fg="black", width=25, show="*")
    old_pass_entry.place(x=225, y=60)

    new_label = Label(password_window, text="New Password:", bg="light blue", fg="black", font=("Arial", 15))
    new_label.place(x=50, y=100)
    new_pass_entry = Entry(password_window, font=("Arial", 12), bg="white", fg="black", width=25, show="*")
    new_pass_entry.place(x=225, y=100)

    confirm_label = Label(password_window, text="Confirm Password:", bg="light blue", fg="black", font=("Arial", 15))
    confirm_label.place(x=50, y=140)
    confirm_pass_entry = Entry(password_window, font=("Arial", 12), bg="white", fg="black", width=25, show="*")
    confirm_pass_entry.place(x=225, y=140)


    old_password = old_pass_entry.get()
    new_password = new_pass_entry.get()
    confirm_password = confirm_pass_entry.get()
    if old_password and new_password and confirm_password:
        if new_password == confirm_password:
            messagebox.showinfo("Password Change Successful", "Your password has been changed!")
        else:
            messagebox.showwarning("Error", "New passwords do not match!")
    
    # Function to handle cancellation
    def save():
        result = messagebox.askyesno("Save", "Are you sure you want to change your password?")
        if result==True:
            messagebox.showinfo("Success", "Password changed successfully!")
            password_window.destroy()

        else:
            messagebox.showinfo("Cancelled", "Password change cancelled.")

    save_btn = Button(password_window, text="Save", font=("Arial", 12), width=12, command=save)
    save_btn.place(x=130, y=210)