from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import os

from tkcalendar import DateEntry


class Booking:
    def __init__(self, root,username):
        self.root = root
        self.username = username
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
        self.box = Entry(self.root, textvariable= self.Bookingid)
        self.box.place(x=390, y=70, width=200)

        self.label = Label(self.root, text='Name of customer', font=('Arial', 10, 'bold'))
        self.label.place(x=250, y=90)
        self.box = Entry(self.root, textvariable=self.name)
        self.box.place(x=390, y=90, width=200)

        self.label = Label(self.root, text='pick up Address', font=('Arial', 10, 'bold'))
        self.label.place(x=250, y=130)
        self.box01 = Entry(self.root, textvariable=self.pickuplocation)
        self.box01.place(x=390, y=130, width=200)

        self.label = Label(self.root, text='droop location', font=('Arial', 10, 'bold'))
        self.label.place(x=250, y=170)
        self.box02 = Entry(self.root, textvariable=self.droplocation)
        self.box02.place(x=390, y=170, width=200)

        self.label = Label(self.root, text='Pick Up date', font=('Arial', 10, 'bold'))
        self.label.place(x=250, y=200)
        self.box03 = Entry(self.root, textvariable=self.pickupdate)
        self.box03.place(x=390, y=200, width=200)
        # self.pickupdate = DateEntry(self.root, width=16, background="magenta3", foreground="white", bd=2)

        self.label = Label(self.root, text='Pick Up time', font=('Arial', 10, 'bold'))
        self.label.place(x=250, y=230)
        self.box04 = Entry(self.root, textvariable=self.pickuptime)
        self.box04.place(x=390, y=230, width=200)

        self.button = Button(self.root, command=self.edit_data,text="Edit", font=('Arial', 10, 'bold'))
        self.button.place(x=1, y=255)


        self.button = Button(self.root,command=self.cancel_data, text="Cancle", font=('Arial', 10, 'bold'))
        self.button.place(x=150, y=255)

        self.button = Button(self.root, text="Back", font=('Arial', 10, 'bold'),command=self.cmd)
        self.button.place(x=925, y=1)

        self.tbl_frm = Frame(self.root, width=800, height=500)
        self.tbl_frm.place(x=100, y=300,width=900)

        scroll_x = Scrollbar(self.tbl_frm, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.tbl_frm, orient=VERTICAL)
        self.user_table = ttk.Treeview(self.tbl_frm, columns=("id","name", "pickup_location", "drop_address", "date", "time", "status",)
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
        self.user_table.column("id", width=100,anchor=CENTER)
        self.user_table.column("name", width=100,anchor=CENTER)
        self.user_table.column("pickup_location", width=100,anchor=CENTER)
        self.user_table.column("drop_address", width=100,anchor=CENTER)
        self.user_table.column("date", width=100,anchor=CENTER)
        self.user_table.column("time", width=100,anchor=CENTER)
        self.user_table.column("status", width=100,anchor=CENTER)


        self.user_table.pack(fill=BOTH, expand=3)
        self.user_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()



    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="booking")
        cursor = conn.cursor()

        cursor.execute("select * from register where email=%s", (self.username,))
        cust_id = cursor.fetchone()[0]

        cursor.execute("SELECT * FROM book  where customer_id=%s",(cust_id,))
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
        cursor.execute("Update book set status='Cancelled' where book_id=%s",(book_id,))
        conn.commit()
        self.fetch_data()
        messagebox.showinfo("Success","Booking Cancelled Sucessfully")

    def edit_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="booking")
        cursor = conn.cursor()
        selected_item = self.user_table.selection()[0]
        book_id = self.user_table.item(selected_item)['values'][0]
        cursor.execute("Update book set pickbox=%s , dropbox= %s, datebox=%s, timebox=%s where book_id=%s", (self.box01.get(),self.box02.get(), self.box03.get(),self.box04.get(),book_id,))
        conn.commit()
        self.fetch_data()
        messagebox.showinfo("Success", "Booking Edited Sucessfully")


    def get_cursor(self,ev):
        f= self.user_table.focus()
        content =(self.user_table.item(f))
        row = content['values']

        self.Bookingid.set(row[0]),
        self.name.set(row[1]),
        self.pickuplocation.set(row[2]),
        self.droplocation.set(row[3]),
        self.pickupdate.set(row[4]),
        self.pickuptime.set(row[5]),




    def cmd(self):
        self.root.destroy()
        import Home
        self.new = Tk()
        reg = Home.Home_Page(self.new, username=self.username)

# def page():
#     root = Tk()
#     Booking(root)
#     root.mainloop()


# if __name__ == '__main__':
#      page()
