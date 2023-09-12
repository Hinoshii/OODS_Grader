def strLen(message,length,newmessage):
    if message == []:  
        print(newmessage)
        return length
    if length%2 == 0:
        newmessage = newmessage + (message.pop(0)) + "*" 
    elif length%2 == 1:
        newmessage = newmessage + (message.pop(0)) + "~" 
    ans = strLen(message,length+1,newmessage)
    return ans

inp = input("Enter Input : ")
lengths = strLen(list(inp),0,"")
print(lengths)