class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

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

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
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
            n.previous = self.tail
            self.tail = n

    def addHead(self, item):
        n = Node(item)
        if self.isEmpty():
            self.head = n
            self.tail = n
        else:
            self.head.previous = n
            n.next = self.head
            self.head = n

    def insert(self, pos, item):
        n = Node(item)
        if not self.isEmpty():
            if pos >= 0 : # pos is integer #

                if pos+1 <= self.size() :
                    h = self.head
                    if pos == 0:
                        h.previous = n
                        n.next = h
                        self.head = n

                    else : # pos not 0 #
                        rounds = pos
                        while rounds != 0 :
                            h = h.next
                            rounds -= 1
                        n.next = h
                        n.previous = h.previous
                        h.previous.next = n
                        h.previous = n
                else :
                    # pos exceed range #
                    self.append(item)

            else : # pos is negative no. #

                if pos*-1 <= self.size():
                    t = self.tail
                    rounds = (pos*-1)-1
                    while rounds != 0 :
                        t = t.previous
                        rounds -= 1
                    n.next = t
                    n.previous = t.previous
                    t.previous.next = n
                    t.previous = n

                else :
                    # pos exceed range #
                    self.addHead(item)

        else : # list empty #
            self.head = n
            self.tail = n

    def search(self, item):
        if not self.isEmpty():
            h = self.head
            index = 0
            while (h != None) :
                if h.value == item:
                    return 'Found'
                h = h.next
                index += 1
            return 'Not Found'
        return 'Not Found'

    def index(self, item):
        if not self.isEmpty():
            h = self.head
            index = 0
            while (h != None) :
                if h.value == item:
                    return index
                h = h.next
                index += 1
            return -1
        return -1

    def size(self):
        h = self.head
        size = 0
        while (h != None) :
            h = h.next
            size += 1
        return size

    def pop(self, pos):
        if 0 <= pos and pos+1 <= self.size() and not self.isEmpty():
            h = self.head
            rounds = pos
            while rounds != 0 :
                h = h.next
                rounds -= 1

            if pos == 0 : # pop head #
                if self.size() == 1:
                    self.head = self.tail = None
                else :
                    self.head = h.next
                    h.next.previous = None
                    h.next = None

            elif pos+1 == self.size(): # pop tail #
                self.tail = h.previous
                h.previous.next = None
                h.previous = None
                
            else : # pop pos #
                h.previous.next = h.next
                h.next.previous = h.previous
                h.next = h.previous = None
            return 'Success'
        return 'Out of Range'
            


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())