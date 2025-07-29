from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3

# Sample list of doctors
def appointment_dashboard():
    doctor_list = ["Dr. Amrit Chand Thakuri", "Dr. Rohit Thakur", "Dr. Jharana Adhikari", "Dr. Aman Rauniyar", "Dr. Saffer Shrestha", 
                    "Dr. Jenish Adhikari", "Dr. Aayush Raut"]

    final_window = Toplevel()
    final_window.title("Appointment")
    final_window.geometry("500x470")
    final_window.resizable(False, False)
    final_window.configure(bg="light blue")

    def cancel5():
        messagebox.showinfo("Cancel", "Cancel")
        final_window.destroy()

    number6_label = Label(final_window, text="Phone:", font=("Segoe UI", 17, "bold"),fg= "black" ,bg="light blue")
    number6_label.place(x=68, y=20)

    number6_entry=Entry(final_window,width= 15, text= "", font=("Segoe UI", 17), bg="gray", fg= "white")
    number6_entry.place(x=250, y=20)

    # ------------------ Select Doctor ------------------
    select_label = Label(final_window, text="Select Doctor:", font=("Segoe UI", 18,"bold"), bg="light blue", fg="black")
    select_label.place(x=45, y=70)

    select_doctor = ttk.Combobox(final_window, values=doctor_list, font=("Segoe UI", 16), state="readonly", width=15)
    select_doctor.place(x=250, y=70)
    select_doctor.set("Choose Doctor")

    # ------------------ Date ------------------
    date_label = Label(final_window, text="Date (YYYY-MM-DD):", font=("Segoe UI", 15, "bold"),fg= "black" ,bg="light blue")
    date_label.place(x=25, y=122)

    date_entry=Entry(final_window,width= 15, text= "", font=("Segoe UI", 17), bg="gray", fg= "white")
    date_entry.place(x=250, y=120)

    var1=StringVar()

    def r_btn():

        r1=Radiobutton(final_window,text="10:00 am",variable=var1,value= "10:00 am", bg= "light blue", fg= "black",font=("Arial",14))
        r1.place(x=250,y=170)

        r2=Radiobutton(final_window,text="11:00 am",variable=var1,value= "11:00 am" , bg= "light blue", fg= "black",font=("Arial",14))
        r2.place(x=250,y=220)

        r3=Radiobutton(final_window,text="1:00  pm",variable=var1,value= "1:00 pm", bg= "light blue", fg= "black",font=("Arial",14))
        r3.place(x=250,y=270)

        r4=Radiobutton(final_window,text="2:00  pm",variable=var1, value= "2:00 pm"  , bg= "light blue", fg= "black",font=("Arial",14))
        r4.place(x=250,y=320)

    def save2_btn():
        select_doctor_data= select_doctor.get()
        date_value = date_entry.get()
        var2 = var1.get()
        phone6= number6_entry .get()
        if not date_value or not var2 or not phone6:
            messagebox.showwarning("Warning", "All fields are required")
            return
        
        if select_doctor_data == "Choose Doctor":
            messagebox.showwarning("Warning", "Please select a doctor")
            return
        
        else:
            #connect with database
            conn = sqlite3.connect("clinic_management_system.db")
            c = conn.cursor()
            c.execute("INSERT INTO appointment (doctor, date, time , phone) VALUES (?, ?, ?, ?)",
                    (select_doctor_data, date_value, var2, phone6))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Appointment booked successfully!")
            final_window.destroy()

    # ------------------ Time ------------------
    time_btn = Button(final_window, text="Select Time", fg="blue", font=("Segoe UI", 14), command= r_btn)
    time_btn.place(x=90, y=220)


    # ------------------ Buttons ------------------
    save_btn = Button(final_window, text="Save", font=("Segoe UI", 16), bg="lightgreen", width=10, command = save2_btn)
    save_btn.place(x=55, y=365)

    cancel_btn = Button(final_window, text="Cancel", font=("Segoe UI", 16), bg="lightcoral", width=10, command=cancel5)
    cancel_btn.place(x=235, y=365)
    
    