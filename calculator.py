
from tkinter import *

from pygments.lexers import q

root = Tk()
root.title("Calculator")
e = Entry(root,width=35,borderwidth=5)
e.grid(row=0, column=0, columnspan=3,padx=10, pady=10)

i=0
d=0
def badd(number):
    global i
    global d
    c = e.get()
    if d==1:
        e.delete(0,END)
        d=0
        return
    e.delete(0, END)
    if c.isdigit() or c=="":
       e.insert(0, str(c)+str(number))
    else:
        i+=1
        e.insert(0, str(float(c)+float(number*10**-i)))
        print(i)

def clear():
    global i
    i=0
    e.delete(0, END)

def add():
    global i
    i = 0
    global num1
    global math
    math = "add"

    num1 = float(e.get())
    e.delete(0, END)
def equal():
    global i
    i = 0
    global d
    d=1
    num2 = float(e.get())
    e.delete(0, END)
    if math == "add":
       e.insert(0, num1 + num2)
    if math == "sub":
        e.insert(0, num1 - num2)
    if math == "mul":
        e.insert(0, num1 * num2)
    if math == "div":
        e.insert(0, float(num1) / float(num2))

def sub():
    global i
    i = 0
    global num1
    global math
    math = "sub"
    num1 = float(e.get())
    e.delete(0, END)

def mul():
    global i
    i = 0
    global num1
    global math
    math = "mul"
    num1 = float(e.get())
    e.delete(0, END)

def div():
    global i
    i = 0
    global num1
    global math
    math = "div"
    num1 = float(e.get())
    e.delete(0, END)

def f():
     num1 = float(e.get())
     e.delete(0, END)
     e.insert(0, num1)
b1 = Button(root, text="1",padx=40, pady=20,command=lambda: badd(1) )
b2 = Button(root, text="2",padx=40, pady=20,command=lambda: badd(2) )
b3 = Button(root, text="3",padx=40, pady=20,command=lambda: badd(3) )
b4 = Button(root, text="4",padx=40, pady=20,command=lambda: badd(4) )
b5 = Button(root, text="5",padx=40, pady=20,command=lambda: badd(5) )
b6 = Button(root, text="6",padx=40, pady=20,command=lambda: badd(6) )
b7 = Button(root, text="7",padx=40, pady=20,command=lambda: badd(7) )
b8 = Button(root, text="8",padx=40, pady=20,command=lambda: badd(8) )
b9 = Button(root, text="9",padx=40, pady=20,command=lambda: badd(9) )
b0 = Button(root, text="0",padx=40, pady=20,command=lambda: badd(0) )
ba = Button(root, text="+",padx=39, pady=20,command=add )
be = Button(root, text="=",padx=88, pady=20,command=
equal )
bc = Button(root, text="clr",padx=85, pady=20,command=clear)
bs = Button(root, text="-",padx=40, pady=20,command=sub)
bm = Button(root, text="X",padx=40, pady=20,command=mul)
bd = Button(root, text="/",padx=40, pady=20,command=div)
bf = Button(root, text=".",padx=138, pady=20,command=f)

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
b0.grid(row=4, column=0)
ba.grid(row=5, column=0)
be.grid(row=5, column=1,columnspan=2)
bc.grid(row=4, column=1,columnspan=2)
bs.grid(row=6, column=0)
bm.grid(row=6, column=1)
bd.grid(row=6, column=2)
bf.grid(row=7, column=0,columnspan=4)
root.mainloop()
