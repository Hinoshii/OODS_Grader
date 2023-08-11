class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
        self.gotPointed = 0 #tell how many node points to this one

    def __str__(self) -> str:
        outputString = str(self.value)
        while self.next != None:
            outputString += "->" + str(self.next.value)
            self = self.next
        return outputString
    
    def size(self):
        size = 1
        while self.next != None:
            size +=1
            self = self.next
        return size
    
    def valueAtPosition(self,index):
        for i in range(index-1):
            self = self.next
        return self.value

inp = input().split(",")
valuelist = []
nodelist = []
for i in inp:
    values = i.split(">")
    for j in values:
        if int(j) not in valuelist:
            valuelist.append(int(j))
    valuelist.sort()

#making nodes
for i in valuelist:
    nodelist.append(Node(i))

#pointing node
for i in inp:
    head,tail = i.split(">")
    headpos = valuelist.index(int(head))
    tailpos = valuelist.index(int(tail))
    nodelist[headpos].next = nodelist[tailpos]
    nodelist[tailpos].gotPointed += 1

#remove all node that intersect
for i in nodelist:
    if i.gotPointed > 1:
        i.next.gotPointed -=1
        for j in nodelist:
            if j.next == i:
                j.next = None

for i in nodelist:
    if i.gotPointed == 0:
        print(i)