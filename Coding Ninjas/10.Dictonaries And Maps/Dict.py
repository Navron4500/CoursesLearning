def subsetSum(l):
    MaxSubSetLength = 0
    sumFromStart = 0
    sumDict = {}
    for i in range(len(l)):
        sumFromStart = sumFromStart + l[i]
        if sumFromStart in sumDict or sumFromStart == 0:
            if sumFromStart == 0 and sumFromStart not in sumDict:
                MaxSubSetLength = i+1
            elif i - sumDict[sumFromStart] > MaxSubSetLength:
                MaxSubSetLength = i - sumDict[sumFromStart]

        else:
            sumDict[sumFromStart] = i
        

    return MaxSubSetLength



l = [95, -97, -387, -435, -5, -70, 897, 127, 23, 284] #5
# l = [1,2,3,4,-10,-10] #5
# l = [2,-2,0,-2,2] # 5
print(subsetSum(l))