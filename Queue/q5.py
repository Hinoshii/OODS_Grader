class Queue:
    def __init__(self) -> None:
        self.data = []
    def __str__(self) -> str:
        return f"{self.data}"
    def isEmpty(self):
        return self.size() == 0
    def enqueue(self,item):
        self.data.append(item)
    def dequeue(self):
        if self.isEmpty():
            return -1
        return self.data.pop(0)
    def size(self):
        return len(self.data)
    def head(self):
        return self.data[0]
    def clear(self):
        self.data = []
    
# Coordinates (x,y) == Room[y][x]

def checkAdjacent(room,path,width,height,oldpath):
    pos = path.head()
    x = pos[0]
    y = pos[1]

    #Check Top
    path.dequeue()
    if y-1 >= 0 :
        if room[y-1][x] == 'O':
            return 'Found Exit'
        if room[y-1][x] == '_':
            if (x,y-1) not in path.data and (x,y-1) not in oldpath.data:
                path.enqueue((x,y-1))
    #Check Right
    if x+1 < width :
        if room[y][x+1] == 'O':
            return 'Found Exit'
        if room[y][x+1] == '_':
            if (x+1,y) not in path.data and (x+1,y) not in oldpath.data:
                path.enqueue((x+1,y))
    #check Down
    if y+1 < height :
        if room[y+1][x] == 'O':
            return 'Found Exit'
        if room[y+1][x] == '_':
            if (x,y+1) not in path.data and (x,y+1) not in oldpath.data:
                path.enqueue((x,y+1))
    #Check Left
    if x-1 >= 0 :
        if room[y][x-1] == 'O':
            return 'Found Exit'
        if room[y][x-1] == '_':
            if (x-1,y) not in path.data and (x-1,y) not in oldpath.data:
                path.enqueue((x-1,y))

    if path.data == []:
        return 'Impossible'
    print(f"Queue: {path}")
    return 'Not Found Exit'

def checkValid(room,width,height):
    h =0
    for i in room:
        if len(i) != width:
            return False
        h +=1
    if h != height :
        return False
    if locateStart(room) == 404:
        return False
    return True

def locateStart(room):
    x = 0
    y = 0
    for i in room:
        for j in i:
            if j == 'F':
                return (x,y)
            x+=1
        y+=1
        x = 0
    return 404

def locateEnd(room):
    x = 0
    y = 0
    for i in room:
        for j in i:
            if j == 'O':
                return (x,y)
            x+=1
        y+=1
        x = 0
    return 404
    
def main():
    path = Queue()
    oldpath = Queue()
    width,height,hong = input("Enter width, height, and room: ").split()
    room = hong.split(",")

    isValid = checkValid(room,int(width),int(height))

    if isValid:
        path.enqueue(locateStart(room))
        print(f"Queue: {path}")

    if not isValid:
        print('Invalid map input.')

    elif locateEnd(room) == 404 :
        print('Cannot reach the exit portal.')

    else:
        while(not path.isEmpty()):
            oldpath.enqueue(path.head())
            status = checkAdjacent(room,path,int(width),int(height),oldpath)
            if status == 'Found Exit':
                print('Found the exit portal.')
                break
            if status == 'Impossible':
                print('Cannot reach the exit portal.')
                break
main()