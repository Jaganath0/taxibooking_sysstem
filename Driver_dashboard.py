import os
from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector


class driver:

    def __init__(self,root,username):

        self.root = root
        self.username = username
        self.root.geometry("800x600")
        self.root.resizable(True, True)

        # self.bg = PhotoImage(file="image.png")
        # self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0)


        #frame and table 1
        self.frame = Frame(self.root,width=700,height=200,bg="red")
        self.frame.place(x=50,y=350)

        scroll_x = Scrollbar(self.frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.frame, orient=VERTICAL)
        self.user_table = ttk.Treeview(self.frame, columns=(
        "id", "name", "pickup_location", "drop_address", "date", "time", "status",)
                                       , xscrollcommand=scroll_x.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.user_table.xview)
        scroll_y.config(command=self.user_table.yview)
        self.user_table.heading("id", text="Id")
        self.user_table.heading("name", text="Name")
        self.user_table.heading("pickup_location", text="Pickup Location")
        self.user_table.heading("drop_address", text="Drop address")
        self.user_table.heading("date", text="Date")
        self.user_table.heading("time", text="Time")
        self.user_table.heading("status", text="Status")

        self.user_table['show'] = 'headings'
        self.user_table.column("id", width=100, anchor=CENTER)
        self.user_table.column("name", width=100, anchor=CENTER)
        self.user_table.column("pickup_location", width=100, anchor=CENTER)
        self.user_table.column("drop_address", width=100, anchor=CENTER)
        self.user_table.column("date", width=100, anchor=CENTER)
        self.user_table.column("time", width=100, anchor=CENTER)
        self.user_table.column("status", width=100, anchor=CENTER)

        self.user_table.pack(fill=BOTH, expand=3)
        # self.user_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data01()


        #frame2 and table 2

        self.frame2 = Frame(self.root, width=700, height=200, bg="red")
        self.frame2.place(x=50, y=50)

        scroll_x = Scrollbar(self.frame2, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.frame2, orient=VERTICAL)
        self.user_table01 = ttk.Treeview(self.frame2, columns=(
            "id", "name", "pickup_location", "drop_address", "date", "time", "status",)
                                       , xscrollcommand=scroll_x.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.user_table01.xview)
        scroll_y.config(command=self.user_table01.yview)
        self.user_table01.heading("id", text="Id")
        self.user_table01.heading("name", text="Name")
        self.user_table01.heading("pickup_location", text="Pickup Location")
        self.user_table01.heading("drop_address", text="Drop address")
        self.user_table01.heading("date", text="Date")
        self.user_table01.heading("time", text="Time")
        self.user_table01.heading("status", text="Status")

        self.user_table01['show'] = 'headings'
        self.user_table01.column("id", width=100, anchor=CENTER)
        self.user_table01.column("name", width=100, anchor=CENTER)
        self.user_table01.column("pickup_location", width=100, anchor=CENTER)
        self.user_table01.column("drop_address", width=100, anchor=CENTER)
        self.user_table01.column("date", width=100, anchor=CENTER)
        self.user_table01.column("time", width=100, anchor=CENTER)
        self.user_table01.column("status", width=100, anchor=CENTER)

        self.user_table01.pack(fill=BOTH, expand=3)
        self.fetch_data()


        # Button
        # self.button = Button(self.root, text="view Booking", font=('Arial', 10, 'bold'))
        # self.button.place(x=100, y=10)

        self.button = Button(self.root, text="Back", font=('Arial', 10, 'bold'), command=self.cmd)
        self.button.place(x=730, y=0)
        self.button = Button(self.root, text="Trip Completed", font=('Arial', 10, 'bold'), command=self.complete_data)
        self.button.place(x=0, y=0)

        self.root.mainloop()

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="booking")
        cursor = conn.cursor()

        cursor.execute("select * from driver where license=%s", (self.username,))
        driver_id = cursor.fetchone()[0]

        cursor.execute("SELECT * FROM book  where driverid =%s and status ='Active'", (driver_id,))
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.user_table01.delete(*self.user_table01.get_children())
            for row in rows:
                self.user_table01.insert('', END, values=row)
                conn.commit()
        conn.close()

    def fetch_data01(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="booking")
        cursor = conn.cursor()

        cursor.execute("select * from driver where license=%s", (self.username,))
        driver_id = cursor.fetchone()[0]

        cursor.execute("SELECT * FROM book  where driverid =%s and status ='Completed'", (driver_id,))
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.user_table.delete(*self.user_table.get_children())
            for row in rows:
                self.user_table.insert('', END, values=row)
                conn.commit()
        conn.close()

    def complete_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="booking")
        cursor = conn.cursor()
        selected_item = self.user_table01.selection()[0]
        book_id = self.user_table01.item(selected_item)['values'][0]
        cursor.execute("select * from driver where license=%s", (self.username,))
        driver_id = cursor.fetchone()[0]
        cursor.execute("Update driver set driver_status = 'Available' where driverid = %s", (driver_id,))
        cursor.execute("Update book set driverid = %s, status='Completed' where book_id=%s", (driver_id,book_id,))
        rows = cursor.fetchall()
        conn.commit()
        # self.fetch_data()
        self.fetch_data01()
        messagebox.showinfo("Success", "Booking  Completed Sucessfully")
        conn.close()

    def cmd(self):
        self.root.destroy()
        os.system("Driver_Login.py")


