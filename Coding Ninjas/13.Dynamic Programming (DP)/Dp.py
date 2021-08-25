from sys import stdin

def knapsack(weights, values, n, maxWeight):
    if maxWeight <= 0:
        return 0
    
    if n == 1:
        return values[0]
    
    excluding_Ans = knapsack(weights[1:],values[1:],n-1,maxWeight) # EXCLUDING

    Including_Ans = weights[0] +  knapsack(weights[1:],values[1:],n-1,maxWeight - weights[0])   # INCLUDING

    return max(excluding_Ans,Including_Ans)



	

def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), list(), n, 0

    weights = list(map(int, stdin.readline().rstrip().split(" ")))
    values = list(map(int, stdin.readline().rstrip().split(" ")))
    maxWeight = int(stdin.readline().rstrip())

    return weights, values, n, maxWeight


#main
# weights, values, n, maxWeight = takeInput()

# weights, values, n, maxWeight =[1,2,4,5],[5,4,8,6],4,5 # 13
weights, values, n, maxWeight = [12,7,11,8,9],[24,13,23,15,16],5,26 # 51

print(knapsack(weights, values, n, maxWeight))