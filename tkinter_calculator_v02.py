import tkinter as tk
from tkinter import ttk, Menu
from tkinter import messagebox as msg
from tkinter.colorchooser import askcolor
import datetime

gui = tk.Tk()
gui.title('Tkinter Calculator v0.1')
gui.resizable(False, False)
gui.configure(background='grey94')

menu_bar = Menu(gui)
gui.config(menu=menu_bar)

def _gray():
    gui.configure(background='gray94')


def _skyBlue():
    gui.configure(background='skyblue1')


def _custom():
    result = askcolor(title='tkinter color')
    gui.configure(background=result[1])


def _msgBox_info():
    msg.showinfo('About', 'This GUI is created using tkinter.\n01/2021.')


def _msgBox_yn():
    answer = msg.askyesnocancel('Quit', 'Are you sure you want to quit?')
    if answer == True:
        quit()


background_menu = Menu(menu_bar, tearoff=0)
background_menu.add_command(label='Gray 94', command=_gray)
background_menu.add_command(label='Sky Blue 1', command=_skyBlue)
background_menu.add_separator()
background_menu.add_command(label='Custom', command=_custom)
menu_bar.add_cascade(label='Background Color', menu=background_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label='About', command=_msgBox_info)
help_menu.add_command(label='Quit', command=_msgBox_yn)
menu_bar.add_cascade(label='Help', menu=help_menu)

expression = ''

ttk.Style().configure('pad.TEntry', padding='5 5 5 5')


def press(number):
    global expression
    expression = expression + str(number)
    equation.set(expression)


def clr():
    global expression
    expression = ''
    equation.set(expression)


def delete():
    global expression
    expression = expression[:-1]
    equation.set(expression)


def equal():
    global expression

    fileTemp = open('temp_calc.text', 'a')
    fileTemp.write(
        str(datetime.datetime.now()) + ' : ' + expression
    )

    try:
        expression = str(eval(expression))
        equation.set(expression)
        fileTemp.write(
            '=' + expression
        )
    except SyntaxError:
        msg.showerror('Error Box', 'Please double check the expression.')
    except ZeroDivisionError:
        msg.showerror('Error Box', 'Cannot divide by zero.')
    fileTemp.write(
        '\n'
    )
    fileTemp.close


def pm():
    global expression
    if expression[0] == '-':
        expression = expression[1:]
    else:
        expression = '-' + expression
    equation.set(expression)


equation = tk.StringVar()
output = ttk.Entry(gui, textvariable=equation, state='disabled', style='pad.TEntry')
output.grid(column=0, row=0, columnspan=2, sticky='NSEW', padx=10, pady=10)
b_lp = ttk.Button(gui, text='(', command=lambda: press('('))
b_lp.grid(column=2, row=0, padx=10, pady=10, ipady=5)
b_rp = ttk.Button(gui, text=')', command=lambda: press(')'))
b_rp.grid(column=3, row=0, padx=10, pady=10, ipady=5)
# newline ---------------------------------
b_7 = ttk.Button(gui, text='7', command=lambda: press(7))
b_7.grid(column=0, row=1, padx=10, pady=10, ipady=5)
b_8 = ttk.Button(gui, text='8', command=lambda: press(8))
b_8.grid(column=1, row=1, padx=10, pady=10, ipady=5)
b_9 = ttk.Button(gui, text='9', command=lambda: press(9))
b_9.grid(column=2, row=1, padx=10, pady=10, ipady=5)
b_div = ttk.Button(gui, text=chr(247), command=lambda: press('/'))
b_div.grid(column=3, row=1, padx=10, pady=10, ipady=5)
# newline ---------------------------------
b_4 = ttk.Button(gui, text='4', command=lambda: press(4))
b_4.grid(column=0, row=2, padx=10, pady=10, ipady=5)
b_5 = ttk.Button(gui, text='5', command=lambda: press(5))
b_5.grid(column=1, row=2, padx=10, pady=10, ipady=5)
b_6 = ttk.Button(gui, text='6', command=lambda: press(6))
b_6.grid(column=2, row=2, padx=10, pady=10, ipady=5)
b_times = ttk.Button(gui, text=chr(215), command=lambda: press('*'))
b_times.grid(column=3, row=2, padx=10, pady=10, ipady=5)
# newline ---------------------------------
b_1 = ttk.Button(gui, text='1', command=lambda: press(1))
b_1.grid(column=0, row=3, padx=10, pady=10, ipady=5)
b_2 = ttk.Button(gui, text='2', command=lambda: press(2))
b_2.grid(column=1, row=3, padx=10, pady=10, ipady=5)
b_3 = ttk.Button(gui, text='3', command=lambda: press(3))
b_3.grid(column=2, row=3, padx=10, pady=10, ipady=5)
b_minus = ttk.Button(gui, text='-', command=lambda: press('-'))
b_minus.grid(column=3, row=3, padx=10, pady=10, ipady=5)
# newline ---------------------------------
b_pm = ttk.Button(gui, text='+/-', command=pm)
b_pm.grid(column=0, row=4, padx=10, pady=10, ipady=5)
b_0 = ttk.Button(gui, text='0', command=lambda: press(0))
b_0.grid(column=1, row=4, padx=10, pady=10, ipady=5)
b_dot = ttk.Button(gui, text='.', command=lambda: press('.'))
b_dot.grid(column=2, row=4, padx=10, pady=10, ipady=5)
b_add = ttk.Button(gui, text='+', command=lambda: press('+'))
b_add.grid(column=3, row=4, padx=10, pady=10, ipady=5)
# newline ---------------------------------
b_clr = ttk.Button(gui, text='CLR', command=clr)
b_clr.grid(column=0, row=5, padx=10, pady=10, ipady=5)
b_del = ttk.Button(gui, text='DEL', command=delete)
b_del.grid(column=1, row=5, padx=10, pady=10, ipady=5)
b_equal = ttk.Button(gui, text='=', command=equal)
b_equal.grid(column=2, row=5, columnspan=2, sticky='NSEW', padx=10, pady=10, ipady=5)

gui.mainloop()
