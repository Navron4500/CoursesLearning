import queue
class Stack :
    
	#Define data members and __init__()
    def __init__(self):
        self.__q1 = queue.Queue()
        self.__q2 = queue.Queue()
        self.__top = 0
        
    def getSize(self) :
        return self.__q1.qsize()
    
    def isEmpty(self) :
        return self.getSize() == 0
    
    def push(self, data) :
        self.__q1.put(data)
        self.__top = data
        
    def pop(self) :
		#Implement the pop() function
        if self.isEmpty():
            return -1
        
        while self.__q1.qsize() > 1:
            self.__q2.put(self.__q1.get())
            
        data = self.__q1.get()
        
        
        while self.__q2.qsize() > 1:
            self.__q1.put(self.__q2.get())

        if not self.__q2.empty() :
            self.__top = self.__q2.get()
            self.__q1.put(self.__top)
        else:
            self.__top = -1
        
        return data 
    
    def top(self) :
		#Implement the top() function
        if self.isEmpty():
            return -1
        return self.__top

s = Stack()
s.push(1)
s.push(2)
s.push(3)
while s.top() != -1:
    print(s.pop())
print(s.isEmpty())


        