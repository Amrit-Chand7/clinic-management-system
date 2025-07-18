from tkinter import *
from PIL import Image, ImageTk

# ------- Admin Dashboard ---------
admin = Tk()
admin.title("Admin Dashboard")
admin.geometry("900x600")
admin.configure(bg="light blue")

admin_frame = Frame(admin, bg="white")
admin_frame.place(relx=0.5, rely=0.5, anchor="center", width=880, height=560)

# Image on right side
img = Image.open("image/admin.jpg")
img = img.resize((880, 560))
photo = ImageTk.PhotoImage(img)
img_label = Label(admin_frame, image=photo)
img_label.place(x=0, y=0)

# ----------- Buttons on left -----------
manage_doctors_btn = Button(admin_frame, text="Manage Doctor", font=("Arial", 14), width=18)
manage_doctors_btn.place(x=50, y=100)

admin_pass_change= Button(admin_frame, text="Change Password", font=("Arial", 14), width=18)
admin_pass_change.place(x=50, y=180)

admin_logout_btn = Button(admin_frame, text="Log Out", font=("Arial", 14), width=18, fg="red")
admin_logout_btn.place(x=50, y=260)

admin.mainloop()