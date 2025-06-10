import tkinter as tk
def loginpage():
    root.destroy()
    import login
"""def open_teacher_form():
    print("Teacher Form")

"""
# Create the main window
root = tk.Tk()
root.title("College Form")
root.resizable(False, False)
root.geometry('1200x600')
root.configure(bg='#333333')
title_label = tk.Label(root, text="Student Management System", font="arial 20 bold", bg='#333333', fg="sky blue",)
title_label.pack(pady=30)

# Create a frame for the buttons
frame = tk.Frame(root, bg='#333333')
frame.pack(pady=30)

# Create and place the Teacher button
teacher_button = tk.Button(frame, text="Teacher", padx=70, pady=10, background="sky blue",command=loginpage)
teacher_button.pack(pady=10)


root.mainloop()
