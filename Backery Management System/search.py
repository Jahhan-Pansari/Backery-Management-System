import sqlite3
from tkinter import *
from tkinter import messagebox

def search_by_id(db_file, name_def):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Data WHERE name_of_customer=?", (name_def,))

    row = cursor.fetchone()
    '''
    if row:
        print("\033[2mDetails found:\033[0m")
        print("Name:", row[0])
        print("Items:", row[1])
        print("Cost:", row[2])
        print("Date:", row[3])
    else:
        print("Details not found for ID:", unique_id)'''
    if row:
        result = f"Name: {row[0]}\nItems: {row[1]}\nCost: {row[2]}\nDate: {row[3]}"
        messagebox.showinfo("Search Result", result)
    else:
        messagebox.showinfo("Search Result", "Details not found for the Name: " + name_def)

    conn.close()

root = Tk()
root.geometry("50x50")
root.title("Review Orders")

namevalue = StringVar()
nameeentry = Entry(root, textvariable=namevalue)
nameeentry.pack()

def submitandmessage():
    db_file = 'backery_manage_system1.db'
    name_def = namevalue.get()
    search_by_id(db_file, name_def)

submitbutton = Button(root, text="Submit", command=submitandmessage)
submitbutton.pack()

root.mainloop()

