from sys import stdin

def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1



def intersection(arr1, arr2, n, m) :
	#Your code goes here
    mergeSort(arr1)
    mergeSort(arr2)
    i = 0
    j = 0 
    while i<n and j<m:
        while arr1[i]>=arr2[j] and i<m and j<n:
            if arr1[i] == arr2[j]:
                print(arr1[i])
                j += 1
                break
            j += 1
        i += 1
        

t = int(input())
for _ in range(t):
    m = int(input(""))
    m_list = list(map(int,input().split()))
    n = int(input(""))
    n_list = list(map(int,input().split()))
    print(intersection(m_list1,n_list,m,n))





















# Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    
    if n == 0 :
    	return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().strip())

while t > 0 :

    arr1, n = takeInput()
    arr2, m = takeInput()
    intersection(arr1, arr2, n, m)
    print()

    t -= 1