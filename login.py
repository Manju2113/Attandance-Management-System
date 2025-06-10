import tkinter 
import tkinter as tk
from tkinter import  messagebox
def table():
    window.destroy()
    import studentdatabase

window = tkinter.Tk()
window.title("Login Form")
window.geometry('1200x600')
window.configure(bg='#333333')
title_label = tk.Label(window, text="Teacher  Management System", font="arial 30 bold", bg='#333333', fg="sky blue",)
title_label.pack(pady=40)


def login():
    username = "ilavendhan"
    password = "1234"
    if username_entry.get()==username and password_entry.get()==password  :
        messagebox.showinfo("Login Success","Login Success")
        table()
    else:
        messagebox.showerror(title = " Error", message = "Invalid Username or Password")

frame =tkinter.Frame(bg='#333333')
login_label = tkinter.Label(frame, text="Login", bg='#333333', fg="sky blue", font=('Arial', 30))
username_label = tkinter.Label(frame, text="Username", bg='#333333', fg="#FFFFFF", font=('Arial', 16))
username_entry = tkinter.Entry(frame, font=('Arial', 16))
password_entry = tkinter.Entry(frame, show="*", font=('Arial', 16))
password_label = tkinter.Label(frame, text="Password", bg='#333333', fg="#FFFFFF", font=('Arial', 16))
login_button = tkinter.Button(frame, text="Login", bg='#333333', fg="sky blue", font=('Arial', 15), command=login)

login_label.grid(row=0, column=0, columnspan=3, padx=30)
username_label.grid(row=2, column=0)
username_entry.grid(row=2, column=1, padx=20)
password_label.grid(row=4, column=0)
password_entry.grid(row=4, column=1, padx=20)
login_button.grid(row=7, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()
