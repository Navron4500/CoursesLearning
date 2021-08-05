# Complete Binary Tree (CBT)

class PriorityQueueNode:
    def __init__(self,value,priority) -> None:
        self.value = value
        self.priority = priority

class PriorityQueue:
    def __init__(self) -> None:
        self.pq = []

    def isEmpty(self):
        return self.getSize() == 0
    
    def getSize(self):
        return len(self.pq)

    def getMax(self):
        if self.isEmpty():
            return None
        return self.pq[0].value
      

    def __percolateUp(self):
        childIndex = self.getSize()-1
        while childIndex > 0:
            parentIndex = (childIndex-1)//2

            if self.pq[childIndex].priority > self.pq[parentIndex].priority:
                self.pq[childIndex], self.pq[parentIndex] = self.pq[parentIndex], self.pq[childIndex]
                childIndex = parentIndex
            else:
                break

    def insert(self,ele,priority):
        Node = PriorityQueueNode(ele,priority)
        self.pq.append(Node)
        self.__percolateUp()


    def __percolateDown(self):
        parentIndex = 0
        leftChild = (2*parentIndex)+1
        rightChild = (2*parentIndex)+2

        while leftChild < self.getSize():
            maxIndex = parentIndex

            if self.pq[maxIndex].priority < self.pq[leftChild].priority:
                maxIndex = leftChild
            if rightChild < self.getSize() and self.pq[maxIndex].priority < self.pq[rightChild].priority:
                maxIndex = rightChild
            if maxIndex == parentIndex:
                break

            self.pq[maxIndex], self.pq[parentIndex] = self.pq[parentIndex], self.pq[maxIndex]
            parentIndex = maxIndex
            leftChild = (2*parentIndex)+1
            rightChild = (2*parentIndex)+2
        
    def removeMax(self):
        if self.isEmpty():
            return None
        self.pq[-1], self.pq[0] = self.pq[0], self.pq[-1]
        data = self.pq.pop().value
        self.__percolateDown()
        return data


pq = PriorityQueue()
pq.insert(5,5)
pq.insert(7,7)
pq.insert(3,3)
pq.insert(9,9)
pq.insert(1,1)
for _ in range(5):
    print(pq.removeMax())