from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from admin_interface import admin_dashboard  
import sqlite3

root = Tk()
root.title("Clinic Management System")
root.geometry("900x600")
root.configure(bg="light blue")  # Light blue

#all functions
# ------------------ Database Setup ------------------

conn = sqlite3.connect("clinic_management_system.db")
c = conn.cursor()
c.execute(''' 
    CREATE TABLE IF NOT EXISTS clinic_record (
        full_name TEXT(20),
        phone TEXT(10),
        date_of_birth TEXT(30),
        gender TEXT(30),
        password TEXT(30),
        confirm_password TEXT(30)
    )
''')

conn.commit()
conn.close()



# ------------------ Login Function ------------------
def login():
    p = phone_entry.get()
    pas = password_entry.get()
    
    if p == "97" and pas == "a":
        
        admin_dashboard()
    elif not p or not pas:
        messagebox.showerror("Login Failed", "Enter both phone number and password")
    else:
        messagebox.showerror("Login Failed", "Invalid phone number or password")

# ------------------ Register Function ------------------
def register():
    window = Toplevel()
    window.title("Register")
    window.geometry("600x400")
    window.resizable(False, False)

    # Create frame
    frame2 = Frame(window, bg="light blue")
    frame2.place(relx=0.5, rely=0.5, anchor="center", width=600, height=400)

    # Full Name
    full_name = Label(frame2, text="Full Name:", bg="white", fg="black", font=("Arial", 16))
    full_name.place(x=60, y=30)
    name_entry = Entry(frame2, font=("Arial", 16), bg="white", fg="black",width=25)
    name_entry.place(x=245, y=30)

    # Phone
    phone = Label(frame2, text="Phone:", bg="white", fg="black", font=("Arial", 16))
    phone.place(x=60, y=80)
    phone_entry = Entry(frame2, font=("Arial", 16),bg="white", fg="black", width=25)
    phone_entry.place(x=245, y=80)

    # Date of Birth
    birth = Label(frame2, text="Date of Birth:", bg="white", fg="black", font=("Arial", 16))
    birth.place(x=60, y=130)
    birth_entry = Entry(frame2, font=("Arial", 16), bg="white", fg="black", width=25)
    birth_entry.place(x=245, y=130)

    #Gender

    gender_label = Label(frame2, text="Gender:", bg="white", fg="black", font=("Arial", 16))
    gender_label.place(x=60, y=180)

    gender_var = StringVar()
    gender_var.set("Male")

    male_rb = Radiobutton(frame2, text="Male", variable=gender_var, value="Male", font=("Arial", 12), bg="white", fg="black", selectcolor="white")
    male_rb.place(x=245, y=180)

    female_rb = Radiobutton(frame2, text="Female", variable=gender_var, value="Female", font=("Arial", 12), bg="white", fg="black", selectcolor="white")
    female_rb.place(x=320, y=180)

    other_rb = Radiobutton(frame2, text="Other", variable=gender_var, value="Other", font=("Arial", 12), bg="white", fg="black", selectcolor="white")
    other_rb.place(x=410, y=180)


    # Password
    password1 = Label(frame2, text="Password:", bg="white", fg="black", font=("Arial", 16))
    password1.place(x=60, y=230)
    password1_entry = Entry(frame2, font=("Arial", 16), show="*", bg="white", fg="black", width=25)
    password1_entry.place(x=245, y=230)

    # Confirm Password
    confirm_pass = Label(frame2, text="Confirm Password:", bg="white", fg="black", font=("Arial", 16))
    confirm_pass.place(x=60, y=280)
    password2_entry = Entry(frame2, font=("Arial", 16), show="*", bg="white", fg="black", width=25)
    password2_entry.place(x=245, y=280)


    def popup():
        n = name_entry.get()
        g= gender_var.get()
        ph = phone_entry.get()
        d = birth_entry.get()

        pass1 = password1_entry.get()
        pass2 = password2_entry.get()

        if not n or not ph or not d or not g or not pass1 or not pass2:
            messagebox.showerror("Error", "Fill all the information 😥")
            return

        if pass1 != pass2:
            messagebox.showerror("Error", "Passwords do not match ❌")
            return
        
        conn = sqlite3.connect("clinic_management_system.db")
        c = conn.cursor()
        c.execute('''
            INSERT INTO clinic_record(full_name, phone, date_of_birth, gender, password, confirm_password)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (n, ph, d, g, pass1, pass2))
        conn.commit()
        conn.close()

        messagebox.showinfo("Congratulations 🎉", "Registered Successfully!")

        #destroy the registration window after successful registration
        window.destroy()


    btn_register2=Button(frame2, text="REGISTER", font=("Arial", 18), fg="blue", command=popup)
    btn_register2.place(x=283, y=335)

# ------------------ Login Frame -----------
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
btn_login=Button(frame1, text="Login", font=("Arial", 18), fg="blue",command= login)
btn_login.place(x=390, y=270)

# Register Prompt
register_text=Label(frame1, text="If you don't have an account, please register", font=("Segoe UI", 12), bg="white", fg="#777")
register_text.place(x=290, y=320)

# Register Button
btn_register1=Button(frame1, text="Register", font=("Arial", 14), fg="green",command= register)
btn_register1.place(x=386, y=360)

root.mainloop()