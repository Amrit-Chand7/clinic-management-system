from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Clinic Management System")
root.geometry("900x600")
root.configure(bg="light blue")  # Light blue

#all functions
# ------------------ Login Function ------------------
def login():
    p = phone_entry.get()
    pas = password_entry.get()
    
    if p == "9745702074" and pas == "amrit@221":
        login_interface = Toplevel()
        login_interface.title("Clinic Management System")
        login_interface.geometry("600x400")
        login_interface.configure(bg="blue")
        after_login_text=Label(login_interface, text="WELCOME TO MY WEB APPLICATION", fg="red", bg="blue", font=("Arial", 18))
        after_login_text.place(x=30, y=30)
    elif not p or not pas:
        messagebox.showerror("Login Failed", "Enter both phone number and password")
    else:
        messagebox.showerror("Login Failed", "Invalid phone number or password")

# ------------------ Register Function ------------------
def register():
    window = Toplevel()
    window.title("Register")
    window.geometry("600x400")
    window.configure(bg="light blue")

    # Create frame
    frame2 = Frame(window, bg="purple")
    frame2.place(relx=0.5, rely=0.5, anchor="center", width=600, height=400)

    # Full Name
    full_name = Label(frame2, text="Full Name:", bg="purple", fg="white", font=("Arial", 16))
    full_name.place(x=60, y=30)
    name_entry = Entry(frame2, font=("Arial", 16), bg="yellow", fg="black",width=25)
    name_entry.place(x=210, y=30)

    # Phone
    phone = Label(frame2, text="Phone:", bg="purple", fg="white", font=("Arial", 16))
    phone.place(x=60, y=80)
    phone_entry = Entry(frame2, font=("Arial", 16),bg="yellow", fg="black", width=25)
    phone_entry.place(x=210, y=80)

    # Email
    email = Label(frame2, text="Email:", bg="purple", fg="white", font=("Arial", 16))
    email.place(x=60, y=130)
    email_entry = Entry(frame2, font=("Arial", 16), bg="yellow", fg="black", width=25)
    email_entry.place(x=210, y=130)

    #Gender
    gender = Label(frame2, text="Gender:", bg="purple", fg="white", font=("Arial", 16))
    gender.place(x=60, y=180)
    gender_entry = Entry(frame2, font=("Arial", 16), bg="yellow", fg="black", width=25)
    gender_entry.place(x=210, y=180)

    # Password
    password1 = Label(frame2, text="Password:", bg="purple", fg="white", font=("Arial", 16))
    password1.place(x=60, y=230)
    password1_entry = Entry(frame2, font=("Arial", 16), show="*", bg="yellow", fg="black", width=25)
    password1_entry.place(x=210, y=230)

    # Confirm Password
    confirm_pass = Label(frame2, text="Confirm Password:", bg="purple", fg="white", font=("Arial", 16))
    confirm_pass.place(x=60, y=280)
    password2_entry = Entry(frame2, font=("Arial", 16), show="*", bg="yellow", fg="black", width=25)
    password2_entry.place(x=210, y=280)


    def popup():
        n = name_entry.get()
        ph = phone_entry.get()
        e = email_entry.get()
        g = gender_entry.get()
        pass1 = password1_entry.get()
        pass2 = password2_entry.get()

        if not n or not ph or not e or not g or not pass1 or not pass2:
            messagebox.showerror("Error", "Fill all the information 😥")
            return

        if pass1 != pass2:
            messagebox.showerror("Error", "Passwords do not match ❌")
            return

        messagebox.showinfo("Congratulations 🎉", "Registered Successfully!")
        name_entry.delete(0, END)
        phone_entry.delete(0, END)
        email_entry.delete(0, END)
        gender_entry.delete(0, END)
        password1_entry.delete(0, END)
        password2_entry.delete(0, END)

    btn_register2=Button(frame2, text="REGISTER", font=("Arial", 16), fg="blue", command=popup)
    btn_register2.place(x=225, y=330)

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
btn_login=Button(frame1, text="Login", font=("Arial", 18), fg="blue",command= login)
btn_login.place(x=390, y=270)

# Register Prompt
register_text=Label(frame1, text="If you don't have an account, please register", font=("Segoe UI", 12), bg="white", fg="#777")
register_text.place(x=290, y=320)

# Register Button
btn_register1=Button(frame1, text="Register", font=("Arial", 14), fg="green",command= register)
btn_register1.place(x=386, y=360)

root.mainloop()