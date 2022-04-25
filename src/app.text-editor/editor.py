# Licensed under the MIT License <https://opensource.org/licenses/MIT>
# Copyright (c) 2022, Shoops

from tkinter import *
from tkinter import filedialog
def new_file():
    text.delete(0.0,END)

def open_file():
    file1 = filedialog.askopenfile(mode='r')
    data=file1.read()
    text.delete(0.0,END)
    text.insert(0.0,data)

def save_file():
    filename = "untitled.txt"
    data=text.get(0.0,END)
    file1=open(filename, 'w')
    file1.write(data)

def save_as():
    file1=filedialog.asksavefile(mode='w')
