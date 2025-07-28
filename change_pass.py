import sqlite3
from tkinter import *
from tkinter import messagebox


# Function to handle password update
def change_password():
    # Main window
    password_window = Toplevel()
    password_window.title("Change Password")
    password_window.geometry("500x300")
    password_window.configure(bg="light blue")
    password_window.resizable(False, False)

    # Labels and Entry fields
    num1_label = Label(password_window, text="Number:", bg="light blue", font=("Arial", 15),fg="black")
    num1_label.place(x=50, y=20)
    num1_entry = Entry(password_window, font=("Arial", 12),bg="white", fg="black", width=25)
    num1_entry.place(x=228, y=20)


    old_label = Label(password_window, text="Old Password:", bg="light blue", font=("Arial", 15),fg="black")
    old_label.place(x=50, y=60)
    old_pass_entry = Entry(password_window, font=("Arial", 12),bg="white", fg="black", width=25, show="*")
    old_pass_entry.place(x=228, y=60)

    new_label = Label(password_window, text="New Password:", bg="light blue", fg="black", font=("Arial", 15))
    new_label.place(x=50, y=100)
    new_pass_entry = Entry(password_window, font=("Arial", 12), bg="white", fg="black", width=25, show="*")
    new_pass_entry.place(x=228, y=100)

    confirm_label = Label(password_window, text="Confirm Password:", bg="light blue", fg="black", font=("Arial", 15))
    confirm_label.place(x=50, y=140)
    confirm_pass_entry = Entry(password_window, font=("Arial", 12), bg="white", fg="black", width=25, show="*")
    confirm_pass_entry.place(x=228, y=142)

    # Function to handle cancellation
    def save():
        phone_n = num1_entry.get()
        old_password = old_pass_entry.get()
        new_password = new_pass_entry.get()
        confirm_password = confirm_pass_entry.get()

        if not phone_n or not old_password or not new_password or not confirm_password:
            messagebox.showwarning("Warning", "All fields are required")
            return
        
        if new_password != confirm_password:
                messagebox.showerror("Error", "New passwords do not match")
                return
        
        conn = sqlite3.connect("clinic_management_system.db")
        c = conn.cursor()

        c.execute("SELECT password FROM admin WHERE phone = ?", (phone_n,))
        result = c.fetchone()
       
        if result == None:
            messagebox.showerror("Error", "Phone number not found")
            return
        
        if result[0] != old_password:
            messagebox.showerror("Error", "Old password is incorrect")
            return
        
        # update the password
        c.execute("UPDATE admin SET password = ? WHERE phone = ?", (new_password, phone_n))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Password changed successfully!")
        password_window.destroy()

    save_btn = Button(password_window, text="Save", font=("Arial", 16), fg="green", width=8, command=save)
    save_btn.place(x=120, y=210)

    cancel_btn4 = Button(password_window, text="Cancel", font=("Segoe UI", 16), bg="lightcoral", width=8, command=password_window.destroy)
    cancel_btn4.place(x=270, y=210)
