def staircase(length,i):
    if abs(length)-i == 0:
        if length < 0:
            print("_" * (abs(length+i)) + "#" * i)
        else:
            print("_" * (i-1) + "#" * (length-i+1))
        return
    else:
        staircase(length,i+1)
    if length < 0:
        print("_" * (abs(length+i)) + "#" * i)
    else:
        print("_" * (i-1) + "#" * (length-i+1))

inp = input("Enter Input : ")
if int(inp) == 0:
    print("Not Draw!")
else:
    staircase(int(inp),1)
