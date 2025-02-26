import os
from tkinter import *
from tkinter import messagebox


class Home_Page:

    def __init__(self,root,username):
        self.root = root
        self.username = username
        self.root.geometry("800x500")
        self.root.resizable(False, False)

        self.bg = PhotoImage(file="image.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0)





        # Button
        self.button = Button(self.root, text="view Booking", font=('Arial', 10, 'bold'),command=self.cmd2)
        self.button.place(x=100, y=10)
        self.button = Button(self.root, text="Booking", font=('Arial', 10, 'bold'),command=self.cmd1)
        self.button.place(x=290, y=10)
        self.button = Button(self.root, text="Back", font=('Arial', 10, 'bold'), command=self.cmd)
        self.button.place(x=290, y=425)



        self.root.mainloop()

    def cmd(self):
        self.root.destroy()
        os.system("Login.py")

    def cmd1(self):
        self.root.destroy()
        import Booking
        self.new = Tk()
        obj = Booking.Jaganath(self.new, username=self.username)

    def cmd2(self):
        self.root.destroy()
        import demo
        self.new = Tk()
        obj = demo.Booking(self.new, username=self.username)

# obj = Home_Page()

