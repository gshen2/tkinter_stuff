import tkinter as tk
from tkinter import ttk
import datetime

win = tk.Tk()
win.iconbitmap('unit.ico')
win.title('Unit Converter')
win.resizable(False, False)

ttk.Style().configure('TButton', foreground='red')

# Tabs

tabControl = ttk.Notebook(win)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Temperature')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Length')
tabControl.pack(expand=1, fill='both')

# Input ---------------------------------------------------------------------
# Input Label

T_in_label = ttk.Label(tab1, text='Input:')
T_in_label.grid(column=0, row=0)

# Input Entry

T_input = tk.StringVar()
T_box_in = ttk.Entry(tab1, width=10, textvariable=T_input, justify='center')
T_box_in.grid(column=1, row=0)

# Input Units

T_unit = tk.StringVar()
T_unit_input = ttk.Combobox(tab1, width=5, textvariable=T_unit, state='readonly', justify='center')
T_unit_input['values'] = ('C', 'F')
T_unit_input.grid(column=2, row=0)
T_unit_input.current(0)

# Output ---------------------------------------------------------------------
# Output Label

T_out_label = ttk.Label(tab1, text='Output:')
T_out_label.grid(column=0, row=1)

# Output Entry

T_output = tk.StringVar()
T_box_out = ttk.Entry(tab1, width=10, textvariable=T_output, state='disabled', justify='center')
T_box_out.grid(column=1, row=1)

# Output Units

T_unit_2 = tk.StringVar()
T_unit_output = ttk.Combobox(tab1, width=5, textvariable=T_unit_2, state='readonly', justify='center')
T_unit_output['values'] = ('C', 'F')
T_unit_output.grid(column=2, row=1)
T_unit_output.current(1)

# Buttons -------------------------------------------------------------------


def convert():

    if T_unit_input.current() == 0:
        unit_input = 'C'
    else:
        unit_input = 'F'

    if T_unit_output.current() == 0:
        unit_output = 'C'
    else:
        unit_output = 'F'

    if T_unit_input.current() == 0 and T_unit_output.current() == 1:
        # F = C / 5 * 9 + 32
        T_output_value = round(float(T_input.get()) / 5 * 9 + 32, 2)
    elif T_unit_input.current() == 1 and T_unit_output.current() == 0:
        # C = (F - 32) / 9 * 5
        T_output_value = round((float(T_input.get()) - 32) / 9 * 5, 2)
    else:
        T_output_value = float(T_input.get())

    T_output.set(T_output_value)

    fileTemp = open('temp.txt', 'a')
    fileTemp.write(
        str(datetime.datetime.now()) + ' : ' + str(float(T_input.get())) + ' ' + unit_input
        + ' = ' + str(T_output_value) + ' ' + unit_output + '\n')
    fileTemp.close


def reset():
    T_input.set('')
    T_output.set('')
    T_box_in.focus()


conv_button = ttk.Button(tab1, text='CONVERT', command=convert, width=15)
conv_button.grid(column=1, row=2, columnspan=2, ipadx=5, ipady=5, padx=5, pady=5)

reset_button = ttk.Button(tab1, text='RESET', command=reset, width=5)
reset_button.grid(column=0, row=2, ipadx=5, ipady=5, padx=5, pady=5)

win.mainloop()
