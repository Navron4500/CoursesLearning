import queue
from threading import current_thread
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def printLevelWise(root):
    # Your code goes here
    if not root:
        return 
    
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        current_node = q.get()
        print(current_node.data,end=":")
        if current_node.left:
            print("L:" + str(current_node.left.data),end=", ")
            q.put(current_node.left)
        else:
            print("L: ",end=", ")
            
            
        if current_node.right:
            print("R:" + str(current_node.right.data),end=" ")
            q.put(current_node.right)
        else:
            print("R: ",end=" ")
        
        print("")


def levelWiseTreeInput():
    q = queue.Queue()
    rootData = input("Enter Root \n")
    if not rootData:
        return None
    
    root = BinaryTreeNode(int(rootData))
    q.put(root)
    while not q.empty():
        current_Node = q.get()

        print("Enter Left Child of ", current_Node.data)
        leftChidData = input()
        if leftChidData:
            leftChild = BinaryTreeNode(int(leftChidData))
            current_Node.left = leftChild
            q.put(leftChild)

        
        print("Enter Right Child of ", current_Node.data)
        rightChildData = input()
        if rightChildData:
            rightChild = BinaryTreeNode(int(rightChildData))
            current_Node.right = rightChild
            q.put(rightChild)

    return root


def printSubTreeNodes(root,k):
    if not root:
        return
    
    if k == 0:
        print(root.data)
        return

    printSubTreeNodes(root.left,k-1)
    printSubTreeNodes(root.right,k-1)


def printNodeAtK(root,target, k):
    if not root:
        return -1
    
    if root.data == target:
        printSubTreeNodes(root,k)
        return 0

    dL = printNodeAtK(root.left,target,k)
    if dL != -1:
        if dL + 1 == k:
            print(root.data)
        
        else:
            printSubTreeNodes(root.right,k-dL-2)
        
        return 1+dL

    dR = printNodeAtK(root.left,target,k)
    if dR != -1:
        if dR + 1 == k:
            print(root.data)
        
        else:
            printSubTreeNodes(root.right,k-dR-2)
        
        return 1+dR
    
    return -1





root = levelWiseTreeInput()
printNodeAtK(root,10,2)
# printLevelWise(root)
