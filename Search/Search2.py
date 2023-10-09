inp = list(map(int,input("Data : ").split()))
lst = []
count = 1
longest = 0
for i in inp:
    if lst == []:
        lst.append(i)
    elif lst[-1] >= i:
        while(lst[-1] >= i):
            lst.pop()
            if lst == []:
                break
        lst.append(i)
    else:
        lst.append(i)
    
    if len(lst) > longest:
        longest = len(lst)
    print(f"{count} : {lst}")
    count +=1

print(f"longest increasing subsequence : {longest}")