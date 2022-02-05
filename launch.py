from tkinter import *
from tkinter import ttk
import config

def clear():
    config.possible_schemes.clear()
    config.possible_enemies.clear()
    config.possible_items.clear()
    config.main_villain.clear()
    config.main_scheme.clear()

if __name__ == '__main__':
    root = Tk()
    frm = ttk.Frame(root, padding=100)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

    root.mainloop()