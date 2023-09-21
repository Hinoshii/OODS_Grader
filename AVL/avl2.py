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
        self.height = 1

    def getBalance(self):
        return self.getHeight(self.left) - self.getHeight(self.right)
    
    def getHeight(self,node):
        if node == None:
            return 0
        return node.height
    
    def setHeight(self):
        a = self.getHeight(self.left)
        b = self.getHeight(self.right)
        self.height = 1 + max(a,b)
        return self.height

class AVL_Tree(object):
    def insert(self, root, data):
        if root is None:
            return TreeNode(data)
        elif nameValue(data) < root.data[1]:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        root.setHeight()

        balance = root.getBalance() 
        # Case 1 - Left Left
        if balance > 1 and nameValue(data) < root.left.data[1]:
            return self.rightRotate(root)

        # Case 2 - Right Right
        if balance < -1 and nameValue(data) > root.right.data[1]:
            return self.leftRotate(root)

        # Case 3 - Left Right
        if balance > 1 and nameValue(data) > root.left.data[1]:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Case 4 - Right Left
        if balance < -1 and nameValue(data) < root.right.data[1]:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root
    
    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
 
        return self.getMinValueNode(root.left)
    
    def delete(self, root, key):
        if not root:
            return root
 
        elif key < root.data[1]:
            root.left = self.delete(root.left, key)
 
        elif key > root.data[1]:
            root.right = self.delete(root.right, key)
 
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
 
            elif root.right is None:
                temp = root.left
                root = None
                return temp
 
            temp = self.getMinValueNode(root.right)
            root.data = temp.data
            root.right = self.delete(root.right,temp.data[1])

            if root is None:
                return root
            balance = root.getBalance()
            # Case 1 - Left Left
            if balance > 1 and root.left.getBalance() >= 0:
                return self.rightRotate(root)
    
            # Case 2 - Right Right
            if balance < -1 and root.right.getBalance() <= 0:
                return self.leftRotate(root)
    
            # Case 3 - Left Right
            if balance > 1 and root.left.getBalance() < 0:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
    
            # Case 4 - Right Left
            if balance < -1 and root.right.getBalance() > 0:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
    
            return root

    def leftRotate(self, x) :
        y = x.right
        z = y.left
        y.left = x
        x.right = z
        y.setHeight()
        x.setHeight()
        return y
    
    def rightRotate(self, x) :
        y = x.left
        z = y.right
        y.right = x
        x.left = z
        y.setHeight()
        x.setHeight()
        return y

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
