import tkinter as tk,pymsgbox
from tkinter import *
root=tk.Tk()
hiddenmodule=['pymsgbox']
def zero():
    t.insert(END, 0)
    root.mainloop()


def one():
    t.insert(END, 1)
    root.mainloop()


def two():
    t.insert(END, 2)
    root.mainloop()


def three():
    t.insert(END, 3)
    root.mainloop()


def four():
    t.insert(END, 4)
    root.mainloop()


def five():
    t.insert(END, 5)
    root.mainloop()


def six():
    t.insert(END, 6)
    root.mainloop()


def seven():
    t.insert(END, 7)
    root.mainloop()


def eight():
    t.insert(END, 8)
    root.mainloop()


def nine():
    t.insert(END, 9)
    root.mainloop()

def plus():
    t.insert(END, "+")
    root.mainloop()

def minus():
    t.insert(END, "-")
    root.mainloop()

def divide():
    t.insert(END, "/")
    root.mainloop()

def mult():
    t.insert(END, "*")
    root.mainloop()

def ge():
    x=t.get()
    x=str(x)
    pymsgbox.alert("Result is : "+str(eval(x)))
    t.delete(0, END)


def clear():
    t.delete(0,END)

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.configure(background='black')
t=tk.Entry(root,bg='white')
t.grid(row=3,column=8)

tk.Button(root, text="0",command=zero,height=1,width=6,bd=4).grid(row=3, column=1, sticky=tk.W, pady=20,padx=20)
tk.Button(root, text="1",command=one,height=1,width=6,bd=4).grid(row=3, column=2, sticky=tk.W, pady=20,padx=20)
tk.Button(root, text="2",command=two,height=1,width=6,bd=4).grid(row=3, column=3, sticky=tk.W, pady=20,padx=20)
tk.Button(root, text="3",command=three,height=1,width=6,bd=4).grid(row=4, column=1, sticky=tk.W, pady=20,padx=20)
tk.Button(root, text="4",command=four,height=1,width=6,bd=4).grid(row=4, column=2, sticky=tk.W, pady=20,padx=20)
tk.Button(root, text="5",command=five,height=1,width=6,bd=4).grid(row=4, column=3, sticky=tk.W, pady=20,padx=20)
tk.Button(root, text="6",command=six,height=1,width=6,bd=4).grid(row=5, column=1, sticky=tk.W, pady=20,padx=20)
tk.Button(root, text="7",command=seven,height=1,width=6,bd=4).grid(row=5, column=2, sticky=tk.W, pady=20,padx=20)
tk.Button(root, text="8",command=eight,height=1,width=6,bd=4).grid(row=5, column=3, sticky=tk.W, pady=20,padx=20)
tk.Button(root, text="9",command=nine,height=1,width=6,bd=4).grid(row=15, column=1, sticky=tk.W, pady=20,padx=20)
tk.Button(root, text="+",command=plus,height=1,width=6,bd=4).grid(row=15, column=3, sticky=tk.W, pady=20,padx=20)
tk.Button(root, text="-",command=minus,height=1,width=6,bd=4).grid(row=15, column=2, sticky=tk.W, pady=20,padx=20)
tk.Button(root, text="/",command=divide,height=1,width=6,bd=4).grid(row=15, column=1, sticky=tk.W, pady=20,padx=20)
tk.Button(root, text="*",command=mult,height=1,width=6,bd=4).grid(row=16, column=1, sticky=tk.W, pady=20,padx=20)
tk.Button(root, text="clear",command=clear,height=1,width=6,bd=4).grid(row=16, column=2, sticky=tk.W, pady=20,padx=20)
tk.Button(root, text="Quit",command=lambda : sys.exit(),height=1,width=6,bd=4).grid(row=16, column=3, sticky=tk.W, pady=20,padx=20)
tk.Button(root, text="Submit", command=ge, height=1, width=6, bg='green2', bd=4).grid(row=3, column=5, sticky=tk.W,pady=20, padx=20)
tk.mainloop()
