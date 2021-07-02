def stockSpan(price, n) :
    stack = []
    op = []
    for index,value in enumerate(price):
        if (index == 0 or price[stack[-1]]>value):
            op.append(1)
            stack.append(index)

        else:
            while stack and price[stack[-1]] < value:
                stack.pop()
            
            if stack:
                op.append(index-stack[-1])
            else:
                op.append(index+1)
            
            stack.append(index)
    return op

arr = [100, 80, 60, 70, 60, 75, 85]

# arr = list(map(int,input().split()))
print(stockSpan(arr,len(arr)))