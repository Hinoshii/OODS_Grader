def nameValue(val):
    sumname = 0
    for i in val:
        sumname += ord(i)
    return sumname

class TreeNode(object):
    def __init__(self, val):
        self.val = [val,nameValue(val)]
        self.left = None
        self.right = None
        self.height = 1
 
class AVL_Tree(object):
 
    def insert(self, root, key):
         
        if not root:
            return TreeNode(key[0])
        elif key[1] < root.val[1]:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
 
        root.height = 1 + max(self.getHeight(root.left),
                          self.getHeight(root.right))

        balance = self.getBalance(root)
 
        if balance > 1 and key[1] < root.left.val[1]:
            return self.rightRotate(root)

        if balance < -1 and key[1] > root.right.val[1]:
            return self.leftRotate(root)

        if balance > 1 and key[1] > root.left.val[1]:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and key[1] < root.right.val[1]:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root

    def delete(self, root, key):
 
        if not root:
            return root
 
        elif key[1] < root.val[1]:
            root.left = self.delete(root.left, key)
 
        elif key[1] > root.val[1]:
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
            root.val = temp.val
            root.right = self.delete(root.right,
                                      temp.val)

        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left),
                            self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)

        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)

        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
 
    def leftRotate(self, z):
 
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
 
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
 
        return y
 
    def rightRotate(self, z):
 
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
 
        return y
 
    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height
 
    def getBalance(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.left) - self.getHeight(root.right)
 
    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
 
        return self.getMinValueNode(root.left)
 
    def printTree(self, node, level = 1):
        if node != None:
            if node.left == None and node.right == None:
                pass
                self.printTree(node.left, level + 1)
                self.printTree(node.right, level + 1)
            else:
                if node.left != None :
                    print(f"{'    ' * level}{node.left.val[0]} ({node.left.val[1]})")
                    self.printTree(node.left, level + 1)
                else:
                    print('    ' * level+"*")
            
                
                if node.right != None :
                    print(f"{'    ' * level}{node.right.val[0]} ({node.right.val[1]})")
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
        root = avl_tree.insert(root, [data,nameValue(data)])
    elif op == "D":
        root = avl_tree.delete(root, [data,nameValue(data)])
    elif op == "P":
        if root:
            print(f"{root.val[0]} ({root.val[1]})")
        avl_tree.printTree(root)
        print("------------------------------")
