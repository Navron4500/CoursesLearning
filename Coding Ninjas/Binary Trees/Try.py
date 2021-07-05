class BinaryTreeNode:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
        
def printTree(root):
    if not root:
        return

    print(root.data, end=": ")
    if root.left:
        print("L",root.left.data,end=" ")
    if root.right:
        print("R",root.right.data,end=" ")
    print()
    printTree(root.left)
    printTree(root.right)

def treeInput(): 
    """
    Taking input According to Parent Children 
    """
    rootData = input()
    if not rootData:
        return None
    
    root = BinaryTreeNode(int(rootData))
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree
    return root


def printNodesWithoutSibling(root) :
    if not root or (not root.left and not root.right):
        return
    
    if not root.left:
        print(root.right.data, end=" ")
        printNodesWithoutSibling(root.right)
        return
    
    if not root.right:
        print(root.left.data, end=" ")
        printNodesWithoutSibling(root.left)
        return

    printNodesWithoutSibling(root.left)
    printNodesWithoutSibling(root.right)




root = treeInput()
printTree(root)
printNodesWithoutSibling(root)
