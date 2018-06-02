#!python3
"""
GUI script borrowed from Programming Python to map 
colors to and from RGB hex string values displayed
on stadndard output.  See also int(X, 16) builtin
to convert to hex from decimal.
"""
from tkinter import *
from tkinter.colorchooser import askcolor

def setBgColor():
    (triple, hexstr) = askcolor()
    if hexstr:
        print(hexstr)
        push.config(bg=hexstr)

root = Tk()
push = Button(root, text='Set Background Color', command=setBgColor)
push.config(height=3, font=('times', 20, 'bold'))
push.pack(expand=YES, fill=BOTH)
root.mainloop()
