from tkinter import *
from tkinter import ttk
import tkinter
import track

all = []

if __name__ == '__main__':
    root = Tk()
    root.title("Tracker")


    def open_popup():
        top = Toplevel(root)
        top.geometry("750x250")
        top.title("Create")
        Label(top, text="Hello World!", font=('Mistral 18 bold')).place(x=150, y=80)

    frm = ttk.Frame(root, padding=10)
    frm.grid()
    tkinter.Button(frm, text="Create", command=open_popup).grid(column=0, row=0)

    root.mainloop()