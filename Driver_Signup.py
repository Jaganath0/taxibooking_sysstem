from tkinter import *
from tkinter import messagebox
import mysql.connector
import os

class Driver:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x500")
        self.root.resizable(False, False)

        self.bg = PhotoImage(file="image.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0)

        self.label = Label(self.root, text='Leave sooner, Drive slower, Live longer', font=('Arial', 20, 'bold'))
        self.label.place(x=200, y=0)
        self.label = Label(self.root, text='Full Name', font=('Arial', 10, 'bold'))
        self.label.place(x=200, y=90)
        self.namebox = Entry(self.root, text="")
        self.namebox.place(x=360, y=90, width=200)

        self.label = Label(self.root, text='Citizensip Number', font=('Arial', 10, 'bold'))
        self.label.place(x=200, y=130)
        self.citizenbox = Entry(self.root, text="")
        self.citizenbox.place(x=360, y=130, width=200)

        self.label = Label(self.root, text='License Number', font=('Arial', 10, 'bold'))
        self.label.place(x=200, y=170)
        self.licensebox = Entry(self.root, text="")
        self.licensebox.place(x=360, y=170, width=200)

        self.label = Label(self.root, text='Password', font=('Arial', 10, 'bold'))
        self.label.place(x=200, y=190)
        self.passwordbox = Entry(self.root, text="")
        self.passwordbox.place(x=360, y=190, width=200)

        self.label = Label(self.root, text='Contact Number', font=('Arial', 10, 'bold'))
        self.label.place(x=200, y=220)


        self.contactbox = Entry(self.root, text="")
        self.contactbox.place(x=360, y=220, width=200)
        self.button = Button(self.root, text="Rigister", font=('Arial', 10, 'bold'),command=self.Connect_info)
        self.button.place(x=290, y=425)

        self.button = Button(self.root, text="Back", font=('Arial', 10,), command=self.cmd)
        self.button.place(x=380, y=425)

    def Connect_info(self):
        if self.namebox.get() == "" or self.citizenbox.get() == "" or self.licensebox.get() == "" or self.passwordbox.get()=="" or self.contactbox.get()=="":
                messagebox.showerror("error", "please fill all the information ")
        else:

            try:
                conn = mysql.connector.connect(host="localhost",
                                                   user="root",
                                                   password="",
                                                   database="booking")
                cursor = conn.cursor()
                cursor.execute("insert into driver(name,citizen,license,password,contact,driver_status) values(%s,%s,%s,%s,%s,'Available')", (
                    self.namebox.get(),
                    self.citizenbox.get(),
                    self.licensebox.get(),
                    self.passwordbox.get(),
                    self.contactbox.get()

                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("sucess", "register sucessfully")
                import Driver_Login
            except:
                messagebox.showerror("error", "database connection problem")

    def cmd(self):
        self.root.destroy()
        os.system("Login.py")





def page():
    root = Tk()
    Driver(root)
    root.mainloop()


if __name__ == '__main__':
    page()