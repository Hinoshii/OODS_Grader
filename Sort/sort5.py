def bubbleRecur(arr, n): #from No1
    if n <= 1: #base (alr sorted)
        return arr

    def sorting(i):
        if i < n - 1:
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i] 
            sorting(i + 1)

    sorting(0)
    bubbleRecur(arr, n - 1)

def bubble_nested(lst,sorting=True):
    n = len(lst)

    for i in range(n):
        if sorting == False :
            break
        sorting = False
        for j in range(0, n-i-1):
            if len(lst[j]) > len(lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                sorting=True
            elif len(lst[j]) == len(lst[j+1]):
                for i in range(len(lst[j])):
                    if lst[j][i] > lst[j+1][i]:
                        lst[j], lst[j+1] = lst[j+1], lst[j]
                        sorting=True
                        break
                    elif lst[j][i] < lst[j+1][i]:
                        break

def getsubs(lst):
    if len(lst) == 0:
        return [[]] 
    subsets = getsubs(lst[:-1])
    item = lst[-1]
    subsets += [subset + [item] for subset in subsets]
    return subsets

targetSum,inp = input("Enter Input : ").split("/")
inp = list(map(int,inp.split()))
bubbleRecur(inp,len(inp))
subs = getsubs(inp)

answer = []
for i in subs:
    if sum(i) == int(targetSum):
        answer.append(i)

if answer == []:
    print("No Subset")
    exit()

bubble_nested(answer)        
for i in answer:
    print(i)