from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

patient = Tk()
patient.title("Patient Dashboard")
patient.geometry("900x600")
patient.configure(bg="light blue")

patient_frame = Frame(patient, bg="white")
patient_frame.place(relx=0.5, rely=0.5, anchor="center", width=880, height=560)

img = Image.open("image/admin.jpg")
img = img.resize((900, 600))
photo = ImageTk.PhotoImage(img)
img_label = Label(patient_frame, image=photo)
img_label.place(x=0, y=0)

appointment_btn = Button(patient_frame, text="Appointment", font=("Arial", 14), width=18)
appointment_btn.place(x=50, y=100)

prescription_btn = Button(patient_frame, text="Prescription", font=("Arial", 14), width=18)
prescription_btn.place(x=50, y=180)

password_btn = Button(patient_frame, text="Change Password", font=("Arial", 14), width=18)
password_btn.place(x=50, y=260)

logout_btn = Button(patient_frame, text="Log Out", font=("Arial", 14), width=18, fg="red")
logout_btn.place(x=50, y=340)


patient.mainloop()
