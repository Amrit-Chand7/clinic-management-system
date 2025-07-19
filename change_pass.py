from tkinter import *
from tkinter import messagebox

# Function to handle password update
def change_password():
    old_password = old_pass_entry.get()
    new_password = new_pass_entry.get()
    confirm_password = confirm_pass_entry.get()

    # Validate if all fields are filled
    if old_password and new_password and confirm_password:
        if new_password == confirm_password:
            messagebox.showinfo("Password Change Successful", "Your password has been changed!")
        else:
            messagebox.showwarning("Error", "New passwords do not match!")
    else:
        messagebox.showwarning("Error", "All fields are required!")

# Function to handle cancellation
def cancel():
    result = messagebox.askyesno("Cancel", "Are you sure you want to cancel?")
    if result:
        password_window.destroy()

# Main window
password_window = Tk()
password_window.title("Change Password")
password_window.geometry("500x400")
password_window.configure(bg="light blue")
password_window.resizable(False, False)

# Labels and Entry fields
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

# Buttons
change_btn = Button(password_window, text="Save", font=("Arial", 12), width=12, command=change_password)
change_btn.place(x=100, y=210)

cancel_btn = Button(password_window, text="Cancel", font=("Arial", 12), width=12, command=cancel)
cancel_btn.place(x=230, y=210)

password_window.mainloop()