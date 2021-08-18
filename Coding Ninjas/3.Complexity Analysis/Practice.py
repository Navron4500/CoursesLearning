# Python program for implementation of MergeSort
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



def intersect(a1,a2):
    mergeSort(a1)
    mergeSort(a2)
    i = 0
    j = 0
    op = []
    while i<len(a1):
        while a1[i]>=a2[j]:
            if a1[i] == a2[j]:
                op.append(a1[i])
                break
            j += 1
    
    return op

a = [1,2,3,4,5,6,7,9,10]
b = [2,4,6,8,10]
print(intersect(a,b))


