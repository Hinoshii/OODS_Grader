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
                
def printTree90(node, level = 0,ans =[]):
    if node != None:
        ans = printTree90(node.right, level + 1)
        if node.left == None and node.right == None:
            ans.append(level)
        ans = printTree90(node.left, level + 1)
    return ans

tree = BinarySearchTree()
inp = [int(i) for i in input('Enter input: ').split()]
for i in range(len(inp)):
    root = tree.create(inp[i])
ans = printTree90(tree.root)
print(f"{len(ans)} path(s)")
ans.sort()
for i in range(ans[-1]+1,0,-1):
    path = ans.count(i)
    if path != 0:
        print(f"{path} path(s) that pass through {i} node(s)")