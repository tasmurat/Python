from tkinter import *

from tkinter.ttk import *

from time import strftime

root = Tk()

root.title("Clock")

def time():
    string = strftime("%H:%M:%S")
    label.config(text=string)
    label.after(1000,time)

label = Label(root, font=("Times New Roman",80), background = "green", foreground = "white")
label.pack(anchor="center")
time()

mainloop()