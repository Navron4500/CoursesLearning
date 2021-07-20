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


def NodePath(root,node):
    if not root:
        return []
    
    if root.data == node:
        a = []
        a.append(str(root.data))
        return 
    
    left = NodePath(root.left,node)
    right = NodePath(root.right,node)
    if left:
        val = root.data+""





root = levelWiseTreeInput()
rootToLeafPathsSumToK(root,13)
# printLevelWise(root)
