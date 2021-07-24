class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    
    def __init__(self) -> None:
        self.root = None
        self.numNodes = 0
        
    def isPresentHelper(self,root,data):
        if not root:
            None

        if root.data == data:
            return True
        
        if root.data > data: 
            self.isPresentHelper(data.left,data)
        else:
            return self.isPresentHelper(data.right,data)
        
    def isPresent(self,data):
        return self.isPresentHelper(self.root,data)
        
    def insertHelper(self,root,data):
        if not root:
            node = BinaryTreeNode(data)
            return node
        
        if root.data > data:
            root.left = self.insertHelper(root.left,data)
        else:
            root.right = self.insertHelper(root.right,data)
        
        return root

    def insert(self,data):
        self.insertHelper(self.root,data)

    def deleteData(self,data):
        return True

    def count(self,data):
        return 0

    def printTreeHelper(self,root):
        if not root:
            return None
        
        print(root.data,end=":")
        if root.left:
            print("L",root.left.data,end=",")
        if root.right:
            print("R",root.right.data,end="")
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)

    def printTree(self):
        self.printTreeHelper(self.root)


b = BST()
b.insert(4)
b.insert(2)
b.insert(6)
b.insert(5)
b.insert(7)
b.printTree()
