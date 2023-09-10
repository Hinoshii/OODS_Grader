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

def checklower(node,value,ans = []):
    if node != None:
        checklower(node.right,value,ans)
        if node.data < value:
            ans.append(node.data)
        checklower(node.left,value,ans)
    return ans

tree = BinarySearchTree()
data = input("Enter Input : ").split("|")
for e in data[0].split():
    tree.create(int(e))
ans = checklower(tree.root,int(data[1]))
ans.reverse()
printTree90(tree.root)
print('--------------------------------------------------')
print(f"Below {data[1]} : ",end="")

if ans == []:
    print("Not have")
else:
    print(*ans)
