inp,maps = input("input : ").split(",")
row,col = inp.split()
realmap = []
for i in range(int(row)):
    realmap.append([0]*int(col))
maps = maps.split()
imap = 0
minval = 123456789
ind = 0
for i in range(int(row)):
    for j in range(int(col)):
        realmap[i][j] = int(maps[imap])
        if int(maps[imap]) < minval:
            minval = int(maps[imap])
            ind = (i,j)
        imap += 1
        
temp = 0
colind = 0
for i in range(int(col)):
    if realmap[ind[0]][i] > temp:
        temp = realmap[ind[0]][i]
        colind = i

temp = 0
for i in range(int(row)):
    if realmap[i][colind] > temp:
        temp = realmap[i][colind]
print(temp)

