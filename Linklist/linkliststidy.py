# class Node:
#     def __init__(self,data) -> None:
#         self.data = data
#         self.next = None

# class List:
#     def __init__(self,head = None) -> None:
#         self.head = head
#         self.tail = None
#     def append(self,data):
#         n = Node(data)
#         if self.head == None:
#             self.head = n
#         else:
#             while(self.head.next != None):
#                 self.head.next = n
    
class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.listprint()