import tkinter
from tkinter import *
from tkinter import ttk
import sqlite3

# Initialize the database and create table if it doesn't exist
def initialize_db():
    with sqlite3.connect("Student.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Student(
                          ID INTEGER PRIMARY KEY,
                          NAME TEXT,
                          AGE INTEGER,
                          DOB TEXT,
                          GENDER TEXT,
                          CITY TEXT)""")
        conn.commit()

class Student:
    def __init__(self, root):
        self.root = root
        self.setup_ui()
        initialize_db()
        self.load_data()

    def setup_ui(self):
        self.T_Frame = Frame(self.root, height=60, width=1200, background="sky blue", bd=2, relief=GROOVE)
        self.T_Frame.pack(fill=X)
        self.Title = Label(self.T_Frame, text="Student Management System", font="arial 20 bold", background="sky blue")
        self.Title.pack(pady=10)

        self.Frame_1 = Frame(self.root, height=600, width=400, background="sky blue", bd=2, relief=GROOVE)
        self.Frame_1.pack(side=LEFT, fill=Y, padx=10, pady=10)

        self.labels_entries = {}
        fields = ["ID", "Name", "Age", "DOB", "Gender", "City"]
        for idx, field in enumerate(fields):
            Label(self.Frame_1, text=field, font="arial 12 bold", background="sky blue").grid(row=idx, column=0, padx=10, pady=5, sticky=W)
            self.labels_entries[field] = Entry(self.Frame_1, font="arial 12", width=40)
            self.labels_entries[field].grid(row=idx, column=1, padx=10, pady=5)

        self.Button_Frame = Frame(self.Frame_1, background="sky blue")
        self.Button_Frame.grid(row=len(fields), column=0, columnspan=2, pady=10)

        Button(self.Button_Frame, text="Add", width=25, font="arial 11 bold", command=self.add).pack(pady=5)
        Button(self.Button_Frame, text="Delete", width=25, font="arial 11 bold", command=self.delete).pack(pady=5)
        Button(self.Button_Frame, text="Update", width=25, font="arial 11 bold", command=self.update).pack(pady=5)
        Button(self.Button_Frame, text="Clear", width=25, font="arial 11 bold", command=self.clear).pack(pady=5)

        self.Frame_2 = Frame(self.root, height=600, width=800, background="sky blue", bd=2, relief=GROOVE)
        self.Frame_2.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(self.Frame_2, columns=("ID", "Name", "Age", "DOB", "Gender", "City"), show="headings", height=25)
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=CENTER, width=120 if col != "ID" else 100)

        self.tree.pack(fill=BOTH, expand=True)

    def load_data(self):
        self.tree.delete(*self.tree.get_children())
        with sqlite3.connect("Student.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Student")
            for row in cursor.fetchall():
                self.tree.insert("", "end", values=row)

    def add(self):
        data = {field: entry.get() for field, entry in self.labels_entries.items()}
        with sqlite3.connect("Student.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Student (ID, NAME, AGE, DOB, GENDER, CITY) VALUES (?, ?, ?, ?, ?, ?)",
                           (data['ID'], data['Name'], data['Age'], data['DOB'], data['Gender'], data['City']))
            conn.commit()
        self.load_data()

    def delete(self):
        selected_item = self.tree.selection()[0]
        id = self.tree.item(selected_item)['values'][0]
        with sqlite3.connect("Student.db") as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Student WHERE ID=?", (id,))
            conn.commit()
        self.tree.delete(selected_item)
        print("Value Deleted")

    def update(self):
        data = {field: entry.get() for field, entry in self.labels_entries.items()}
        selected_item = self.tree.selection()[0]
        id = self.tree.item(selected_item)['values'][0]
        with sqlite3.connect("Student.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""UPDATE Student 
                              SET NAME=?, AGE=?, DOB=?, GENDER=?, CITY=? 
                              WHERE ID=?""",
                           (data['Name'], data['Age'], data['DOB'], data['Gender'], data['City'], id))
            conn.commit()
        self.load_data()

    def clear(self):
        for entry in self.labels_entries.values():
            entry.delete(0, END)


root = Tk()
root.title("Student Management System")
root.resizable(False, False)
root.geometry("1200x600")
Student(root)
root.mainloop()