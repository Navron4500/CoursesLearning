from sys import setrecursionlimit
def fibbo(n):
    if n == 1 or n==2:
        return 1
    output = fibbo(n-1) + fibbo(n-2)
    return output


def issorted(a):
    l = len(a)
    if l == 0 or l == 1:
        return True
    
    if a[0] > a[1]:
        return False
    
    smallerlist = a[l:]
    isSmallerListSorted = issorted(smallerlist)
    return isSmallerListSorted

def sumArray(arr):
    l = len(arr)
    # Please add your code here
    if l == 0 or l == 1:
        return arr[0]
    num = sumArray(arr[:l-2])
    added = num + arr[l-1]
    return added

# Main

setrecursionlimit(11000)
n=int(input("2INPUT PLEASE"))
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))

"""n = int(input("Enter Input: "))
print(fibbo(n))"""
#a = [1,2,3,4,5]
#b = [0,1,2,5,2]
#print(issorted(b))
#print(b[:6])
