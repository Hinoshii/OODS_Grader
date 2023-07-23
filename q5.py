class Queue:
    def __init__(self) -> None:
        self.data = []

    def __str__(self) -> str:
        return f"{self.data[-1]}"
    
    def isEmpty(self):
        return self.size() == 0
    
    def enqueue(self,item):
        self.data.append(item)

    def dequeue(self):
        if self.isEmpty():
            return -1
        return self.data.pop(0)
    
    def rear(self):
        return self.data[-1]
    
    def size(self):
        return len(self.data)
    
    def isFinding(self,ending):
        print(self.data[-1])
        if ending in self.data[-1] :
            return False
        return True
    
def locateStart(room):
    posx = 0
    posy = 0
    for i in room:
        for j in i:
            if j == 'F':
                pos = (posx,posy)
                return pos
            posx+=1
        posy+=1
        posx =0

def locateEnd(room):
    posx = 0
    posy = 0
    for i in room:
        for j in i:
            if j == 'O':
                pos = (posx,posy)
                return pos
            posx+=1
        posy+=1
        posx =0

def checkAdjacent(room,oldq):
    validPath = []
    for i in oldq:
        print(oldq)
        if int(i[0]) > 0:         
            if room[int(i[1])][int(i[0])-1] == '_':
                pos = (i[0],i[1]-1)
                if pos not in oldq and pos not in validPath:
                    validPath.append(pos)
        if int(i[1]) < len(room)-1:
            if room[int(i[1])+1][int(i[0])] == '_':
                pos = (i[0]+1,i[1])
                if pos not in oldq and pos not in validPath:
                    validPath.append(pos)
        if int(i[0]) < len(room)-1:
            if room[int(i[1])][int(i[0])+1] == '_':
                pos = (i[0],i[1]+1)
                if pos not in oldq and pos not in validPath:
                    validPath.append(pos)
        if int(i[1]) > 0:
            if room[int(i[1])-1][int(i[0])] == '_':
                pos = (i[0]-1,i[1])
                if pos not in oldq and pos not in validPath:
                    validPath.append(pos)
    return validPath

def main():
    q = Queue()
    wid,higt,hong = input("Enter width, height, and room: ").split()
    room = hong.split(",")
    start = locateStart(room)
    end = locateEnd(room)
    q.enqueue([start])
    print(f"Queue : {q.rear()}")

    while(q.isFinding(end)):
        path = checkAdjacent(room,q.rear())
        q.enqueue(path)
        print(f"Queue : {q.rear()}")
    print("Found the exit portal.")
main()