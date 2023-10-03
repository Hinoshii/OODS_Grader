def checkMP(item,previous=None):
    flag = [True,False]
    for i in item:
        if previous == None:
            previous = i
        else:
            if previous > i:
                flag[0] = False
            if previous == i:
                flag[1] = True
            previous = i
    return flag

def checkKN(item,previous=None):
    flag = [True,False]
    for i in item:
        if previous == None:
            previous = i
        else:
            if previous < i:
                flag[0] = False
            if previous == i:
                flag[1] = True
            previous = i
    return flag

def checkR(item):
    if item.count(item[0]) == len(item):
        return True
    return False

inp = list(map(int,input("Enter Input : ")))
isDrome = False

if checkR(inp):
    print("Repdrome")
    exit()

drome = checkMP(inp)
if drome == [True,True]:
    print("Plaindrome")
    isDrome = True
elif drome == [True,False]:
    print("Metadrome")
    isDrome = True

drome = checkKN(inp)
if drome == [True,True]:
    print("Nialpdrome")
    isDrome = True
elif drome == [True,False]:
    print("Katadrome")
    isDrome = True

if not isDrome:
    print("Nondrome")

