import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw

def verify_login():
    """Function to verify user login credentials."""
    user_id = entry_user_id.get()
    password = entry_password.get()
    if user_id and password:
        messagebox.showinfo("Success", "Login Successful!")
    else:
        messagebox.showerror("Error", "Please enter all fields!")

def create_rounded_rectangle(width, height, radius, color):
    """Creates an image of a rounded rectangle."""
    image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((0, 0, width, height), radius=radius, fill=color)
    return ImageTk.PhotoImage(image)

# Initialize the main application window
root = tk.Tk()
root.title("Student Login")
root.geometry("1440x1024")
root.configure(bg="white")

# Title: Student Log In
title_label = tk.Label(root, text="STUDENT\nLOG IN", font=("Arial", 36, "bold"), fg="red", bg="white", justify="left")
title_label.place(x=80, y=400)

# Login Form Background (rounded rectangle)
form_background_image = create_rounded_rectangle(560, 400, 20, "#E0E0E0")
form_background_label = tk.Label(root, image=form_background_image, bg="white")
form_background_label.place(x=450, y=312)

# User ID Entry
entry_user_id = tk.Entry(root, font=("Arial", 18), width=22, bg="white", fg="gray", relief="flat")
entry_user_id.insert(0, "Userid/usn")
entry_user_id.place(x=530, y=370)

# Password Entry
entry_password = tk.Entry(root, font=("Arial", 18), width=22, bg="white", fg="gray", relief="flat", show="*")
entry_password.insert(0, "Password")
entry_password.place(x=530, y=430)

# Forgot Password Link
forgot_password_label = tk.Label(root, text="forgot password?", font=("Arial", 12, "italic"), bg="#E0E0E0", fg="gray")
forgot_password_label.place(x=530, y=480)

# Captcha Checkbox
captcha_checkbox = tk.Checkbutton(root, text="captcha verification", font=("Arial", 14), bg="#E0E0E0", relief="flat")
captcha_checkbox.place(x=530, y=520)

# Login Button (rounded rectangle for button background)
button_image = create_rounded_rectangle(200, 50, 25, "red")
login_button_bg = tk.Label(root, image=button_image, bg="#E0E0E0")
login_button_bg.place(x=630, y=580)

# Login Button Text
login_button = tk.Button(root, text="LOG IN", font=("Arial", 18, "bold"), bg="red", fg="white", relief="flat", command=verify_login)
login_button.place(x=660, y=590)

# Start the application
root.mainloop()
