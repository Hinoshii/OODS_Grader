def bubbleRecur(arr, n): #got this from my No1
    if n <= 1: #base (alr sorted)
        return arr

    def sorting(i):
        if i < n - 1:
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i] 
            sorting(i + 1)

    sorting(0)
    bubbleRecur(arr, n - 1)

inp = list(map(int,input("Enter Input : ").split()))
neglist = []
for index, value in enumerate(inp): #get negative pos
    if value < 0:
        neglist.append((index,value))

poslist = [e for e in inp if e>=0]

bubbleRecur(poslist,len(poslist))

for i in neglist: #insert neg back
    poslist.insert(i[0],i[1])

print(*poslist)