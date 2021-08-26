def keypad(n,d, soFar=""):
    if n == 0:
        print(soFar)
        return
    
    values = d[n]

    keypad(n//10,d,values[0]+soFar)



d = {
    2:["a","b","c"],
    3:["d","e","f"],
    4:["g","h","i"],
    5:["j","k","l"],
    6:["m","n","o"],
    7:["p","q","r","s"],
    8:["t","u","v"],
    9:["w","x","y","z"]
}

n = 23
ans = keypad(n,d)
print(*ans)