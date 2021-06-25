class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def takeinput():
    inputList = list(map(int,input().split()))
    # inputList.append(int(-1))
    head = None
    tail = None
    for ele in inputList:
        # if ele == -1:
        #     break
        
        NewNode = Node(ele)
        if not head:
            head = NewNode
            tail = NewNode
        else:
            tail.next = NewNode
            tail = tail.next

    return head

def lengthLL(head) :
    #Your code goes here
    lengthOfLL = 0
    while head:
        lengthOfLL += 1
        head = head.next

    return lengthOfLL

def printLL(head):
    while head:
        print(f"{head.data}->",end="")
        head = head.next
    print("None")
    return

def deleteNodeR(head, pos) :
    if pos<0:
        return head

    if not head:
        return None

    if pos == 0:
        return head.next

    smallhead = deleteNodeR(head.next,pos-1)
    head.next = smallhead
    return head
    
def findNode(head, n) :
    index = 0
    while head:
        if head.data == n:
            return index
        head = head.next
        index += 1
    
    return -1    

def appendLastNToFirst(head, n):
    Length = length(head)
    find = Length - n
    index = 0
    
    prev = None
    curr = head
    while index < find:
        prev = curr
        curr = curr.next
        index += 1
    
    prev.next = None
    prev = curr

    while curr.next:
        curr = curr.next

    curr.next = head
    head = prev

    return head

head = takeinput()
printLL(head)
# head.data, head.next.next.data = head.next.next.data, head.data
head = appendLastNToFirst(head,5)
printLL(head)