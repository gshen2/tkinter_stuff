import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title('Python GUI')

# Label
a_label = ttk.Label(win, text='Hello World!')
a_label.grid(column=0, row=0)

# Button
def click_me():
    action.configure(text='** I have been Clicked! **')
    a_label.configure(foreground='red')
    a_label.configure(text='A Red Label')

action = ttk.Button(win, text='Click Me!', command=click_me)
action.grid(column=1, row=0)

# Text Box
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

# Button 2
def click_me_2():
    action2.configure(text='Hello ' + name.get() + '!')

action2 = ttk.Button(win, text='Hello', command=click_me_2)
action2.grid(column=1, row=1)

# Combo Box
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
number_chosen['values'] = ('UK', 'US', 'Canada')
number_chosen.grid(column=0, row=2)
number_chosen.current(0)

win.mainloop()