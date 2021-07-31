a = "2 1 3 4 5 6 7 1 2 "
b = a.split()



def maxfreq(arr):
    #Write your code here 
    d = {}
    for a in arr:
        d[a] = d.get(a,0) + 1
    
    max_li = [-1]
    maxi = -1000
    for key in d:
        if d[key] > maxi:
            max_li.append(key)
            maxi = d[key]
    
    return max_li[-1]
            

print(maxfreq(b))