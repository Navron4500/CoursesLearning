class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    
    def __init__(self):
        self.root = None
        self.numNodes = 0
        
    def printTreeHelper(self,root):
        if not root:
            return
        
        print(root.data,end=":")
        if root.left:
            print("L:"+str(root.left.data),end=",")
        if root.right:
            print("R:"+ str(root.right.data),end="")
        print()
        
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)
        
    
    
    def printTree(self):
    ##################################
    # PLEASE IMPLEMENT THIS FUNCTION #
    ##################################
    	self.printTreeHelper(self.root)
    
    
    def search(self, data):
    ##################################
    # PLEASE IMPLEMENT THIS FUNCTION #
    ##################################
    	self.searchHelper(self.root,data)
        
    def searchHelper(self,root,data):
        if not root:
            return False
        
        if root.data == data:
            return True
        
        if root.data > data:
            return self.searchHelper(root.left,data)
        
        return self.searchHelper(root.right,data)
            
    
    

        
    def insert(self, data):
    ##################################
    # PLEASE IMPLEMENT THIS FUNCTION #
    ##################################
    	self.numNodes += 1
    	self.root = self.insertHelper(self.root,data)
        
    def insertHelper(self,root,data):
        if not root:
            node = BinaryTreeNode(data)
            return node
        
        if data > root.data:
            root.right = self.insertHelper(root.right,data)
            return root
        
        root.left = self.insertHelper(root.left,data)
        return root
            
    
    
    def mini(self,root):
        if not root:
            return 100000
        
        if not root.left:
            return root.data
        return self.mini(self.left)
      
        
    def delete(self, data):
        deleted,self.root = self.deleteHelper(self.root,data)
        if deleted:
            self.numNodes -= 1
        return deleted
    
    def deleteHelper(self,root,data):
        if not root:
            return False,None
        
        if root.data > data:
            deleted,root.left = self.deleteHelper(root.left,data)
            return deleted,root
        
        elif root.data < data:
            deleted,root.right = self.deleteHelper(root.right,data)
            return deleted,root
        
        else:
            if not root.left and not root.right:
                return True,None
            
            if not root.left and root.right:
                return True, root.right
            
            if not root.right and root.left:
                return True, root.left
            
            root.data = self.mini(root.right)
            deleted,root.right = self.deleteHelper(root.right,root.data)
            return True,root


b = BST()
b.insert(4)
b.insert(4)
b.insert(4)
b.insert(4)
b.printTree()
print("---------------")
print(b.delete(4))
b.printTree()

