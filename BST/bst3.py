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

def father(node,value,ans="notFound"):
    if node != None:
        ans = father(node.right,value,ans)
        if node.right != None and node.right.data == value :
            ans = str(node.data)
        elif node.left != None and node.left.data == value :
            ans = str(node.data)
        ans = father(node.left,value,ans)
    return ans


tree = BinarySearchTree()
data = input("Enter Input : ").split("/")
for e in data[0].split():
    tree.create(int(e))
printTree90(tree.root)
ans = father(tree.root,int(data[1]))
if tree.root.data == int(data[1]):
    print(f'None Because {tree.root.data} is Root')
elif ans == 'notFound':
    print('Not Found Data')
else:
    print(ans)