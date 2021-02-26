import tkinter as tk
from tkinter import scrolledtext, Spinbox


gui = tk.Tk()

scr = scrolledtext.ScrolledText(gui, width=30, height=5, wrap=tk.WORD)
scr.grid(column=0, row=1, columnspan=2)


def _spin():
    value = spin.get()
    scr.insert(tk.INSERT, '%s Guest\n' % value)


spin = Spinbox(gui, from_=0, to=100, width=5, bd=8, command=_spin, relief=tk.FLAT)
spin.grid(column=0, row=0, padx=10, pady=10)

label = tk.Label(gui, text='Guest')
label.grid(column=1, row=0, padx=10, pady=10)
# tk.RAISED, SUNKEN, GROOVE, RIDGE


def scr_hover(event):
    scr['bg'] = 'gray94'


def scr_leave(event):
    scr['bg'] = 'white'


def spin_hover(event):
    spin['bg'] = 'gray94'


def spin_leave(event):
    spin['bg'] = 'white'


scr.bind('<Enter>', scr_hover)
scr.bind('<Leave>', scr_leave)

spin.bind('<Enter>', spin_hover)
spin.bind('<Leave>', spin_leave)

# String Formatting
# name = 'John'
# print('Hello, %s!' % name)
# %d integers
# %s string
# %f decimals
# %.<number of digits>f


gui.mainloop()
