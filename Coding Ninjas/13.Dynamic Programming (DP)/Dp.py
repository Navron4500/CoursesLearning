import sys
sys.setrecursionlimit(10**4)
def mcm(p, i, j, dp):

    if i == j:
        return 0

    minCost = sys.maxsize
    for k in range(i,j):
        if dp[i][k] == -1:
            ans1 = mcm(p,i,k,dp)
            dp[i][k] = ans1
        else:
            ans1 = dp[i][k]
        
        if dp[k+1][j] == -1:
            ans2 = mcm(p,k+1,j,dp)
            dp[k+1][j] = ans2
        else:
            ans2 = dp[k+1][j]

        cost = ans1 + ans2 + (p[i-1 ] * p[k] * p[j])
        minCost = min(minCost,cost)

    return minCost



p,n = [10,15,20,25], 3 # 8000
dp = [[-1 for i in range(len(p))] for _ in range(len(p))]
print(mcm(p, 1, n, dp))