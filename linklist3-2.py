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
        cur, s = self.head, str(self.head.value)
        while cur.next != None:
            s +=  "->" + str(cur.next.value)
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

    def addHead(self, item):
        n = Node(item)
        if self.isEmpty():
            self.head = n
            self.tail = n
        else:
            n.next = self.head
            self.head = n

    def size(self):
        h = self.head
        size = 0
        while (h != None) :
            h = h.next
            size += 1
        return size
    
    def search(self, item):
        if not self.isEmpty():
            h = self.head
            while (h != None) :
                if int(h.value) == int(item):
                    return 'Found'
                h = h.next
            return 'Not Found'
        return 'Not Found'

inp = input("Enter input: ").split()
numbokey = inp[0]
inp = inp[1].split(",")
trainlist = []
bokeylist = []
for i in inp:
    bokey = i.split('-')
    bokeylist.append((bokey[0],bokey[1]))

while(bokeylist != []):
    isChanging = True
    changelist = []
    train=LinkedList()
    train.append(bokeylist[0][0])
    train.append(bokeylist[0][1])
    bokeylist.pop(0)
    
    lasthead = train.head
    lasttail = train.tail
    while(isChanging):
        for i in bokeylist:
            if int(i[0]) == int(train.tail.value):
                train.append(i[1])
                changelist.append(bokeylist.index(i))
            if int(i[1]) == int(train.head.value):
                train.addHead(i[0])
                changelist.append(bokeylist.index(i))

        #check if train update size
        if train.tail != lasttail or train.head != lasthead:
            isChanging = True
            lasttail = train.tail
            lasthead = train.head
        else:
            isChanging = False

        changelist.sort()
        changelist.reverse()

    for i in changelist:
        bokeylist.pop(i)
    changelist = []

    trainlist.append(train)

#make new train for unlinked bokey
for i in range(int(numbokey)):
    isFound = False
    for j in trainlist:
        if j.search(i+1) == 'Found' :
            isFound = True
    if not isFound :
        train=LinkedList()
        train.append(i+1)
        trainlist.append(train)

#sorting
for j in range(len(trainlist)-1):
    for i in range(len(trainlist)-1):
        if int(trainlist[i].head.value) > int(trainlist[i+1].head.value):
            temp = trainlist[i+1]
            trainlist[i+1] = trainlist[i]
            trainlist[i] = temp

#output
count = 1
for i in trainlist:
    print(f"{count}:",i)
    count+=1
print(f"Number of train(s): {count-1}")


 
