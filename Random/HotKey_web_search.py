import tkinter 
import webbrowser
import keyboard

def SearchInWeb():
    got = E1.get()
    got = got.split()
    # top.destory()
    toOpen = "https://duckduckgo.com/?q=" + "+".join(got) + "&t=h_&ia=web"
    webbrowser.open(toOpen)


top = tkinter.Tk()
L1 = tkinter.Label(top, text="What to Search")
L1.grid(row=0,column=0)

E1 = tkinter.Entry(top, bd =5)
E1.grid(row=0, column=1)

b1 = tkinter.Button(top, text="Search", command=SearchInWeb)
b1.grid(row=1,column=1)

# top.bind('<Control-f>', click)


top.mainloop()