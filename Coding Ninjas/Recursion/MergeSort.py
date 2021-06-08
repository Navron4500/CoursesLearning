def merge(arr, start1, end1, start2, end2):
    while start1 <= end1 and start2 <= end2:
        if arr[start1] > arr[start2]:
            arr.insert(start1, arr.pop(start2))
            start1 += 1
            start2 += 1


def mergeSort(arr, start, end):
    # Please add your code here
    if start == end or start > end:
        return

    mid = (start + end) // 2
    mergeSort(arr, start, mid)
    mergeSort(arr, mid + 1, end - 1)
    merge(arr, start, mid, mid + 1, end)


# Main
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
mergeSort(arr, 0, n)
print(*arr)

a = [5,4,3,2,1]
b = [9,87,5,2,4,1]
c = [9,3,7,4,2]
d = [29,28,27,26]
mergeSort(a, 0, len(a)-1)
print(*a)