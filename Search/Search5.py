def getDistance(cord1,cord2):
    dis = ((cord1[0]-cord2[0])**2 + (cord1[1]-cord2[1])**2)**0.5
    return dis
#Enter a list of points: 1 1,2 2,3 3/1 1
inp, start = input("Enter a list of points: ").split("/")
start = tuple(map(int,start.split()))
inp = inp.split(",")
cords = []
for i in inp:
    i = list(map(int,i.split()))
    i = tuple(i)
    cords.append(i)
print(cords,start)

getDistance(cords[1],start)