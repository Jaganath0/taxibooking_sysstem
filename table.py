#!/usr/bin/env python

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Username and Password Handler")

lsideframe = Frame(root)
lsideframe.pack(side=LEFT)

rsideframe = Frame(root)
rsideframe.pack(side=RIGHT)

u_label = Label(lsideframe, text="Username")
u_label.grid(row=0, column=0)
u_entry = Entry(lsideframe)
u_entry.grid(row=0, column=1)

p_label = Label(lsideframe, text="Password")
p_label.grid(row=1, column=0)
p_entry = Entry(lsideframe)
p_entry.grid(row=1, column=1)





def display(user, passwd):
    top = Toplevel()
    tview = ttk.Treeview( top, columns=('Username', 'Password'))
    tview.heading('#0', text='SN')
    tview.column('#0', stretch=NO)
    tview.heading('#1', text='Username')
    tview.column('#1', stretch=NO)
    tview.heading('#2', text='Password')
    tview.column('#2', stretch=NO)
    tview.bind("<<TreeviewSelect>>", showcred)
    tview.grid(row=0, columnspan=2, sticky='nsew')
    treeview = tview

    # tview = ttk.Treeview( top, columns=('Username', 'Password'),
	# 					 show="headings")
    # tview.heading('Username', text="Username")
    # tview.heading('Password', text="Password")
    # tview.bind("<<TreeviewSelect>>", showcred)
    # tview.grid(row=0, columnspan=2, sticky='nsew')


    tview.insert('', 1, text='1', values=(user, passwd))
    tview.insert('', 'end', text='2', values=("bishwo", "passwd"))
    tview.insert('', 'end', text='3', values=("other", "other"))

def showcred(event):
    data = event.widget.item(event.widget.selection())
    print(f"Username: {data['values'][0]} Password: {data['values'][1]}")


button = Button(rsideframe, text="Generate Treeview", command=lambda:display(u_entry.get(), p_entry.get()))
button.grid(row=0, column=0)












root.mainloop()





#     def insert_data(self):
#         """
#         Insertion method.
#         """
#         self.treeview.insert('', 'end', text="Item_"+str(self.i), values=(self.dose_entry.get()+" mg", self.modified_entry.get()))
#         # Increment counter
#         self.i = self.i + 1

# def main():
#     root=Tkinter.Tk()
#     d=Begueradj(root)
#     root.mainloop()

# if __name__=="__main__":
#     main()