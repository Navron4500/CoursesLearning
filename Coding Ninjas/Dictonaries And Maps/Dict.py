# Hash Map
class MapNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

  
class Map:

    def __init__(self):
        self.bucketSize = 5
        self.buckets = [None for i in range(self.bucketSize)]
        self.count = 0
    
    def size(self):
        return self.count

    def compresionFunction(self,hc):
        return abs(hc)%(self.bucketSize)

    def insert(self,key,value):
        # Time Complexity = O(1)
        # Due to load factor < 0.7 (Reharsing)

        hc = hash(key)
        index = self.compresionFunction(hc)
        head = self.buckets[index]
        
        while head is not None:
            if head.key == key:
                head.value = value
                return 
            head = head.next

        head = self.buckets[index]        
        newNode = MapNode(key,value)
        newNode.next = head
        self.buckets[index] = newNode
        self.count += 1
        loadFactor = self.count/self.bucketSize
        if loadFactor >= 0.7:
            self.rehash()
         
    def remove(self,key):
        hc = hash(key)
        index = self.compresionFunction(hc)
        
        prev = None
        head = self.buckets[index]
        while head is not None:
            
            if head.key == key:
                if not prev:
                    prev = head.next
                else:
                    prev.next = head.next
                
                self.count -= 1
                self.buckets[index] = prev
                return head.value

            head = head.next
            prev = head

    def search(self,key):
        hc = hash(key)
        index = self.compresionFunction(hc)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None

    def rehash(self):
        temp = self.buckets
        self.buckets = [None for i in range(2*self.bucketSize)]
        self.bucketSize *= 2
        self.count = 0

        for head in temp:
            while head is not None:
                self.insert(head.key,head.value)
                head = head.next

    def loadFactor(self):
        return self.count / self.bucketSize


m = Map()
for i in range(10):
    m.insert("abc" + str(i), i+1)
    print(m.loadFactor())

for i in range(10):
    print("abc" + str(i)+":", m.search("abc" + str(i)))
    