from tkinter import *
from PIL import Image, ImageTk

# ------- Admin Dashboard ---------
admin = Tk()
admin.title("Admin Dashboard")
admin.geometry("900x600")
admin.configure(bg="light blue")

admin_frame = Frame(admin, bg="white")
admin_frame.place(relx=0.5, rely=0.5, anchor="center", width=880, height=560)

# ------------------ All Functions ------------------
def manage_doctors():
    doctor = Toplevel(admin)
    doctor.title("Manage Doctors")
    doctor.geometry("800x800")
    doctor.configure(bg="light blue")
    doctor.resizable(False, False)

    add_frame = Frame(doctor, bg="white") 
    add_frame.place(relx=0.27, rely=0.1, width=390, height=280) 

    # ---------- Add Doctor Section ----------
    add_label = Label(add_frame, text="Add Doctor",bg= "white", fg="black" ,font=("Arial", 18, "bold"))
    add_label.place(x=110,y=10)

    name_label = Label(add_frame, text="Name:", fg="black",bg="white", font=("Arial", 13))
    name_label.place(x=20, y=60)
    add_name_entry = Entry(add_frame, width=20,bg="white", fg="black")
    add_name_entry.place(x=140, y=60)

    spec_label = Label(add_frame, text="Specialization:", fg="black",bg="white",font=("Arial", 13))
    spec_label.place(x=20, y=105)
    add_spec_entry = Entry(add_frame, width=20,bg="white", fg="black")
    add_spec_entry.place(x=140, y=103)

    number_label = Label(add_frame, text="Phone Number:", fg="black", bg="white", font=("Arial", 13))
    number_label.place(x=20, y=153)
    number_spec_entry = Entry(add_frame, width=20,bg="white", fg="black")
    number_spec_entry.place(x=140, y=150)
    

    btn_save = Button(add_frame, text="Save", fg="Green", width=12, font=("Arial", 14))
    btn_save.place(x=100, y=200)
    
    #doctor frame 
    remove_frame = Frame(doctor, bg="white") 
    remove_frame.place(relx=0.27, rely=0.5, width=390, height=280) 

    # ---------- Remove doctor ----------
    remove_label = Label(remove_frame, text="Remove Doctor",bg= "white", fg="black", font=("Arial", 18, "bold"))
    remove_label.place(x=85,y=20)

    phone_num_label = Label(remove_frame, text="Phone number:", fg="black",bg="white", font=("Arial", 14))
    phone_num_label.place(x=25, y=90)
    phone_num_entry = Entry(remove_frame, width=20,bg="white",fg="black")
    phone_num_entry.place(x=150, y=88)

    btn_del = Button(remove_frame, text="Delete", fg="blue", width=12, font=("Arial", 14))
    btn_del.place(x=100, y=160)



# ------------------ Image ------------------
img = Image.open("image/admin.jpg")
img = img.resize((880, 560))
photo = ImageTk.PhotoImage(img)
img_label = Label(admin_frame, image=photo)
img_label.place(x=0, y=0)

#  Buttons on Left
manage_doctors_btn = Button(admin_frame, text="Manage Doctor", font=("Arial", 14), width=18, command=manage_doctors)
manage_doctors_btn.place(x=30, y=150)

admin_pass_change = Button(admin_frame, text="Change Password", font=("Arial", 14), width=18)
admin_pass_change.place(x=30, y=220)

admin_logout_btn = Button(admin_frame, text="Log Out", font=("Arial", 14), width=18, fg="red")
admin_logout_btn.place(x=30, y=290)

admin.mainloop()