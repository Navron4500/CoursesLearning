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

def printLL(head):
    while head:
        print(f"{head.data}->",end="")
        head = head.next
    print("None")
    return
 

def mergeTwoSortedLinkedLists(head1, head2):
    finalHead, tail = None, None
    
    if head1.data <= head2.data:
        finalHead, tail = head1, head1
        head1 = head1.next
    elif head2.data < head1.data:
        finalHead, tail = head2, head2
        head2 = head2.next

    while head1 and head2:
        if head1.data <= head2.data:
            tail.next = head1
            tail = tail.next
            head1 = head1.next

        elif head2.data < head1.data:
            tail.next = head2
            tail = tail.next
            head2 = head2.next

    if head1:
        tail.next = head1
        tail = tail.next
        head1 = head1.next

    if head2:
        tail.next = head2
        tail = tail.next
        head2 = head2.next

    return finalHead

def midPoint(head):
    slow , fast= head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def mergeSortLL(head):
    if not head:
        return None
    
    if not head.next:
        return head

    mid = midPoint(head)
    head2 = mid.next
    mid.next = None
    head1 = mergeSortLL(head)
    head2 = mergeSortLL(head2)

    return mergeTwoSortedLinkedLists(head1, head2)


head = takeinput()
printLL(head)

head = mergeSortLL(head)
printLL(head)