import queue
class TreeNode:
    def __init__(self,data) -> None:
        self.data = data
        self.children = []

def treeInputLevelWise():
    q = queue.Queue()
    rootData = int(input("Enter Input: "))
    if rootData == -1:
        return None

    root = TreeNode(rootData)
    q.put(root)
    while not q.empty():
        current_node = q.get()
        print("Enter number of children for ",current_node.data)
        numChildren = int(input())
        for i in range(numChildren):
            print("Enter next child for ", current_node.data)
            childData = int(input())
            child = TreeNode(childData)
            current_node.children.append(child)
            q.put(child)
    
    return root

def printLevelWise(root):
    if not root:
        return 
    
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        current_node = q.get()
        print(current_node.data,end=":")
        for child in current_node.children:
            if child != current_node.children[-1]:
                print(child.data,end=",")
            else:
                print(child.data,end="")
            q.put(child)
        print()
