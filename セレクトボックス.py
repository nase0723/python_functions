import os
from tkinter import *
from tkinter import ttk

current_directory = os.getcwd()
listdir = os.listdir(current_directory)

def select_show(items):
    root = Tk()
    root.title('pythonファイル名')
    # フレーム
    frame = ttk.Frame(root, padding=10)
    frame.grid()
    # リストボックス
    v = StringVar(value=items)
    lb = Listbox(
        frame, listvariable=v,
        selectmode='single', height=15, width=50)
    lb.grid(row=0, column=0)
    # Button
    ok_button = ttk.Button(
        frame, text='OK',
        command=lambda: print("a"))
    ok_button.grid(row=1, column=0)
    root.mainloop()

select_show(listdir)