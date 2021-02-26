import tkinter as tk
from tkinter import ttk
import datetime

win = tk.Tk()
win.iconbitmap('unit_conversion.ico')
win.title('Unit Conversion')
win.resizable(False, False)

ttk.Style().configure('TButton', foreground='blue')
# tabs
# Length: mm, m, km, in, ft, yd, mi
# Temperature: C, F, K

tabCtrl = ttk.Notebook(win)

tab1 = ttk.Frame(tabCtrl)
tabCtrl.add(tab1, text='Temperature')
tab2 = ttk.Frame(tabCtrl)
tabCtrl.add(tab2, text='Length')

tabCtrl.pack(expand=1, fill='both')

# 'Input'

t_in = ttk.Label(tab1, text='INPUT=')
t_in.grid(column=0, row=0, sticky='E')

# Enter input value

temp = tk.StringVar()
t_box = ttk.Entry(tab1, width=10, textvariable=temp, justify='center')
t_box.grid(column=1, row=0)
t_box.focus()  # Place cursor into Input Entry

# Select input unit

t_unit = tk.StringVar()
t_unit_chosen = ttk.Combobox(
    tab1, width=5, textvariable=t_unit, justify='center', state='readonly')
t_unit_chosen['values'] = ('C', 'F')
t_unit_chosen.grid(column=2, row=0)
t_unit_chosen.current(0)

# 'Output'

t_out = ttk.Label(tab1, text='OUTPUT=')
t_out.grid(column=0, row=1, sticky='E')

# Select output unit

t_unit_o = tk.StringVar()
t_unit_chosen_o = ttk.Combobox(
    tab1, width=5, textvariable=t_unit_o, justify='center', state='readonly')
t_unit_chosen_o['values'] = ('C', 'F')
t_unit_chosen_o.grid(column=2, row=1)
t_unit_chosen_o.current(1)

# Output Converted Value

temp_2 = tk.StringVar()
t_box_o = ttk.Entry(tab1, width=10, textvariable=temp_2, justify='center', state='disabled')
t_box_o.grid(column=1, row=1)


def convert():

    if t_unit_chosen.current() == 0 and t_unit_chosen_o.current() == 1:
        temp_21 = round(float(temp.get()) / 5 * 9 + 32, 2)
    elif t_unit_chosen.current() == 1 and t_unit_chosen_o.current() == 0:
        temp_21 = round((float(temp.get()) - 32) / 9 * 5, 2)
    else:
        temp_21 = float(temp.get())
    temp_2.set(temp_21)
    t_box.focus()  # Place cursor into Input Entry
    print(temp_21)

    fileTemp = open('Temp.txt', 'a')
    fileTemp.write(
        str(datetime.datetime.now()) + ' : ' +
        str(float(temp.get())) + ' unit ' + str(t_unit_chosen.current()) + ' = ' +
        str(temp_21) + ' unit ' + str(t_unit_chosen_o.current()) +
        '\n')
    fileTemp.close


def reset():
    temp.set('')
    temp_2.set('')
    t_box.focus()  # Place cursor into Input Entry


conv = ttk.Button(tab1, text='CONVERT', command=convert, width=15)
conv.grid(column=1, row=2, columnspan=2, ipadx=5, ipady=5, padx=5, pady=5)

reset_b = ttk.Button(tab1, text='RESET', command=reset, width=5)
reset_b.grid(column=0, row=2, ipadx=5, ipady=5, padx=5, pady=5)



win.mainloop()
