def ManageStack(stack,inp):
    stackcpy = stack
    inp = inp.split()
    if inp[0] == 'A':
        stackcpy.append(inp[1])
        print(f"Add = {inp[1]}")
    elif inp[0] == 'P':
        if stackcpy == []:
            print(-1)
        else:
            num = stackcpy[-1]
            stackcpy.pop(-1)
            print(f"Pop = {num}")
    elif inp[0] == 'D':
        roundPop = 0
        if stackcpy == []:
            print(-1)
        else:
            for i in range(len(stack)):
                if stack[i-roundPop] == inp[1]:
                    stackcpy.pop(i-roundPop)
                    print(f"Delete = {inp[1]}")
                    roundPop +=1
    elif inp[0] == 'LD':
        roundPop = 0
        if stackcpy == []:
            print(-1)
        else:
            for i in range(1,len(stack)+1):
                if int(stack[-i+roundPop]) < int(inp[1]):
                    num = stack[-i+roundPop]
                    stackcpy.pop(-i+roundPop)
                    print(f"Delete = {num} Because {num} is less than {inp[1]}")
                    roundPop +=1
    elif inp[0] == 'MD':
        roundPop = 0
        if stackcpy == []:
            print(-1)
        else:
            for i in range(1,len(stack)+1):
                if int(stack[-i+roundPop]) > int(inp[1]):
                    num = stack[-i+roundPop]
                    stackcpy.pop(-i+roundPop)
                    print(f"Delete = {num} Because {num} is more than {inp[1]}")
                    roundPop +=1
    return stackcpy

def main():
    stack = []
    inp = input("Enter Input : ").split(",")
    for i in inp:
        stack = ManageStack(stack,i)
    stackanswer = [int(i) for i in stack]
    print(f"Value in Stack = {stackanswer}")
main()