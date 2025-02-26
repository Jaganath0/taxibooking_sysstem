from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkcalendar import Calendar, DateEntry
import os



class Jaganath:

        # Registration.Register()
    def __init__(self,root,username):
        self.root = root
        self.username=username
        self.root.geometry("800x500")
        self.root.resizable(False, False)
        #self.bg = PhotoImage(file="image.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0)

        self.name = Label(self.root, text='Name of Customer', font=('Arial', 10, 'bold'))
        self.name.place(x=266, y=100)
        self.tf_name = Entry(self.root, text="")
        self.tf_name.place(x=400, y=100, width=135)
        self.pickup = Label(self.root, text='Pick up location', font=('Arial', 10, 'bold'))
        self.pickup.place(x=266, y=152)
        self.tf_pick = Entry(self.root, text="")
        self.tf_pick.place(x=400, y=152, width=135)
        self.drop = Label(self.root, text='Drop location', font=('Arial', 10, 'bold'))
        self.drop.place(x=266, y=189)
        self.tf_drop = Entry(self.root, text="")
        self.tf_drop.place(x=400, y=189, width=135)
        self.date = Label(self.root, text='Pick up date', font=('Arial', 10, 'bold'))
        self.date.place(x=266, y=224)
        self.tf_date = DateEntry(self.root, width=16, background="magenta3", foreground="white", bd=2)

        self.tf_date.place(x=400, y=224, width=135)
        self.time = Label(self.root, text='Pick up time', font=('Arial', 10, 'bold'))
        self.time.place(x=266, y=250)
        self.tf_time = Entry(self.root, text="")
        self.tf_time.place(x=400, y=255, width=135)
        self.button = Button(self.root, text="Request for booking",command=self.valid__info)
        self.button.place(x=325, y=300)
        self.button = Button(self.root, text="Back", font=('Arial', 10, 'bold'), command=self.cmd)
        self.button.place(x=340, y=380)
        self.root.mainloop()

    def valid__info(self):
        name = self.tf_name.get()
        pickuplocation = self.tf_pick.get()
        droplocation = self.tf_drop.get()
        date = self.tf_date.get()
        time = self.tf_time.get()


        if time == "" or name =="" or pickuplocation=="" or droplocation=="" or date=="":
            messagebox.showerror("Error", "Fields should not be Empty!", parent=self.root)

       # else:

           '''' try:
                conn = mysql.connector.connect(host="localhost", user="root", password="",
                                               database="booking")
                cursor = conn.cursor()
                cursor.execute("select * from register where email=%s", (self.username,))
                cust_id = cursor.fetchone()[0]

                statement = (
                    "INSERT INTO book (name, pickbox, dropbox, datebox, timebox, status, customer_id) values (%s,%s,%s,%s,%s,'Pending',%s)")

                values = (name,
                          pickuplocation,
                          droplocation,
                          date,
                          time,
                          cust_id
                          )
                cursor.execute(statement, values)

                conn.commit()

                messagebox.showinfo("Success", " Booked Successfully !", parent=self.root)

                # self.view_booking(username=self.username)


            except Exception as es:

                messagebox.showerror("Error", f"Error due to: {str(es)}")'''


    def cmd(self):
            self.root.destroy()
            import Home
            self.new = Tk()
            reg = Home.Home_Page(self.new, username=self.username)


#Jaganath()

# if __name__ == '__main__':
#     page()