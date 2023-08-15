class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
        self.gotPointed = 0 #tell how many node points to this one

    def __str__(self) -> str:
        alreadyCounted = []
        outputString = str(self.value)
        while self.next != None:
            if self.next.value in alreadyCounted:
                return outputString
            outputString += "->" + str(self.next.value)
            alreadyCounted.append(self.value)
            self = self.next
        return outputString
    
    def size(self):
        alreadyCounted = []
        size = 1
        while self.next != None:   
            if self.next.value in alreadyCounted:
                return size
            size +=1
            alreadyCounted.append(self.value)
            self = self.next
        return size
    
    def makeAList(self):
        alreadyCounted = []
        outputList = [self.value]
        while self.next != None:
            if self.next.value in alreadyCounted:
                return outputList
            outputList.append(self.next.value)
            alreadyCounted.append(self.value)
            self = self.next
        return outputList

inp = input("Enter edges: ").split(",")
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

#detect all node that intersect
removelist = []
for i in nodelist:
    if i.gotPointed > 1:
        removelist.append(i.value)
        print(f"Node({i.value}, size={i.size()})")

for i in nodelist:
    if i.value in removelist:
        if i.next != None:
            i.next.gotPointed -= 1

if removelist == []:
    print("No intersection")
    exit()

#making list yoi
trainlist = []
for i in nodelist:
    if i.gotPointed == 0:
        l = i.makeAList()
        trainlist.append(l)

#remove node that is intersect
newTrainList = []
for i in trainlist:
    newlist = []
    for j in i:
        if j in removelist:
            break
        newlist.append(j)
    newTrainList.append(newlist)

#swap merge
finalTrain = []
while(newTrainList != []):
    for i in newTrainList:
        if i != []:
            finalTrain.append(i.pop(0))
        elif i == []:    
            newTrainList.remove(i)

#output
outputString = ""
for i in finalTrain:
    if outputString == "":
        outputString += str(i)
    else:
        outputString += " -> " + str(i)
print("Delete intersection then swap merge:")
print(outputString)

