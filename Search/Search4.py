#Enter Input : 5 1 67/1 6
#Enter Input : table max_col %treshold / Data(s)
def isPrime(n):
    if(n <= 1):
        return False
    if(n <= 3):
        return True
    
    if(n % 2 == 0 or n % 3 == 0):
        return False
     
    for i in range(5,int(n**0.5 + 1), 6): 
        if(n % i == 0 or n % (i + 2) == 0):
            return False
     
    return True

def nextPrime(N):
    if (N <= 1):
        return 2
 
    prime = N
    found = False
 
    while(not found):
        prime = prime + 1
 
        if(isPrime(prime) == True):
            found = True
 
    return prime

def printhash(table):
    for i in range(len(table)):
        print(f"#{i+1}	{table[i]}")
    print("----------------------------------------")

def hashing(data,tablesize,maxCol,tresh,currentNum,jumnuandata = 0,colcount=0):
    hashtable = [None]*int(tablesize)
    for i in data:
        if hashtable[i%int(tablesize)] == None:

            hashtable[i%int(tablesize)] = i
            jumnuandata +=1

            if i == currentNum:
                print(f"Add : {data[jumnuandata-1]}")

            print(jumnuandata*100/tablesize)
            if jumnuandata*100/tablesize >= tresh :
                print("****** Data over threshold - Rehash !!! ******")
                tablesize = nextPrime(2*tablesize)
                if len(data) >= jumnuandata+1:
                    hashing(data,tablesize,maxCol,tresh,data[jumnuandata])
                    exit()
                else:
                    hashing(data,tablesize,maxCol,tresh,data[jumnuandata-1])
                    exit()
            
            printhash(hashtable)

        else:
            colcount += 1
            print(f"collision number {colcount} at {i%int(tablesize)}")

            if colcount == maxCol :
                print("****** Max collision - Rehash !!! ******")
                tablesize = nextPrime(2*tablesize)
                hashing(data,tablesize,maxCol,tresh,data[jumnuandata-1])
                exit()
            
    return hashtable



inp,data = input("Enter Input : ").split("/")
data = list(map(int,data.split()))
tablesize, maxCol, tresh = inp.split()
print("Initial Table :")
printhash([None]*int(tablesize))
ans = hashing(data,int(tablesize),int(maxCol),int(tresh),data[0])