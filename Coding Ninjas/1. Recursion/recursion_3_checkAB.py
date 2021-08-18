def checkAB(s,si=0):
    if si >=  len(s)-1:
        return True

    if s[0] != 'a':
        return False

    if s[si] == 'a': #and (s[si+1] == 'a' or (s[si+1] == 'b' and s[si+2] == 'b')):
        if s[si+1] == "a":
            res = checkAB(s,si+1)
            if res:
                return True
            return False
        
        elif s[si+1:si+3] == 'bb':
            res = checkAB(s,si+2)
            if res:
                return True
            return False    

        """if res:
            return True
        return False"""

    if s[si] == 'b': #and s[si+1] == 'a':  
        if s[si+1] == 'a':  
            res = checkAB(s,si+1)
            if res:
                return True
            return False

    return False

t1 = "abbab"
t2 = "abababa"
t3 = "babba"
t4 = "abbaabba"

print(checkAB(t1))

