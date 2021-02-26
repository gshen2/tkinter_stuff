# Guoyang Shen 12/12/2020

# http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html

import tkinter as tk
from tkinter import ttk

gui = tk.Tk()
gui.title('Tkinter Calculator v0.1')
gui.resizable(False, False)
gui.configure(background='grey94')

expression = ''

ttk.Style().configure('pad.TEntry', padding='5 5 5 5', font=('Helvetica', 20))

def press(number):
    global expression
    expression += str(number)
    equation.set(expression)


def pm():
    global expression
    if float(expression[:2]) < 0:
        expression = expression[1:]
    else:
        expression = '-' + expression
    equation.set(expression)


def clear():
    global expression
    expression = ''
    equation.set(expression)


def delete():
    global expression
    expression = expression[:-1]
    equation.set(expression)


def equal():
    global expression
    expression = str(eval(expression))
    equation.set(expression)


equation = tk.StringVar()
output = ttk.Entry(gui, textvariable=equation, state='disabled', style='pad.TEntry')
output.grid(column=0, row=0, columnspan=4, sticky='NSEW', padx=10, pady=10)
# newline-------------------------------
b_7 = ttk.Button(gui, text='7', command=lambda: press(7))
b_7.grid(column=0, row=1, padx=10, pady=10, ipady=5)
b_8 = ttk.Button(gui, text='8', command=lambda: press(8))
b_8.grid(column=1, row=1, padx=10, pady=10, ipady=5)
b_9 = ttk.Button(gui, text='9', command=lambda: press(9))
b_9.grid(column=2, row=1, padx=10, pady=10, ipady=5)
b_add = ttk.Button(gui, text=chr(247), command=lambda: press('/'))
b_add.grid(column=3, row=1, padx=10, pady=10, ipady=5)
# newline-------------------------------
b_4 = ttk.Button(gui, text='4', command=lambda: press(4))
b_4.grid(column=0, row=2, padx=10, pady=10, ipady=5)
b_5 = ttk.Button(gui, text='5', command=lambda: press(5))
b_5.grid(column=1, row=2, padx=10, pady=10, ipady=5)
b_6 = ttk.Button(gui, text='6', command=lambda: press(6))
b_6.grid(column=2, row=2, padx=10, pady=10, ipady=5)
b_minus = ttk.Button(gui, text=chr(215), command=lambda: press('*'))
b_minus.grid(column=3, row=2, padx=10, pady=10, ipady=5)
# newline-------------------------------
b_1 = ttk.Button(gui, text='1', command=lambda: press(1))
b_1.grid(column=0, row=3, padx=10, pady=10, ipady=5)
b_2 = ttk.Button(gui, text='2', command=lambda: press(2))
b_2.grid(column=1, row=3, padx=10, pady=10, ipady=5)
b_3 = ttk.Button(gui, text='3', command=lambda: press(3))
b_3.grid(column=2, row=3, padx=10, pady=10, ipady=5)
b_times = ttk.Button(gui, text='-', command=lambda: press('-'))
b_times.grid(column=3, row=3, padx=10, pady=10, ipady=5)
# newline-------------------------------
b_pm = ttk.Button(gui, text='+/-', command=pm)
b_pm.grid(column=0, row=4, padx=10, pady=10, ipady=5)
b_0 = ttk.Button(gui, text='0', command=lambda: press(0))
b_0.grid(column=1, row=4, padx=10, pady=10, ipady=5)
b_dec = ttk.Button(gui, text='.', command=lambda: press('.'))
b_dec.grid(column=2, row=4, padx=10, pady=10, ipady=5)
b_div = ttk.Button(gui, text='+', command=lambda: press('+'))
b_div.grid(column=3, row=4, padx=10, pady=10, ipady=5)
# newline-------------------------------
b_clear = ttk.Button(gui, text='CLR', command=clear)
b_clear.grid(column=0, row=5, padx=10, pady=10, ipady=5)
b_clear = ttk.Button(gui, text='DEL', command=delete)
b_clear.grid(column=1, row=5, padx=10, pady=10, ipady=5)
b_equal = ttk.Button(gui, text='=', command=equal)
b_equal.grid(column=2, row=5, columnspan=2, sticky='NSEW', padx=10, pady=10, ipady=5)

gui.mainloop()

