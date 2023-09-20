def nameValue(val):
    sumname = 0
    for i in val:
        sumname += ord(i)
    return sumname

class TreeNode(object):
    def __init__(self, val):
        self.data =[val,nameValue(val)]
        self.right = None
        self.left = None
        self.height = self.setHeight()

    def getBalance(self):
        return self.getHeight(self.left) - self.getHeight(self.right)
    
    def getHeight(self,node):
        if node == None:
            return -1
        return node.height
    
    def setHeight(self):
        a = self.getHeight(self.left)
        b = self.getHeight(self.right)
        self.height = 1 + max(a,b)
        return self.height

class AVL_Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            return TreeNode(data)
        else:
            if nameValue(data) < int(root.data[1]):
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
            root = self.rebalances(root)                
            return root
        
    def updateHeight(self, root):
        if root is not None:
            self._postOrder(root.left)
            self._postOrder(root.right)
            root.setHeight()

    def delete(self, root, data):
        self.updateHeight(self.root)
        if root is None : 
            return root
        if data < root.data[1] :
            root.left = self.delete(root.left, data)
        elif data > root.data[1] :
            root.right = self.delete(root.right, data)
        else :
            if root.left is None or root.right is None :
                root = root.left if root.right is None else root.right
            else :
                temp = root.left
                while temp.right is not None :
                    temp = temp.right
                root.data = temp.data
                root.left = self.delete(root.left, temp.data[1])
            root = self.rebalances(root)         
        return root

    def leftRotate(self, x) :
        y = x.left
        x.left = y.right
        y.right = x
        x = y
        x.right.setHeight()
        x.setHeight()
        return x
    
    def rightRotate(self, x) :
        y = x.right
        x.right = y.left
        y.left = x    
        x = y
        x.left.setHeight()
        x.setHeight()
        return x

    def rebalances(self, x):
        if x == None:
            return x
        balance = x.getBalance()
        if balance == -2 : 
            if x.right.getBalance() == 1 :
                x.right = self.leftRotate(x.right)
            x = self.rightRotate(x)
        elif balance == 2 : 
            if x.left.getBalance() == -1:   
                x.left = self.rightRotate(x.left)                                         
            x = self.leftRotate(x)
        x.setHeight()
        return x 

    def printTree(self, node, level = 1):
        if node != None:
            if node.left == None and node.right == None:
                pass
                self.printTree(node.left, level + 1)
                self.printTree(node.right, level + 1)
            else:
                if node.left != None :
                    print(f"{'    ' * level}{node.left.data[0]} ({node.left.data[1]})")
                    self.printTree(node.left, level + 1)
                else:
                    print('    ' * level+"*")
            
                
                if node.right != None :
                    print(f"{'    ' * level}{node.right.data[0]} ({node.right.data[1]})")
                    self.printTree(node.right, level + 1)
                else:
                    print('    ' * level+"*")

avl_tree = AVL_Tree()
root = None
inp = input("Enter the data of your friend: ").split(",")
print("------------------------------")
for i in inp:
    op, *data = i.split(" ")
    data = data[0] if data else ""
    if op == "I":
        root = avl_tree.insert(root, data)
    elif op == "D":
        root = avl_tree.delete(root, nameValue(data))
    elif op == "P":
        print(f"{root.data[0]} ({root.data[1]})")
        avl_tree.printTree(root)
        print("------------------------------")
