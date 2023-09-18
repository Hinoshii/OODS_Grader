class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None
                
def addnode(node,father,value):
    if node != None:
        addnode(node.right,father,value)
        if node.data == father:
            if node.left == None:
                node.left = Node(value)
            else:
                node.right = Node(value)
        addnode(node.left,father,value)

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def getleft(node,res=[]):
    if node != None:
        res = getleft(node.left,res)
        res.append(node.data)
        return res
    return res

def getright(node,res=[]):
    if node != None:
        res = getright(node.right,res)
        res.append(node.data)
        return res
    return res


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
first = data[0].split()
tree.root = Node(first[0])
for e in data:
    e = e.split()
    addnode(tree.root,e[0],e[1])
right = getright(tree.root)
right.reverse()
ans = getleft(tree.root)+(right[1:])
print("Top view : ",end = "")
print(*ans)