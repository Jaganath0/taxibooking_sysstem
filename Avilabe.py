from tkinter import *
from tkinter import messagebox, ttk
import os

import mysql.connector


class avilable:
    def __init__(self, root):
        self.root = root
        self.root.geometry("750x300")
        self.root.resizable(False, False)
        # self.bg = PhotoImage(file="image.png")
        # self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0)

        self.frame = Frame(self.root, width=700, height=200, bg="red")
        self.frame.place(x=25, y=50)

        self.tbl_frm = Frame(self.root, width=800, height=500)
        self.tbl_frm.place(x=100, y=300, width=900)

        scroll_x = Scrollbar(self.frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.frame, orient=VERTICAL)
        self.user_table = ttk.Treeview(self.frame, columns=(
        "driverid", "name", "citizen", "license", "contact", "driver_status",)
                                       , xscrollcommand=scroll_x.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.user_table.xview)
        scroll_y.config(command=self.user_table.yview)
        self.user_table.heading("driverid", text="Id")
        self.user_table.heading("name", text="Name")
        self.user_table.heading("citizen", text="Citizen")
        self.user_table.heading("license", text="License")
        self.user_table.heading("contact", text="Contact")
        self.user_table.heading("driver_status", text="Status")

        self.user_table['show'] = 'headings'
        self.user_table.column("driverid", width=100, anchor=CENTER)
        self.user_table.column("name", width=100, anchor=CENTER)
        self.user_table.column("citizen", width=100, anchor=CENTER)
        self.user_table.column("license", width=100, anchor=CENTER)
        self.user_table.column("contact", width=100, anchor=CENTER)
        self.user_table.column("driver_status", width=100, anchor=CENTER)

        self.user_table.pack(fill=BOTH, expand=3)
        self.fetch_data()

        self.root.mainloop()

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="booking")
        cursor = conn.cursor()


        cursor.execute("SELECT driverid, name, citizen, license, contact,driver_status FROM driver")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.user_table.delete(*self.user_table.get_children())
            for row in rows:
                self.user_table.insert('', END, values=row)
                conn.commit()
        conn.close()

    def cancel_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="booking")
        cursor = conn.cursor()
        selected_item = self.user_table.selection()[0]
        book_id = self.user_table.item(selected_item)['values'][0]
        cursor.execute("Update book set status='Cancelled' where book_id=%s", (book_id,))
        conn.commit()
        self.fetch_data()
        messagebox.showinfo("Success", "Booking Cancelled Sucessfully")


# if __name__ == '__main__':
#     root = Tk()
#     obj = avilable(root)
#     root.mainloop()
