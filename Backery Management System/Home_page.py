from tkinter import *
import subprocess
root = Tk()
root.geometry("200x100")
root.title("Backery Home")
root.resizable(False, False)

def search_button():
    subprocess.run(["python", "search.py"])

def new_order_button():
    subprocess.run(["python", "main_input.py"])

def quit():
    root.destroy()

Search_button = Button(text="Review Orders", command=search_button)
Search_button.pack(fill=X)

New_Order_button = Button(text="New Order", command=new_order_button)
New_Order_button.pack(fill=X)

Quit_button = Button(text="Quit", command=quit)
Quit_button.pack(fill=X)

root.mainloop()