import os
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector


class Payment:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x700")
        self.root.resizable(False, False)

        self.bg = PhotoImage(file="image.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0)

        self.var_booking = StringVar()
        self.var_price = IntVar()
        self.var_VAT = IntVar()
        self.var_total = IntVar()
        self.var_bill = IntVar()


        self.frame = Frame(self.root, width=300, height=100, bg="white")
        self.frame.place(x=20, y=20, height=300, width=820)

        self.name = Label(self.frame, text="Booking Id ", font=("times new roma", 15, "bold"))
        self.name.place(x=20, y=20)

        self.name_e = Entry(self.frame, textvariable=self.var_booking, font=("times new roma", 15, "bold"))
        self.name_e.place(x=180, y=20)

        self.price = Label(self.frame, text="price", font=("times new roma", 15, "bold"))
        self.price.place(x=20, y=80)

        self.price_e = Entry(self.frame, textvariable=self.var_price,font=("times new roma", 15, "bold"))
        self.price_e.place(x=180, y=80)

        total_button = Button(self.frame, text='Total', command=self.total, width=10, height=1, bg='blue',font=("times new roma", 15, "bold"))
        total_button.place(x=180, y=240)

        receipt_button = Button(self.frame, text='Receipt', command=self.receipt, width=10, height=1, bg='blue',font=("times new roma", 15, "bold"))
        receipt_button.place(x=20, y=240)
        # self.button = Button(self.root, text="Back", font=('Arial', 10, 'bold'),command=self.cmd)
        # self.button.place(x=400, y=250)

        self.frame2 = Frame(self.frame, width=350, height=100, bg="white")
        self.frame2.place(x=500, y=10, height=280, width=300)

        scroll_y = Scrollbar(self.frame2, orient=VERTICAL)
        self.txt = Text(self.frame2, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txt.yview)
        self.txt.pack(fill=BOTH, expand=1)



##frame 1

##frame 2

        self.frame1 = Frame(self.root, width=300, height=100, bg="green")
        self.frame1.place(x=20, y=340,height=300,width=820)
        scroll_x = Scrollbar(self.frame1, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.frame1, orient=VERTICAL)
        self.user_table01 = ttk.Treeview(self.frame1, columns=(
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
        self.user_table01.bind("<ButtonRelease-1>", self.get)
        self.fetch_data()
        self.root.mainloop()
    def get(self, ab):
        s = self.user_table01.focus()
        content = (self.user_table01.item(s))
        row = content['values']

        self.var_booking.set(row[0])


    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="booking")
        cursor = conn.cursor()

        try:

            cursor.execute("SELECT * FROM book  where  status ='Completed'")
            rows = cursor.fetchall()
            if len(rows) != 0:
                self.user_table01.delete(*self.user_table01.get_children())
                for row in rows:
                    self.user_table01.insert('', END, values=row)
                    conn.commit()
            conn.close()

        except Exception as es:

            messagebox.showerror("error", f"error due  to: {str(es)}")

    def total(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="booking")
        cursor = conn.cursor()
        cursor.execute(
            "select customer_id from book where book_id = %s",
            (self.var_booking.get(),))
        row = cursor.fetchone()
        cus_id = row[0]
        print(cus_id)
        # customerId = customerId1[0]

        Total_bill = float((self.var_price.get()))
        # print(Total)
        VAT = float((Total_bill) * 0.13, )
        total = float(Total_bill + VAT)
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="booking")
            cursor = conn.cursor()
            if  self.var_booking.get() == "" or self.var_price.get() == "":
                messagebox.showerror(
                    "Error", "All the field must be required", parent=self.root)
            # else:
            #     cursor.execute("Select Bill_No from bill where Bill_No = %s", (self.var_bill_no.get(),))
            #     row = cursor.fetchone()
            #     if row != None:
            #         messagebox.showerror(
            #             "Error", "Bill already exits, Try different", parent=self.root)
            else:

                selected_item = self.user_table01.selection()[0]
                Booking_ID = self.user_table01.item(selected_item)['values'][0]

                cursor.execute(
                    "Insert into billing (price,VAT,total,customer_id) values(%s,%s,%s,%s)",
                    (
                        self.var_price.get(),
                        VAT,
                        total,
                        cus_id,
                    ))
                # cursor.executemany(statement,values)
                cursor.execute("Update book set  Status='Completed' where Book_id=%s",
                               (Booking_ID,))
                conn.commit()
                messagebox.showinfo("Sucessful", "Successfully Bill Generated", parent=self.root)
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root)
    # def cmd(self):
    #     self.root.destory()
    #     os.system("Admin.py")

    def receipt(self):

        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="booking")
            cursor = conn.cursor()
            cursor.execute(
                "select customer_id from book where book_id = %s",
                (self.var_booking.get(),))
            row = cursor.fetchone()
            cus_id = row[0]
            print(cus_id)
            # customerId = customerId1[0]

            Total_bill = float((self.var_price.get()))
            # print(Total)
            VAT = float((Total_bill) * 0.13, )
            total = float(Total_bill + VAT)

            self.txt.delete('1.0', END)
            self.txt.insert(END, "                 Welcome to our\n online taxi booking system\n")

            self.txt.insert(END, "                        Receipt\n")
            self.txt.insert(END, f"\n            Booking ID : {str(self.var_booking.get())}")
            self.txt.insert(END, "\n         =========================================")
            self.txt.insert(END, "\n            Price Price ")
            self.txt.insert(END, "\n         =========================================")
            self.txt.insert(END,
                             f"\n            Rate       {self.var_price.get()}Rs  ")
            self.txt.insert(END, "\n         =========================================")
            self.txt.insert(END, f"\n                       Total:  {Total_bill}")
            self.txt.insert(END, f"\n                       VAT(13%):  {VAT}")
            self.txt.insert(END, "\n         =========================================")
            self.txt.insert(END, f"\n                       Total including VAT:  {total}")
            self.txt.insert(END, "\n\n\n\n           *Thank You so much!!*              ")

        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root)

    # def cmd(self):
    #     self.root.widthdraw()
    #     os.system("Admin.py")
    #



if __name__ == '__main__':
     root = Tk()
     obj = Payment(root)
     root.mainloop()