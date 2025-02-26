from tkinter import *
import mysql.connector
from tkinter import messagebox
import os

class Register:
    def __init__(self):
        self.root =Tk()
        self.root.geometry("800x500")
        self.root.resizable(False, False)


        self.bg = PhotoImage(file="image.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0)



        self.label = Label(self.root, text='Welcome to online taxi service', font=('Arial', 20, 'bold'))
        self.label.place(x=250, y=0)

        self.label = Label(self.root, text='Full Name', font=('Arial', 10, 'bold'))
        self.label.place(x=250, y=90)
        self.namebox = Entry(self.root, text='')
        self.namebox.place(x=360, y=90, width=200)

        self.label = Label(self.root, text='Address', font=('Arial', 10, 'bold'))
        self.label.place(x=250, y=130)
        self.addressbox = Entry(self.root, text='')
        self.addressbox.place(x=360, y=130, width=200)

        self.label = Label(self.root, text='Email address', font=('Arial', 10, 'bold'))
        self.label.place(x=250, y=170)
        self.emailbox = Entry(self.root, text='')
        self.emailbox.place(x=360, y=170, width=200)

        self.label = Label(self.root, text='Mobile number', font=('Arial', 10, 'bold'))
        self.label.place(x=250, y=205)
        self.mobilebox = Entry(self.root, text='')
        self.mobilebox.place(x=360, y=205, width=200)

        self.label = Label(self.root, text='Password', font=('Arial', 10, 'bold'))
        self.label.place(x=250, y=235)
        self.passwordbox = Entry(self.root, text='')
        self.passwordbox.place(x=360, y=235, width=200)

        self.button = Button(self.root, text="Sign Up", command=self.Connect_info)
        self.button.place(x=360, y=425)
        self.button = Button(self.root, text="Back", command=self.cmd)
        self.button.place(x=450, y=425)

        self.root.mainloop()

    def Connect_info(self):
        if self.namebox.get() == "" or self.addressbox.get() == "" or self.emailbox.get() == "" or self.mobilebox.get() == "" or self.passwordbox.get() == "":
            messagebox.showerror("error", "please fill all the information ")
        else:

            try:
                conn = mysql.connector.connect(host="localhost",
                                               user="root",
                                               password="",
                                               database="booking")
                cursor = conn.cursor()
                cursor.execute("insert into register(name,address,email,contact,password) values(%s,%s,%s,%s,%s)", (
                    self.namebox.get(),
                    self.addressbox.get(),
                    self.emailbox.get(),
                    self.mobilebox.get(),
                    self.passwordbox.get()
                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("sucess", "register sucessfully")
                import Login

            except Exception as es :
                messagebox.showerror("error", f" Error : str{(es)}")
    def cmd(self):
        self.root.destroy()
        os.system("Login.py")

# def page():
#     root = Tk()
#     Register(root)
#
#
#
# if __name__ == '__main__':
#      page()
Register()