n = [1,2,3,4,5,6,7,8,9,-1]

def arrayP(n, op=0):
    while n:
        n.remove(max(n))
        op += max(n)
        n.remove(max(n))
        n.remove(max(n))
        op += max(n)
        n.remove(max(n))
    return op

print(arrayP(n))


