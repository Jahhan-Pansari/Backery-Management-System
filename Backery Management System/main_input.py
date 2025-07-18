import sqlite3
from tkinter import *
from datetime import datetime

def SaveData():
    global Name_of_customer, Item_buyed, Bill_cost
    Name_of_customer = customernameentry.get()
    Item_buyed = itemsbuyedvalue.get()
    Bill_cost = billingcostvalue.get()

    sql_query = "CREATE TABLE IF NOT EXISTS Data (name_of_customer TEXT, item_buyed TEXT, bill_cost TEXT, date TEXT, unique_id TEXT);"
    c.execute(sql_query)
    sql_insert_data = '''
        INSERT INTO Data VALUES(?,?,?,?,?);
    '''

    table_name = "Data"
    def count_rows(table_name):
        c.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = c.fetchone()[0]
        return count
    row_count = count_rows(table_name)

    id_unique = row_count + 1

    current_datetime = datetime.now()
    formatted_date = current_datetime.strftime("%d/%m/%Y")

    c.execute(sql_insert_data, (Name_of_customer, Item_buyed, Bill_cost, formatted_date, id_unique))
    conn.commit()
    print("Data Stored Successfully")
    root.destroy()

root = Tk()
root.title("Backery System")
root.geometry("300x300")
root.resizable(False, False)

conn = sqlite3.connect('backery_manage_system1.db')
c = conn.cursor()

heading = Label(root, text="Welcome to the Backery", font=("Helvetica", 12, "bold"))
heading.pack(padx=5, pady=5)

label1 = Label(root, text="Customer Name", font=("Helvetica", 8))
label1.pack(anchor=NW, pady=5)

customernamevalue = StringVar()
customernameentry = Entry(root, textvariable=customernamevalue)
customernameentry.pack(anchor=NW, padx=3)

label2 = Label(root, text="Items Buyed", font=("Helvetica", 8))
label2.pack(anchor=NW, pady=5)

itemsbuyedvalue = StringVar()
itemsbuyedentry = Entry(root, textvariable=itemsbuyedvalue, width=20)
itemsbuyedentry.pack(anchor=NW, padx=3)

label3 = Label(root, text="Billing Cost", font=("Helvetica", 8))
label3.pack(anchor=NW, pady=5)

billingcostvalue = StringVar()
billingcostentry = Entry(root, textvariable=billingcostvalue, width=20)
billingcostentry.pack(anchor=NW, padx=3)

button1 = Button(root, text="Add Data", command=SaveData)
button1.pack(anchor=NW, pady=5, padx=3)

root.mainloop()
conn.commit()
conn.close()
