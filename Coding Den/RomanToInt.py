def roman_to_int(ip, op = 0):
    roman_to_int_simple = {
        "I":1,
        "V":5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    roman_to_int_complicated = {
        "IV":4,
        "IX": 9,
        "LX": 40,
        "XC": 90,
        "DC": 400,
        "CM": 900
    }

    while ip:
        if len(ip) >= 2:
            smallip = [ip[-1], ip[-2], ip[-2:]]

        else:
            smallip = ip

        if "IV" in smallip or "IX" in smallip or "LX" in smallip or "XC" in smallip or "DC" in smallip or "CM" in smallip:
            
            for key, value in roman_to_int_complicated.items():
                if smallip[2] == key:
                    op += int(value)
                    break
            ip = ip[:-2]
        else:
            op += roman_to_int_simple[smallip[0]]
            ip = ip[:-1]

    return op


t1 = "III"
t2 = "IV"
t3 = "IX"
t4 = "LVIII"
t5 = "MCMXCIV"
t = t5[-2:]
op = roman_to_int(t5)
print(op)