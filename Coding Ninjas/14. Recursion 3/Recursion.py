import sys
sys.setrecursionlimit(10 ** 8)




def printAllSubsetsRec(arr, n, sum, v = []) :
 
    # If remaining sum is 0, then print all
    # elements of current subset.
    if (sum == 0) :
        v.reverse()
        print(*v)
        return
     
 
    # If no remaining elements,
    if (n == 0):
        return
 
    # We consider two cases for every element.
    # a) We do not include last element.
    # b) We include last element in current subset.
    printAllSubsetsRec(arr, n - 1, sum, v)
    v1 = [] + v
    v1.append(arr[n - 1])
    printAllSubsetsRec(arr, n - 1, sum - arr[n - 1], v1)



#taking input
def takeInput() :
    n = int(input().strip())

    if n == 0 :
        return list(), 0

    arr = [int(element) for element in list(input().strip().split(" "))]
    return arr, n


#printing the list of lists
def printListOfList(liOfLi) :
    for li in liOfLi :
        for elem in li :
            print(elem, end = " ")
        print()

#main
# arr, n = [5,12,3,17,1,18,15,3,7], 9
arr,n = [4,3,1],3

if n != 0 :
    k = 5
    liOfLi = printAllSubsetsRec(arr, n, k)
    # print(liOfLi)

    # printListOfList(liOfLi)

