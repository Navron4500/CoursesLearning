class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def takeinput(inputList):
    # inputList = list(map(int,input().split()))
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

def printLL(head):
    while head:
        print(f"{head.data}->",end="")
        head = head.next
    print("None")
    return

def lengthLL(head) :
    #Your code goes here
    lengthOfLL = 0
    while head:
        lengthOfLL += 1
        head = head.next

    return lengthOfLL 

def bubbleSort(head) :
    if not head:
        return head

    for _ in range(lengthLL(head)):
        
        temp = head

        while temp and temp.next:
            if temp.data > temp.next.data:
                temp.data, temp.next.data = temp.next.data, temp.data
            temp = temp.next

        # if subhead.data == data:
        #     subhead = subhead.next


    return head


arr = [10,-5,9,90,5,67,1,89]
head = takeinput(arr)
printLL(head)

head = bubbleSort(head)
printLL(head)