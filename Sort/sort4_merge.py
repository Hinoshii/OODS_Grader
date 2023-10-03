class Monkey:
    def __init__(self, name, strength, intelligence, agility, id):
        self.name = name
        self.str = strength
        self.int = intelligence
        self.agi = agility
        self.id = id
    
    def __repr__(self) -> str:
        return str(self.id) + "-" + str(self.name)
    
def merge(arr, l, m, r): #left, mid, right
    n1 = m - l + 1
    n2 = r - m
 
    # Create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays 
    i = 0    
    j = 0    
    k = l     
 
    while i < n1 and j < n2:
        if order == 'A': #Id initially sorted by Ascending
            if L[i] < R[j] :
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        elif order == 'D': #if all att are same, sort by id (ascend)
            if (L[i] > R[j] and L[i][-1] != R[j][-1]) or (L[i][:-1] == R[j][:-1] and L[i][-1] < R[j][-1]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
    
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
def mergeSort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

def findMonke(lst,ids):
    for i in lst:
        if int(i.id) == ids :
            return i

monkelist = []
order,priority,monke = input("Enter Input: ").split("/")
priority = priority.split(",")
monke = monke.split(",")
ids = 0
for i in monke:
    i = i.split()
    m = Monkey(i[0],int(i[1]),int(i[2]),int(i[3]),int(ids)) #name, strength, name, agility, id
    ids +=1
    monkelist.append(m)

item = []
for i in monkelist:
    temp = []
    for p in priority:
        if p == 'str':
            temp.append(i.str)
        elif p == 'name':
            temp.append(i.name)
        elif p == 'int':
            temp.append(i.int)
        elif p == 'agi':
            temp.append(i.agi)
    temp.append(i.id)
    temp = tuple(temp)
    item.append(temp)

n = len(item)
mergeSort(item, 0, n-1)

res= []
for i in range(n):
    res.append(findMonke(monkelist,item[i][-1]))

print(res)