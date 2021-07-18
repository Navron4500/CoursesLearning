import queue
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
            print("L:" + str(current_node.left.data),end=",")
            q.put(current_node.left)
        else:
            print("L: ",end=",")
            
            
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

def buildTree(postOrder, inOrder, n) :
    if len(postOrder) <= 0 or len(inOrder) <= 0 or n <= 0:
        return None

    root = BinaryTreeNode(int(postOrder[-1]))
    root_index = inOrder.index(postOrder[-1])
    postOrder = postOrder[:-1]
    LeftIO, RightIO = inOrder[:root_index], inOrder[root_index+1:]
    LeftPO, RightPO = postOrder[:len(LeftIO)], postOrder[ -len(RightIO):]
    root.left, root.right = buildTree(LeftPO,LeftIO,len(LeftIO)), buildTree(RightPO, RightIO, len(RightPO))
    return root

list1 = [4,5,2,6,7,3,1]
list2 = [4,2,5,1,6,3,7]
root = buildTree(list1, list2, len(list1))
printLevelWise(root)

