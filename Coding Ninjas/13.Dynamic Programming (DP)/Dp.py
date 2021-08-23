def LisIndexMemo(li,start,end,dp):
    
    if start == end:
        dp[start] = 1
        return 1,1

    including_max = 1
    for i in range(start+1,end):
        if li[i] > li[start]:
            if dp[i] == -1:
                ans = LisIndexMemo(li,i,end,dp)
                dp[i] = ans
                further_including_max = ans[0]
            else:
                further_including_max = dp[i][0]
            including_max = max(further_including_max + 1,including_max)
    
    if dp[start+1] == -1:
        ans = LisIndexMemo(li,start+1,end,dp)
        dp[start+1] = ans
        excluding_max = ans[1]
    else:
        excluding_max = dp[start+1][1]

    overall_max = max(including_max,excluding_max)

    return including_max, overall_max

def LisIterative(li,n):
    dp = [[0 for j in range(2)] for i in range(n+1)]
    # dp.append([1,1])
    # dp.append([0,0])

    for i in range(n-1,-1,-1):

        including_max = 1
        for j in range(i+1,n):
            if li[j] > li[i]:
                including_max = max(including_max,1+dp[j][0])
            
        dp[i][0] = including_max
        
        excluding_max = dp[i+1][1]

        overallMax = max(including_max,excluding_max)
        dp[i][1] = overallMax
    
    return dp[0][1]
    


# li = [6,3,1,2,0,7,9] # 4
# li = [1,7,2,3,4,5,6,8,9] # 8
# li = [5,4,11,1,16,8] # 3
li = [1,2,2] #2
dp = [-1 for i in range(len(li)+1)]
print(LisIterative(li,len(li)))
