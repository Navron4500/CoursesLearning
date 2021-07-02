class Stack:
    
    def __init__(self):
        self.__data = []

    def push(self,item):
        if self.isEmpty():
            print("Stack is empty")
            return 
        self.__data.append(item)

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return 
        self.__data.pop()

    def isEmpty(self):
        return len(self.__data) == 0

    def top(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        return self.__data[-1]

    def size(self):
        return len(self.__data)

s = 