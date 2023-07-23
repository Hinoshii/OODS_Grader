class Queue:
    def __init__(self) -> None:
        self.data = []
    def __str__(self) -> str:
        return f"{self.data}"
    def isEmpty(self):
        return self.size() == 0
    def enqueue(self,item):
        self.data.append(item)
    def dequeue(self):
        if self.isEmpty():
            return -1
        return self.data.pop(0)
    def size(self):
        return len(self.data)
    def updateTime(self):
        self.data[0] -=1
    def finishAt(self):
        if self.isEmpty():
            return 99999
        return int(self.data[0][0]+self.data[0][1]+self.data[0][2])
    
def main():
    print(" ***Cafe***")
    barista1 = Queue()
    barista2 = Queue()
    wait = Queue()
    time = 0
    customer = 1
    longestWaitCustomer = 0
    longestTime = 0
    inp = input("Log : ").split('/')
    for i in inp:
        timeJoin,timeToMake = i.split(",")
        while(time <= int(timeJoin)):
            if barista1.finishAt() <= time :
                print(f"Time {time} customer {barista1.data[0][3]} get coffee")
                barista1.dequeue()
            if barista2.finishAt() <= time :
                print(f"Time {time} customer {barista2.data[0][3]} get coffee")
                barista2.dequeue()
            if wait.finishAt() <= time :
                print(f"Time {time} customer {wait.data[0][3]} get coffee")
                wait.dequeue()
            time +=1

        time -=1

        if barista1.isEmpty() :
            barista1.enqueue([int(timeJoin),int(timeToMake),int(0),customer])
        elif barista2.isEmpty() : 
            barista2.enqueue([int(timeJoin),int(timeToMake),int(0),customer])
        else:
            if barista1.data[0][1]+barista1.data[0][0]-time > barista2.data[0][1]+barista2.data[0][0]-time:
                wait.enqueue([int(timeJoin),int(timeToMake),barista2.data[0][1]-time+barista2.data[0][0],customer])

                if barista2.data[0][1]-time+barista2.data[0][0] >= longestTime :
                    longestTime = barista2.data[0][1]-time+barista2.data[0][0]
                    longestWaitCustomer = customer

            if barista1.data[0][1]+barista1.data[0][0]-time <= barista2.data[0][1]+barista2.data[0][0]-time:
                wait.enqueue([int(timeJoin),int(timeToMake),barista1.data[0][1]-time+barista1.data[0][0],customer])
                if barista1.data[0][1]-time+barista1.data[0][0] >= longestTime :
                    longestTime = barista1.data[0][1]-time+barista1.data[0][0]
                    longestWaitCustomer = customer

        customer +=1

    customer -=1
    while(not barista1.isEmpty() or not barista2.isEmpty() or not wait.isEmpty()):
        if barista2.finishAt() <= time :
            print(f"Time {time} customer {barista2.data[0][3]} get coffee")
            barista2.dequeue()
        if barista1.finishAt() <= time :
            print(f"Time {time} customer {barista1.data[0][3]} get coffee")
            barista1.dequeue()
        

        if barista1.isEmpty() and not wait.isEmpty() :
            barista1.enqueue(wait.dequeue())
            print(barista1,barista2,wait)
        if barista2.isEmpty() and not wait.isEmpty():
            barista2.enqueue(wait.dequeue())
            print(barista1,barista2,wait)
        
        time +=1
    
    if longestTime != 0 :
        print(f"The customer who waited the longest is : {longestWaitCustomer}")
        print(f"The customer waited for {longestTime-1} minutes")
    else :
        print("No waiting")

        0,3/0,7/2,3/7,7/10,5/10,1
main()