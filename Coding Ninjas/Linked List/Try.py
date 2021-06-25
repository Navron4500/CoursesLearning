class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def takeinput():
    inputList = list(map(int,input().split()))
    inputList.append(int(-1))
    head = None
    tail = None
    for ele in inputList:
        if ele == -1:
            break
        
        NewNode = Node(ele)
        if not head:
            head = NewNode
            tail = NewNode
        else:
            tail.next = NewNode
            tail = tail.next

    return head

def printLL(head):
    while head:
        print(f"{head.data}->",end="")
        head = head.next
    print("None")
    return


def length(head) :
    #Your code goes here
    lengthOfLL = 0
    while head:
        lengthOfLL += 1
        head = head.next

    return lengthOfLL

def printIthNode(head, i):
    if length(head) < i:
        return
    index = 0
    while head:
        if index == i:
            print(head.data)
            return
        index += 1
        head = head.next

def insertAtI(head,i,data):
    
    if i<0 or length(head) < i:
        return head
    
    count = 0
    prev = None
    curr = head
    while count < i:
        prev = curr
        curr = curr.next
        count += 1

    newNode = Node(data)
    if not i:
        head = newNode
    else:
        prev.next = newNode
    newNode.next = curr

    return head
    



head = takeinput()
printLL(head)
# print(length(head))
head = insertAtI(head,6,99)
printLL(head)