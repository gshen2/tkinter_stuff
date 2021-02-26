import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()

scr = scrolledtext.ScrolledText(win, width=30, height=10, wrap=tk.WORD)
scr.grid(column=1, row=0, columnspan=3, rowspan=3, padx=10, pady=10)

scr.focus()

# checkButton

chVar1 = tk.IntVar()
check1 = tk.Checkbutton(win, text='Disabled', variable=chVar1, state='disabled')
check1.select()
check1.grid(column=4, row=0, padx=10, pady=5, ipadx=10, ipady=5, sticky='W')

chVar2 = tk.IntVar()
check2 = tk.Checkbutton(win, text='Enabled', variable=chVar2)
check2.select()
check2.grid(column=4, row=1, padx=10, pady=5, ipadx=10, ipady=5, sticky='W')

chVar3 = tk.IntVar()
check3 = tk.Checkbutton(win, text='Disable All', variable=chVar3)
check3.grid(column=4, row=2, padx=10, pady=5, ipadx=10, ipady=5, sticky='W')

# radioButton

def radCall():
    radSel = radVar.get()
    if radSel == 1:
        win.configure(background='grey')
    elif radSel == 2:
        win.configure(background='blue')
    elif radSel == 3:
        win.configure(background='gold')

# create three Radiobuttons using one variable
radVar = tk.IntVar()

rad1 = tk.Radiobutton(win, text='grey', variable=radVar, value=1, command=radCall())
rad1.grid(column=0, row=0, padx=10, pady=5, ipadx=10, ipady=5)

rad2 = tk.Radiobutton(win, text='blue', variable=radVar, value=2, command=radCall())
rad2.grid(column=0, row=1, padx=10, pady=5, ipadx=10, ipady=5)

rad3 = tk.Radiobutton(win, text='gold', variable=radVar, value=3, command=radCall())
rad3.grid(column=0, row=2, padx=10, pady=5, ipadx=10, ipady=5)

win.mainloop()