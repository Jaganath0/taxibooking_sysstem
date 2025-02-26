from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import os

class Booking:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x500")
        self.root.resizable(False, False)

        self.bg = PhotoImage(file="image.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0)

        self.Bookingid = StringVar()
        self.name = StringVar()
        self.pickuplocation = StringVar()
        self.droplocation = StringVar()
        self.pickupdate = StringVar()
        self.pickuptime = StringVar()


        self.label = Label(self.root, text='Booking ID', font=('Arial', 10, 'bold'))
        self.label.place(x=250, y=70)
        self.bookid = Entry(self.root, textvariable=self.Bookingid)
        self.bookid.place(x=390, y=70, width=200)
        self.label = Label(self.root, text='Name of customer', font=('Arial', 10, 'bold'))
        self.label.place(x=250, y=90)
        self.cust_name = Entry(self.root, textvariable=self.name)
        self.cust_name.place(x=390, y=90, width=200)

        self.label = Label(self.root, text='pick up Address', font=('Arial', 10, 'bold'))
        self.label.place(x=250, y=130)
        self.address = Entry(self.root, textvariable=self.pickuplocation)
        self.address.place(x=390, y=130, width=200)

        self.label = Label(self.root, text='droop location', font=('Arial', 10, 'bold'))
        self.label.place(x=250, y=170)
        self.drop = Entry(self.root, textvariable=self.droplocation)
        self.drop.place(x=390, y=170, width=200)

        self.label = Label(self.root, text='Driver name', font=('Arial', 10, 'bold'))
        self.label.place(x=250, y=200)
        self.driver_name = Entry(self.root, text="")
        self.driver_name.place(x=390, y=200, width=200)

        self.label = Label(self.root, text='Pick up Time', font=('Arial', 10, 'bold'))
        self.label.place(x=250, y=260)
        self.time = Entry(self.root, textvariable=self.pickuptime)
        self.time.place(x=390, y=260, width=200)

        self.label = Label(self.root, text='Pick up Date', font=('Arial', 10, 'bold'))
        self.label.place(x=250, y=230)
        self.date = Entry(self.root, textvariable=self.pickupdate)
        self.date.place(x=390, y=230, width=200)

        self.button = Button(self.root, text="Assign",command=self.assign_data, font=('Arial', 10, 'bold'))
        self.button.place(x=1, y=255)



        self.button = Button(self.root, text="Back", font=('Arial', 10, 'bold'),command=self.cmd)
        self.button.place(x=925, y=1)

        self.button = Button(self.root, text="Avilable Driver", font=('Arial', 10, 'bold'),command=self.cmd1)
        self.button.place(x=850, y=50)





        self.frm = Frame(self.root, width=700, height=500)
        self.frm.place(x=1, y=300)

        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="booking")
        cursor = mydb.cursor()

        sql = "SELECT * FROM book"
        cursor.execute(sql)
        rows = cursor.fetchall()
        total = cursor.rowcount
        print("Total Data Entries: " + str(total))
        # messagebox.showinfo('info', 'Inserted')

        scroll_x = Scrollbar(self.frm, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.frm, orient=VERTICAL)
        self.user_table = ttk.Treeview(self.frm, columns=(
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
        self.user_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="booking")
        cursor = conn.cursor()

        sql = "SELECT * FROM book"
        cursor.execute(sql)
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.user_table.delete(*self.user_table.get_children())
            for row in rows:
                self.user_table.insert('', END, values=row)
                conn.commit()
        conn.close()

    def assign_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="booking")
        cursor = conn.cursor()
        selected_item = self.user_table.selection()[0]
        book_id = self.user_table.item(selected_item)['values'][0]
        cursor.execute("select driverid from driver where name = %s",(self.driver_name.get(),))
        driver_id = cursor.fetchone()[0]
        cursor.execute("Update driver set driver_status = 'not Available' where driverid = %s",(driver_id,))
        cursor.execute("Update book set driverid = %s, status='Active' where book_id=%s", (driver_id,book_id,))
        conn.commit()
        self.fetch_data()
        messagebox.showinfo("Success", "Booking  Assigned Sucessfully")

    def get_cursor(self, ev):
        f = self.user_table.focus()
        content = (self.user_table.item(f))
        row = content['values']

        self.Bookingid.set(row[0]),
        self.name.set(row[1]),
        self.pickuplocation.set(row[2]),
        self.droplocation.set(row[3]),
        self.pickupdate.set(row[4]),
        self.pickuptime.set(row[5]),


    def cmd(self):
        self.root.destroy()
        os.system("Admin.py")
    def cmd1(self):
        # self.root.destroy()
        import Avilabe
        self.new = Tk()
        reg = Avilabe. avilable(self.new)

def page():
    root = Tk()
    Booking(root)
    root.mainloop()


if __name__ == '__main__':
     page()