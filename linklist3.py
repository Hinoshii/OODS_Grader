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

    
def main():
    inp = input("Enter input: ").split()
    numbokey = inp[0]
    if len(inp) > 1:
        inp = inp[1].split(",")
        bokeylist = []
        trainlist = []
        #make bokeylist
        for i in range(int(numbokey)):
            bokeylist.append(i+1)
            
        for i in inp:
            checked = False
            bokey = i.split('-')
            if int(bokey[0]) in bokeylist:
                bokeylist.remove(int(bokey[0]))
            if int(bokey[1]) in bokeylist:
                bokeylist.remove(int(bokey[1]))

            for i in trainlist:
                #checktail
                if i.tail.value == bokey[0]:
                    i.append(bokey[1])
                    checked = True
                #checkhead
                if i.head.value == bokey[1]:
                    i.addHead(bokey[0])
                    checked = True

            #no train match
            if not checked:
                t = LinkedList()
                t.append(bokey[0])
                t.append(bokey[1])
                trainlist.append(t)

        for i in bokeylist:
            t = LinkedList()
            t.append(i)
            trainlist.append(t)

        #sorting
        for j in range(len(trainlist)-1):
            for i in range(len(trainlist)-1):
                if int(trainlist[i].head.value) > int(trainlist[i+1].head.value):
                    temp = trainlist[i+1]
                    trainlist[i+1] = trainlist[i]
                    trainlist[i] = temp

        count = 1
        for i in trainlist:
            print(f"{count}:",i)
            count+=1
        print(f"Number of train(s): {count-1}")
    else:
        bokeylist = []
        trainlist = []
        #make bokeylist
        for i in range(int(numbokey)):
            bokeylist.append(i+1)

        for i in bokeylist:
            t = LinkedList()
            t.append(i)
            trainlist.append(t)

        count = 1
        for i in trainlist:
            print(f"{count}:",i)
            count+=1
        print(f"Number of train(s): {count-1}")

main()