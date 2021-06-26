import tkinter as tk
from functools import partial


Calculator = tk.Tk()
Calculator.title('Calculator')
Calculator.geometry("325x175")


def action():
    global expression
    try:
        expression = eval(ip.get())
        expression = str(expression)
        ip.delete(0,tk.END)
        ip.insert(0,expression)
    except ZeroDivisionError:
        ip.delete(0,tk.END)
        ip.insert(0,"ERROR")

def insert(n):
    global expression 

    expression += n
    ip.delete(0,tk.END)
    ip.insert(0,expression)

def clear():
    global expression
    expression = ""
    ip.delete(0,tk.END)

expression = ""

# BUTTONS
ip = tk.Entry(Calculator,width=25)

equalBt = tk.Button(Calculator,text="=",command=action)
clearBt = tk.Button(Calculator,text="Clear",command=clear)

addBt  = tk.Button(Calculator,text="+",command=lambda: insert("+"))  
subsBt  = tk.Button(Calculator,text="-",command=lambda: insert("-")) 
multiBt  = tk.Button(Calculator,text="*",command=lambda: insert("*")) 
divBt  = tk.Button(Calculator,text="/",command=lambda: insert("/")) 

one = tk.Button(Calculator,text="1",command=lambda: insert("1")) 
two  = tk.Button(Calculator,text="2",command=lambda: insert("2")) 
three  = tk.Button(Calculator,text="3",command=lambda: insert("3")) 
four  = tk.Button(Calculator,text="4",command=lambda: insert("4")) 
five  = tk.Button(Calculator,text="5",command=lambda: insert("5")) 
six  = tk.Button(Calculator,text="6",command=lambda: insert("6")) 
seven  = tk.Button(Calculator,text="7",command=lambda: insert("7")) 
eight  = tk.Button(Calculator,text="8",command=lambda: insert("8")) 
nine  = tk.Button(Calculator,text="9",command=lambda: insert("9")) 
zero  = tk.Button(Calculator,text="0",command=lambda: insert("0")) 


# Adding buttons
ip.place(height=100)

# addBt.grid(row=,column=)
# subsBt.pack()
# multiBt.pack()
# divBt.pack()

# one.pack()
# two.pack()
# three.pack()
# four.pack()
# five.pack()
# six.pack()
# seven.grid(row=1,column=0)
# eight.grid(row=2,column=1)
# nine.grid(row=3,column=2)
# zero.pack()

# equalBt.pack()
# clearBt.pack()


Calculator.mainloop()