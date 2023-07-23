def lookBack(stack):
    stack.reverse()
    highest_now = 0
    see = 0
    for i in stack:
        if int(i) > int(highest_now):
            see +=1
            highest_now = i
    stack.reverse()
    return see

def main():
    stack = []
    inp = input("Enter Input : ").split(",")
    for i in inp :
        whatToDo = i.split()
        if whatToDo[0] == 'A':
            stack.append(whatToDo[1])
        if whatToDo[0] == 'B':
            seeing = lookBack(stack)
            print(seeing)
main()