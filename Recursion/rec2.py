def strLen(limit,strings,i):
    if limit == i:
        return 0
    else:
        if i%2 == 1:
            print(strings[i] + "~",end = "")
        elif i%2 == 0:
            print(strings[i] + "*",end = "")
        strLen(limit,strings,i+1)

inp = input("Enter Input : ")
strLen(len(inp),inp,0)
print("")
print(len(inp))