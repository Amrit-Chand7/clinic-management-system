from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Clinic Management System")
root.geometry("900x600")
root.configure(bg="light blue")  # Light blue

# ------------------ Login Frame ------------------
frame1 = Frame(root, bg="white")
frame1.place(relx=0.5, rely=0.5, anchor="center", width=700, height=450)

# ------------------ Image ------------------
img = Image.open("image/WhatsApp Image 2025-07-17 at 10.15.11_0c179260.jpg")
img = img.resize((250, 450))
photo = ImageTk.PhotoImage(img)
img_label = Label(frame1, image=photo)
img_label.place(x=0, y=0)

# ------------------ Login Form ------------------
form_bg = Frame(frame1, bg="white")
form_bg.place(x=260, y=0, width=440, height=450)

title = Label(form_bg, text="Welcome to Clinic System", font=("Segoe UI", 18, "bold"), bg="white", fg="#333")
title.place(x=50, y=30)

# Phone Number Label & Entry
phone_number = Label(form_bg, text="Phone Number", font=("Segoe UI", 14), bg="white", fg="#555")
phone_number.place(x=50, y=100)
phone_entry = Entry(form_bg, font=("Segoe UI", 14), width=30, bg="#eef", fg="black")
phone_entry.place(x=50, y=130)

# Password Label & Entry
password = Label(form_bg, text="Password", font=("Segoe UI", 14), bg="white", fg="#555")
password.place(x=50, y=180)
password_entry = Entry(form_bg, font=("Segoe UI", 14), show="*", width=30, bg="#eef", fg="black")
password_entry.place(x=50, y=210)

# Login Button
btn_login=Button(frame1, text="Login", font=("Arial", 18), fg="blue")
btn_login.place(x=390, y=270)

# Register Prompt
register_text=Label(frame1, text="If you don't have an account, please register", font=("Segoe UI", 12), bg="white", fg="#777")
register_text.place(x=290, y=320)

# Register Button
btn_register1=Button(frame1, text="Register", font=("Arial", 14), fg="green")
btn_register1.place(x=386, y=360)

root.mainloop()