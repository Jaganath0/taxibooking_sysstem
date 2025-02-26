import os
from tkinter import *
from tkinter import messagebox
#import mysql.connector
import Registration
import Driver_signup


class Login_page():

        # Registration.Register()
    def __init__(self,root):
        self.root = root
        self.root.geometry("800x500")
        self.root.resizable(False, False)


        self.bg=PhotoImage(file="image.png")
        self.bg_image= Label(self.root,image=self.bg).place(x=0,y=0)



        # Heading
        self.label = Label(self.root, text='We Make Travel Fun', font=1000)
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

        self.button = Button(self.root, text="Sign in as driver", font=('Arial', 10,),command=self.cmd)
        self.button.place(x=480, y=250)

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





        self.label = Label(self.root, text="Don't have account? sign up as ", font=('Arial', 10,))
        self.label.place(x=345, y=290)
        self.button = Button(self.root, text="Customer", font=('Arial', 10,),command=self.nextPage)
        self.button.place(x=380, y=320)
        self.button = Button(self.root,text="Driver",font=('Arial',10,),command=self.next_page)
        self.button.place(x=380, y=380)

    def admin(self):
        import Admin
        self.root.withdraw()
        self.new = Toplevel()
        self.obj = Admin.Admin_Dashboard(self.new)

    # validation and database connection
    def validinfo(self):
        # self.destroy()
        username=self.userbox.get()
        passwd=self.passwordbox.get()
        if self.userbox.get() == "" or self.passwordbox.get() == "" :
            messagebox.showerror("error", "please enter user name and password ")

        elif username == 'admin' or passwd == 'admin':
                messagebox.showinfo("welcome","wlcome to the admin dashboard")
                self.admin()


        #else:
            #try:
                #conn = mysql.connector.connect(host="localhost",
                                              # user="root",
                                               #password="",
                                               #database="booking")
                #cursor = conn.cursor()
                #cursor.execute("SELECT * FROM register WHERE email = %s AND password = %s", (username, passwd))
                #data = cursor.fetchone()
                #if data== None:
                    #messagebox.showerror("error", "incorrect password or username",parent=self.root)
                #else:
                    #messagebox.showinfo("welcome", f"Welcome {username}", parent=self.root)

                    #self.home_page(username)



                    '''''
                    username = data[2]
                    messagebox.showinfo("sucess", "WELCOME "+username)
                    print(data)
                    Home.Booking()
                    '''
                #if data:
                     #Home.Booking()
                #conn.close()


                #self.root.destroy()

            #except Exception as es:

                #messagebox.showerror("error", f"error due  to: {str(es)}")
                #self.root.mainloop()
    def home_page(self,username):
        self.root.destroy()
        import Home
        self.new = Tk()
        reg = Home.Home_Page(self.new,username)

    def nextPage(self):
        self.root.destroy()
        os.system("Registration.py")

    def next_page(self):
        self.root.destroy()
        os.system("Driver_signup.py")
    def cmd(self):
        self.root.destroy()
        os.system("Driver_Login.py")

#if __name__ == '__main__':
     #root = Tk()
     #obj = Login_page(root)
     #root.mainloop()