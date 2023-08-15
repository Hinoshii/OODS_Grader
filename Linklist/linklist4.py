class Node:
    def __init__(self,data):
        self.next = None
        self.slist = link()
        self.value = data
class Snode:
    def __init__(self,data):
        self.next = None
        self.value = data
class link:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self):
        if self.head == None:
            return ""
        cur, s = self.head, str(self.head.value)+ "," 
        while cur.next != None:
            s +=  str(cur.next.value) + "," 
            cur = cur.next
        return s
    def search(self,data):
        h = self.head
        while(h != None):
            if data.value == h.value:
                return 'Found'
            h = h.next
        return 404
    def next_node(self,data):
        if self.head == None:
            self.head = data
            self.tail = data
        elif self.search(data) == 'Found':
            pass
        else:
            self.tail.next = data
            self.tail = data
    def next_secondary_node(self,n,data):
        h = self.head
        while(h != None):
            if n == h.value:
                h.slist.next_node(data)
            h = h.next
    def show_all(self):
        h = self.head
        while(h != None):
            print(f"{h.value} : {h.slist}")
            h = h.next
            
        

inp = input("input : ").split(",")
l = link()
for i in inp:
    u = i.split(" ")
    if u[0] == "ADN":
        l.next_node(Node(u[1]))
    elif u[0] == "ADSN":
        h = u[1].split("-")
        l.next_secondary_node(h[0],Snode(h[1]))
l.show_all()