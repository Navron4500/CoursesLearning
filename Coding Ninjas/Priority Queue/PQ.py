import heapq as heap
class LinkedListNode :
    def __init__(self, data) :
        self.data = data
        self.next = None
        
class Queue :
    def __init__(self) :
        self.head = None 
        self.tail = None
        self.size = 0
        
    def enqueue(self, data) :
        newNode = LinkedListNode(data)
        if self.head is None :
            self.head = self.tail = newNode
        else :
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
        return
        
    def dequeue(self) :
        if self.head is None :
            return None
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data
    
    def getSize(self) :
        return self.size
    
    def isEmpty(self) :
        if self.head is None :
            return True
        return False
    
    def peek(self) :
        if self.head is None :
            return None
        return self.head.data

def buyTicket(arr, n, k) : 
    q = Queue()
    count = 1
    heapMax = arr[:]
    heap._heapify_max(heapMax)
    for index in range(len(arr)):
        q.enqueue(index)

    while not q.isEmpty():
        if heapMax[0] == arr[q.peek()] and q.peek() == k:
            return count
            
        if heapMax[0] == arr[q.peek()]:
            heap._heappop_max(heapMax)
            q.dequeue()
            count += 1
        else:
            val = q.dequeue()
            q.enqueue(val)
    
    return None

# li = [2,3,2,2,4]
li = [3,9,4]
print(buyTicket(li,len(li),2))

