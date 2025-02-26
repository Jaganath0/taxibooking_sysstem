import os
from tkinter import *
from tkinter import messagebox
import mysql.connector
# import Registration
# import Driver_signup


class Login_page():

        # Registration.Register()
    def __init__(self,root):
        self.root = root
        self.root.geometry("800x500")
        self.root.resizable(False, False)


        self.bg=PhotoImage(file="image.png")
        self.bg_image= Label(self.root,image=self.bg).place(x=0,y=0)



        # Heading
        self.label = Label(self.root, text='Driver Login', font=1000)
        self.label.place(x=350, y=1)

        #  username box and label
        self.label = Label(self.root, text='Username', font=('Arial', 10,))
        self.label.place(x=320, y=180)
        self.userbox = Entry(self.root, text="")
        self.userbox.place(x=390, y=180)

        # password box and label
        self.label = Label(self.root, text='Password', font=('Arial', 10))
        self.label.place(x=320, y=210)
        self.passwordbox = Entry(self.root, text="", show="*")
        self.passwordbox.place(x=390, y=210)

        # password show  button
        def showpwd(event):
            box = self.passwordbox.get()
            self.passwordbox.config(show="", text=box)
        def hidepwd(event):
            self.passwordbox.config(show="*")
        self.btn1 = Button(self.root, text="show password", font=('Arial', 10,), compound="center")
        self.btn1.place(x=600, y=210)
        self.btn1.bind('<Button-1>', showpwd)
        self.btn1.bind('<ButtonRelease-1>', hidepwd)

        #  For Button
        self.button = Button(self.root, text="Sign in", font=('Arial', 10,), command=self.validinfo)
        self.button.place(x=380, y=250)
        self.button = Button(self.root, text="Back", font=('Arial', 10,),command=self.cmd)
        self.button.place(x=380, y=300)









    # validation and database connection
    def validinfo(self):
        # self.destroy()
        username=self.userbox.get()
        passwd=self.passwordbox.get()
        if self.userbox.get() == "" or self.passwordbox.get() == "" :
            messagebox.showerror("error", "please enter user name and password ")




        else:
            try:
                conn = mysql.connector.connect(host="localhost",
                                               user="root",
                                               password="",
                                               database="booking")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM driver WHERE license = %s AND password = %s", (username, passwd))
                data = cursor.fetchone()
                if data== None:
                    messagebox.showerror("error", "incorrect password or username",parent=self.root)
                else:
                    messagebox.showinfo("welcome", f"Welcome {username}", parent=self.root)
                    self.driver_page(username)


                    '''''
                    username = data[2]
                    messagebox.showinfo("sucess", "WELCOME "+username)
                    print(data)
                    Home.Booking()
                    '''
                # if data:
                #     Home.Booking()
                conn.close()


                # self.root.destroy()

            except Exception as es:

                messagebox.showerror("error", f"error due  to: {str(es)}")
                # self.root.mainloop()
    def cmd(self):
        self.root.destroy()
        os.system("Login.py")

    def driver_page(self,username):
        self.root.destroy()
        import Driver_dashboard
        self.new = Tk()
        reg = Driver_dashboard.driver(self.new,username)




if __name__ == '__main__':
     root = Tk()
     obj = Login_page(root)
     root.mainloop()