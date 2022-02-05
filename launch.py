from tkinter import *
from tkinter import ttk
import villain

def klaw_setup(mode,num_pl):
    if mode:
        villain.villain("Klaw",12*num_pl,0,2,18*num_pl,1,2)
    else:
        villain.villain("Klaw", 18 * num_pl, 1, 2, 22 * num_pl, 2,3)

if __name__ == '__main__':
    root = Tk()
    frm = ttk.Frame(root, padding=100)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

    root.mainloop()