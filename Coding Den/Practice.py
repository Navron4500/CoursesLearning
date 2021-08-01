import tkinter as tk


Calculator = tk.Tk()
Calculator.title('Calculator')
Calculator.geometry("250x175")

def action():
    global expression
    try:
        expression = eval(ip.get())
        expression = str(expression)
        ip.delete(0,tk.END)
        ip.insert(0,expression)
        expression = ""
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

equalBt = tk.Button(Calculator,text="=",width = 5,command=action)
clearBt = tk.Button(Calculator,text="Clear",width = 5,command=clear)

addBt  = tk.Button(Calculator,text="+",width = 5,command=lambda: insert("+"))  
subsBt  = tk.Button(Calculator,text="-",width = 5,command=lambda: insert("-")) 
multiBt  = tk.Button(Calculator,text="*",width = 5,command=lambda: insert("*")) 
divBt  = tk.Button(Calculator,text="/",width = 5,command=lambda: insert("/")) 

one = tk.Button(Calculator,text="1",width = 5,command=lambda: insert("1")) 
two  = tk.Button(Calculator,text="2",width = 5,command=lambda: insert("2")) 
three  = tk.Button(Calculator,text="3",width = 5,command=lambda: insert("3")) 
four  = tk.Button(Calculator,text="4",width = 5,command=lambda: insert("4")) 
five  = tk.Button(Calculator,text="5",width = 5,command=lambda: insert("5")) 
six  = tk.Button(Calculator,text="6",width = 5,command=lambda: insert("6")) 
seven  = tk.Button(Calculator,text="7",width = 5,command=lambda: insert("7")) 
eight  = tk.Button(Calculator,text="8",width = 5,command=lambda: insert("8")) 
nine  = tk.Button(Calculator,text="9",width = 5,command=lambda: insert("9")) 
zero  = tk.Button(Calculator,text="0",width=5,command=lambda: insert("0")) 
blankLabel = tk.Label(Calculator,text="",height=2)

# Adding buttons
ip.place(height=30)
blankLabel.grid(row=0,column=6)

addBt.grid(row=1,column=3)
subsBt.grid(row=1,column=4)
multiBt.grid(row=2,column=3)
divBt.grid(row=2,column=4)

one.grid(row=3,column=0)
two.grid(row=3,column=1)
three.grid(row=3,column=2)

four.grid(row=2,column=0)
five.grid(row=2,column=1)
six.grid(row=2,column=2)

seven.grid(row=1,column=0)
eight.grid(row=1,column=1)
nine.grid(row=1,column=2)

zero.grid(row=4,column=0)

equalBt.grid(row=3,column=3)
clearBt.grid(row=3,column=4)


Calculator.mainloop()