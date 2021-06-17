# def sum_array(arr,n,num):
#     arr.sort()
#     i = 0
#     j = n-1
#     cnt = 0
#     while i<j:
#         s = arr[i]+arr[j]
#         if s>num:
#             j -= 1
#         elif s<num:
#             i += 1
#         else:
#             ai = int(arr[i+1] == arr[i] and i+1 != j) + int(arr[i] + arr[i+1]==num and i+1 != j)
#             aj = int(arr[j-1] == arr[j] and j-1 != i) + int(arr[j] + arr[j-1] == num and j-1 != i)
#             cnt += 1 + ai  + aj
#             i += 1
#             j -= 1
    
#     # if n%2 != 0:
#     #     return cnt-1
#     return cnt

def pairs_count(arr, n, sum):
     
    # To store the count of pairs
    ans = 0
 
    # Sort the given array
    arr = sorted(arr)
 
    # Take two pointers
    i, j = 0, n - 1
 
    while (i < j):
         
        # If sum is greater
        if (arr[i] + arr[j] < sum):
            i += 1
 
        # If sum is lesser
        elif (arr[i] + arr[j] > sum):
            j -= 1
             
        # If sum is equal
        else:
             
            # Find the frequency of arr[i]
            x = arr[i]
            xx = i
            while (i < j and arr[i] == x):
                i += 1
 
            # Find the frequency of arr[j]
            y = arr[j]
            yy = j
            while (j >= i and arr[j] == y):
                j -= 1
 
            # If arr[i] and arr[j] are same
            # then remove the extra number counted
            if (x == y):
                temp = i - xx + yy - j - 1
                ans += (temp * (temp + 1)) // 2
            else:
                ans += (i - xx) * (yy - j)
 
    # Return the required answer
    return ans


arr = list(map(int,input().split()))
num = int(input())
# arr = [1, 5, 7, -1,5]
# num = 6
print(pairs_count(arr,len(arr),num))