from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector


class Payment:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        self.frame = Frame(self.root, width=460, height=460, bg="red")
        self.frame.place(x=20, y=20)




if __name__ == '__main__':
    root = Tk()
    obj = Payment(root)
    root.mainloop()