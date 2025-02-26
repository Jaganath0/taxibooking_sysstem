from tkinter import *
from tkinter import messagebox
import os

class Admin_Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x500")
        self.root.resizable(False, False)

        self.bg = PhotoImage(file="image.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0)
        self.label = Label(self.root, text='Welcome to Admin Dashboard', font=1000)
        self.label.place(x=250, y=1)

        self.button = Button(self.root, text="Manage Booking", font=('Arial', 10, 'bold'),command=self.cmd1)
        self.button.place(x=270, y=90)
        self.button = Button(self.root, text="Payment", font=('Arial', 10, 'bold'),command=self.cmd2)
        self.button.place(x=270, y=130)

        self.button = Button(self.root, text="logout", font=('Arial', 10, 'bold'),command=self.cmd)
        self.button.place(x=290, y=425)

    def cmd(self):
        self.root.destroy()
        os.system("Login.py")
    def cmd1(self):
        self.root.destroy()
        os.system("Manage.py")
    def cmd2(self):
        self.root.destroy()
        os.system("payment.py")


if __name__ == '__main__':
     root = Tk()
     obj = Admin_Dashboard(root)
     root.mainloop()