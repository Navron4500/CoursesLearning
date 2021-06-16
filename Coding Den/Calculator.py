import math
import time

def add():
    ip1 = int(input("Enter a number: "))
    ip2 = int(input("Enter a number: "))
    res = ip1 + ip2
    print(f"{ip1} + {ip2} = {res}")


def substrct():
    ip1 = int(input("Enter a number: "))
    ip2 = int(input("Enter a number: "))
    res = ip1 - ip2
    print(f"{ip1} - {ip2} = {res}")


def mul():
    ip1 = int(input("Enter a number: "))
    ip2 = int(input("Enter a number: "))
    res = ip1 * ip2
    print(f"{ip1} * {ip2} = {res}")


def div():
    ip1 = int(input("Enter a number: "))
    ip2 = int(input("Enter a number: "))

    res = ip1 / ip2
    print(f"{ip1} / {ip2} = {res}")


def sqr():
    ip1 = int(input("Enter a number: "))

    res = ip1**2
    print(f"Square of {ip1}= {res}")


def cube():
    ip1 = int(input("Enter a number: "))

    res = (ip1**2)*ip1
    print(f"Cube of {ip1} = {res}")


def sqrt():
    ip1 = int(input("Enter a number: "))

    res = ip1**(1/2)
    print(f"square root of {ip1} = {res}")


def cubert():
    ip1 = int(input("Enter a number: "))

    res = ip1**(1/3)
    print(f"cube root of {ip1} = {res}")


def cosec(x):
    return 1/(math.sin(x))


def sec(x):
    return 1/(math.cos(x))


def cot(x):
    return 1/(math.tan(x))


def trigno():
    functions = """\nEnter Trignometeric Function and angle separated by SPACE
    sin cos tan 
    cosec sec cot: \n"""

    func_dict = {
        "sin":math.sin,
        "cos":math.cos,
        "tan":math.tan,
        "cosec":cosec,
        "sec":sec,
        "cot":cot
    }


    ip1,ip2 = input(functions).split()
    ip2 = int(ip2)
    ip2_rad = math.radians(ip2)

    if ip1 in func_dict:
        res = func_dict[ip1](ip2_rad)  
        print(f"{ip1}({ip2}) = {res}")  # First Class Function Concepts Used

    else:
        print("Wrong input")
        

def acosec(x):
    return math.asin(1/x)


def asec(x):
    return math.acos(1/x)


def acot(x):
    return math.cot(1/x)


def inverse_trigno():
    functions = """\nEnter Trignometeric Function and separated by SPACE
    isin icos itan 
    icosec isec icot: \n"""

    func_dict = {
        "isin":math.asin,
        "icos":math.acos,
        "itan":math.atan,
        "icosec":acosec,
        "isec":asec,
        "icot":acot
    }


    ip1,ip2 = input(functions).split()
    ip2 = int(ip2)

    if ip1 in func_dict:
        res = func_dict[ip1](ip2)   # First Class Function Concepts Used
        res = math.degrees(res)
        print(f"{ip1}({ip2}) = {res}")

    else:
        print("Wrong input")


def menu():
    MENU = """  Select the Operation to Perfrom:
    1.addition          6.Cube Root 
    2.substract         7.Square 
    3.Division          8.Cube 
    4.Multiplication    9.Trignometery Function
    5.square Root       10.Inverse Trignometery
    q to exit:
    """
    MENU_dict = {
        "1":add,
        "2":substrct,
        "3":div,
        "4":mul,
        "5":sqrt,
        "6":cubert,
        "7":sqr,
        "8":cube,
        "9":trigno,
        "10":inverse_trigno
    }

    ip = ""
    while ip != 'q':

        ip = input(MENU)

        if ip in MENU_dict:
            MENU_dict[ip]()  # First Class Function Concepts Used
            time.sleep(2)   # Use of TIME library to wait for 2second before resuming the program
        
        elif ip != "q":
            print("INVALID INPUT TRY AGAIN..")

    print("*****THANK YOU FOR USING OUR SERVICE*****")


menu()