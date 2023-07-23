def isLessPriority(i,fromstack):
    if i == '-' or i =='+':
        iprior = 1
    elif i == '/' or i =='*':
        iprior = 2
    elif i == '^':
        iprior = 3
    elif i =='(' or i == ')':
        iprior = 4
    if fromstack == '-' or fromstack =='+':
        fprior = 1
    elif fromstack == '/' or fromstack =='*':
        fprior = 2
    elif fromstack == '^':
        fprior = 3
    elif fromstack =='(' or fromstack == ')':
        fprior = 4

    if iprior <= fprior :
        return True
    return False

def main():
    stack = []
    answer = ""
    operatorList = ['+','-','/','*','^','(',')']
    inp = input("Enter Infix : ")
    for i in inp:
        if i not in operatorList:
            answer += i

        else :
            if i == '(':
                stack.append(i)


            elif i == ')':
                operator = stack.pop()

                while (operator != '('):
                    answer += operator
                    operator = stack.pop()
            else:
                while ((stack != []) and (isLessPriority(i,stack[-1])) and stack[-1] != '('):
                    answer += stack.pop()

                stack.append(i)
    while (stack != []):
        answer += stack.pop()

    print(f"Postfix : {answer}")
main()