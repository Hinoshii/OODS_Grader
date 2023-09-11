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

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def checkpos(node, value, level = 0,found=False):
    if node != None:
        found = checkpos(node.right, value, level + 1,found)
        if node.data == value:
            if level == 0:
                print("Root")
                found = True
            elif node.right == None and node.left == None:
                print("Leaf")
                found = True
            else:
                print("Inner")
                found = True
        found = checkpos(node.left, value, level + 1,found)
    return found
    

tree = BinarySearchTree()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = tree.create(inp[i])
printTree90(tree.root)
isfound = checkpos(tree.root,inp[0])
if not isfound :
    print("Not exist")