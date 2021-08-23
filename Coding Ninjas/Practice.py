def countMinStepsToOne(n) :
    if n == 1 or n==0:
        return 0
    if n == 2 or n== 3:
        return 1

    dp = [-1 for i in range(n+1)]
    dp[0],dp[1] = 0,0
    
    i = 2
    while i <= n:
        ans = dp[i-1]
        if i%2 == 0:
            ans = dp[i//2]
        if i%3 == 0:
            ans = dp[i//3]

        dp[i] = ans+1
        i += 1
    
    return dp
   
n = 4
# dp = [-1 for i in range(n+1)]
print(countMinStepsToOne(n))