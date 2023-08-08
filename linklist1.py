class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        n = Node(item)
        if self.isEmpty():
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n

    def size(self):
        h = self.head
        size = 0
        while (h != None) :
            h = h.next
            size += 1
        return size
    
    def index(self, pos):
        if not self.isEmpty():
            h = self.head
            index = 0
            while (h != None) :
                if index == pos:
                    return h.value
                h = h.next
                index += 1
            return -1
        return -1

    def indexnext(self, pos):
        if not self.isEmpty():
            h = self.head
            index = 0
            while (h != None) :
                if index == pos:
                    if h.next != None:
                        return h.next.value
                    else:
                        return -1
                h = h.next
                index += 1
            return -1
        return -1
    
def ceil(num):
    if num%1 != 0:
        return int(num)+1
    return int(num)

def main():
    l = LinkedList()
    inp,k = input("Input : ").split("/")
    newinp = inp.split()
    for i in newinp:
        l.append(i)
    
    if int(k) <= l.size()+1:
        for i in range(ceil(l.size()/int(k))):
            data = l.index(i*int(k))
            nextdata = l.indexnext(i*int(k))
            print(f"Now index {i*int(k)} value is {data} next value is {nextdata}")
    else:
        print("Over length")



main()