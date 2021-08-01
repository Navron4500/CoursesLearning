# Hash Map
class MapNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

  
class Map:

    def __init__(self):
        self.bucketSize = 10
        self.buckets = [None for i in range(self.bucketSize)]
        self.count = 0
    
    def size(self):
        return self.count

    def getBuckIndex(self,hc):
        return abs(hc)%(self.bucketSize)


    def insert(self,key,value):

        hc = hash(key)
        index = self.getBuckIndex(hc)
        head = self.buckets[index]
        
        while head is not None:
            if head.key == key:
                head.value = value
                return 
            head = head.next
        
        newNode = MapNode(key,value)
        newNode.next = head
        self.buckets[index] = newNode
        self.count += 1
         
    def remove(self,key):
        hc = hash(key)
        index = self.getBuckIndex(hc)
        
        prev = None
        head = self.buckets[index]
        while head is not None:
            
            if head.key == key:
                if not prev:
                    prev = head.next
                else:
                    prev.next = head.next
                
                self.buckets[index] = prev
                return head.value

            head = head.next
            prev = head

    def search(self,key):
        hc = hash(key)
        index = self.getBuckIndex(hc)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None



m = Map()
# print(m.size())
m.insert("Rohan",7)
# print(m.size())
m.insert("Naveen",10)
# print(m.size())
print(m.remove("Naveen"))
print(m.search("Naveen"))