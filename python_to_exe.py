import os
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import subprocess

current_directory = os.getcwd()
python_file_list = []

for file_name in os.listdir(current_directory):
    if ("." in file_name):
        split_file_name = file_name.split(".")
        extension = len(split_file_name) - 1
        if (split_file_name[extension] == "py"):
            python_file_list.append(file_name)

def run_cmd():
    select_file = lb.get(lb.curselection())
    os.system("cd " + current_directory)
    cmd = "pyinstaller " + select_file + " --onefile --noconsole"
    subprocess.call(cmd)
    os.system("rd /s /q __pycache__")
    os.system("rd /s /q build")
    split_select_file = select_file.split(".py")

    os.system("copy dist\\" + split_select_file[0] + ".exe " + current_directory)
    os.system("rd /s /q dist")
    # os.remove(split_select_file[0] + ".spec")
    root.withdraw()
    messagebox.showinfo("python exe化", "exeを作成しました！")
    root.destroy()

root = Tk()
root.title('pythonファイル名')
# フレーム
frame = ttk.Frame(root, padding=10)
frame.grid()
# リストボックス
v = StringVar(value=python_file_list)
lb = Listbox(
    frame, listvariable=v,
    selectmode='single', height=15, width=50)
lb.grid(row=0, column=0)
# Button
ok_button = ttk.Button(
    frame, text='OK',
    command=lambda: run_cmd())
ok_button.grid(row=1, column=0)
root.mainloop()

