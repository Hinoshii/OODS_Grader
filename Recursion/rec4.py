#get powerset of all goods
def getNewSet(base,newMember,rounds):
    if rounds == 0:
        return 0
    else:
        getNewSet(base,newMember,rounds-1)
        base.append(base[rounds-1] + newMember)
        return base
def powerSet(L):
    if len(L) == 0:
        return [[]]
    else:
        base = powerSet(L[:-1]) #except last index
        newMember = L[-1:]
        powerset = getNewSet(base,newMember,len(base))
        return powerset

#detect set(list) that have sum == money
shopCart = []
def checkMoney(store,rounds):
    if rounds == 0:
        return 0
    else:
        checkMoney(store,rounds-1)
        if sum(store[rounds]) == int(money):
            print(store[rounds])
        return 0

#input
money,product = input('Enter Input (Money, Product) : ').split('/')
product = product.split() 
product = [int(e) for e in product]
# product.sort(reverse=True)
store = (powerSet(product))
print(store)
print('=======================')

#output
checkMoney(store,len(store)-1)

#right answer but wrong recursion (not intended way)