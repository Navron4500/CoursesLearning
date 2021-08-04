# Complete Binary Tree (CBT)

class PriorityQueueNode:
    def __init__(self,value,priority) -> None:
        self.value = value
        self.priority = priority

class PriorityQueue:
    def __init__(self) -> None:
        self.pq = []

    def getSize(self):
        return len(self.pq)

    def isEmpty(self):
        return self.getSize() == 0

    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].value

    def __percolateUp(self):
        childIndex = len(self.pq)-1
        while childIndex > 0:
            parentIndex = (childIndex-1)//2
            if self.pq[childIndex].priority < self.pq[parentIndex].priority:
                self.pq[childIndex], self.pq[parentIndex] = self.pq[parentIndex], self.pq[childIndex]
                childIndex = parentIndex
            else:
                break

    def insert(self,value,priority):

        node = PriorityQueueNode(value,priority)
        self.pq.append(node)
        self.__percolateUp()


    def __percolateDown(self):
        
        parentIndex = 0
        LeftChildIndex = 2*parentIndex+1
        RightChildIndex = 2*parentIndex+2

        while LeftChildIndex < self.getSize():
            minIndex = parentIndex

            if self.pq[minIndex].priority > self.pq[LeftChildIndex].priority:
                minIndex = LeftChildIndex
            
            if RightChildIndex < self.getSize() and self.pq[minIndex].priority > self.pq[RightChildIndex].priority:
                minIndex = RightChildIndex
            
            if minIndex == parentIndex:
                break

            self.pq[parentIndex],self.pq[minIndex] = self.pq[minIndex], self.pq[parentIndex]
            parentIndex = minIndex
            LeftChildIndex = 2*parentIndex+1
            RightChildIndex = 2*parentIndex+2
                  
    def removeMin(self):
        if self.isEmpty():
            return None
        self.pq[0], self.pq[-1] = self.pq[-1], self.pq[0]
        removedData = self.pq.pop().value
        self.__percolateDown()
        return removedData


pq = PriorityQueue()
pq.insert("A",10)
pq.insert("C",5)
pq.insert("B",90)
pq.insert("D",4)
for i in range(4):
    print(pq.removeMin())
