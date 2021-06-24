import tkinter as tk
Calculator = tk.Tk()
Calculator.title('Calculator')

# Creatingn Input interface
tk.Label(Calculator,text="Number 1").grid(row=0)
tk.Label(Calculator,text="Number 2").grid(row=1)
ip1 = tk.Entry(Calculator)
ip2 = tk.Entry(Calculator)
ip1.grid(row=0,column=1)
ip2.grid(row=1,column=1)



def showOutput(ip1,ip2):
    res = int(ip1) + int(ip2)
    w = tk.Label(Calculator, text=str(res))

# Creating Add Button
add_button = tk.Button(Calculator, text="Add", width=25, command=showOutput(ip1,ip2)).grid(row=3)
add_button.pack()



Calculator.mainloop()