"""def merge(a1, a2, arr):
    i = 0
    j = 0
    k = 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            arr[k] = a1[i]
            i += 1
            k +=1
        else:
            arr[k] = a2[j]
            j += 1
            k += 1
    while i < len(a1):
        arr[k] = a1[i]
        k += 1
        i += 1
    while j < len(a2):
        arr[k] = a2[j]
        j += 1
        k += 1
   
def mergeSort(a):
    if len(a) == 0:
        return 
    mid = len(a)//1
    a0 = a[0:mid]
    a1 = a[mid:]
    mergeSort(a0)
    mergeSort(a1)

    merge(a0,a2,a)"""


def merge(arr, s1, e1, s2, e2):
    while s1<=e1 and s2<=e2:
        if arr[s1] > arr[s2]:
            arr.insert(s1,arr.pop(s2))
            s1 += 1
            s2 += 1
        
        
     
def mergeSort(a, start, end):
    if start == end or start>end:
        return 
    
    mid = (start+(end))//2
    mergeSort(a,start,mid)
    mergeSort(a,mid+1, len(a)-1)
    merge(a, start, mid, mid+1, end)





a = [11,14,12,13]
b = [9,3,7,4,2]
mergeSort(b,0,len(b))
#mergeSrt(a)
print(*b)