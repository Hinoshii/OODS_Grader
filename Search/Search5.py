def getDistance(cord1,cord2):
    dis = ((cord1[0]-cord2[0])**2 + (cord1[1]-cord2[1])**2)**0.5
    return dis
#Enter a list of points: 1 1,2 2,3 3/1 1
inp, start = input("Enter a list of points: ").split("/")
start = list(map(float,start.split()))
inp = inp.split(",")
cords = []
for i in inp:
    i = list(map(float,i.split()))
    cords.append(i)

if start not in cords:
    #[0.0, 0.0] is not in [[123.0, 456.0], [-4627.0, 9921.0], [0.0, -716.0], [40.0, 32.0], [1.0, 738.0], [83.0, 0.0], [6321.0, 342.0]]
    print(f"{start} is not in {cords}")
    exit()

mindis = 5000000
closecords = 0
while(len(cords) != 1):
    for i in cords:
        dis = getDistance(i,start)
        if dis < mindis and dis != 0:
            mindis = dis
            closecords = i

    #[1.0, 1.0] -> [2.0, 2.0] | The distance is 1.4142
    print(f"{start} -> {closecords}",end="")
    print(" | The distance is " + "{:.4f}".format(mindis))

    cords.remove(start)
    start = closecords
    closecords = 0
    mindis = 5000000


