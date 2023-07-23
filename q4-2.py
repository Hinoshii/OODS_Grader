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
    def head(self):
        return self.data[0]

class Customer:
    def __init__(self,timeJoin,duration,number,waiting_time=None) -> None:
        self.number = int(number)
        self.timeJoin = int(timeJoin)
        self.duration = int(duration)
        if waiting_time == None:
            self.waiting_time = 0
        else:
            self.waiting_time = int(waiting_time)

    def get_timeJoin(self):
        return int(self.timeJoin)

    def get_duration(self):
        return int(self.duration)
    def doCoffee(self):
        self.duration -= 1

    def get_number(self):
        return int(self.number)

    def get_waitingTime(self):
        return int(self.waiting_time)
    def add_waitingTime(self):
        self.waiting_time +=1

def checkArrive(log,time):
    arriveList = []
    for i in log:
        if i.get_timeJoin() == time:
            arriveList.append(i)
    return arriveList


def main():
    print(" ***Cafe***")
    b1 = Queue()
    b2 = Queue()
    wait = Queue()
    time = 0
    customerNo = 1
    longestWaitCustomer = 0
    longestTime = 0
    allCus = 0
    inp = input("Log : ").split('/')
    logList = []
    for i in inp:
        timeJoin,timeToMake = i.split(",")
        customer = Customer(timeJoin,timeToMake,customerNo)
        logList.append(customer)
        customerNo += 1
    allCus += len(logList)
    while(1):
        if not wait.isEmpty():
            for i in wait.data :
                i.add_waitingTime()

        if not b1.isEmpty() or not b2.isEmpty():
            if not b1.isEmpty():
                b1.head().doCoffee()
 
            if not b2.isEmpty():
                b2.head().doCoffee()

            # Who come first
            if b1.isEmpty():
                if b2.head().get_duration() == 0:
                        print(f"Time {time} customer {b2.head().get_number()} get coffee")
                        #check wait time
                        if b2.head().get_waitingTime() >= longestTime:
                            longestTime = b2.head().get_waitingTime()
                            longestWaitCustomer = b2.head().get_number()
                        b2.dequeue()
                        if not wait.isEmpty():
                            b1.enqueue(wait.dequeue())
            elif b2.isEmpty():
                if b1.head().get_duration() == 0:
                        print(f"Time {time} customer {b1.head().get_number()} get coffee")
                        #check wait time
                        if b1.head().get_waitingTime() >= longestTime:
                            longestTime = b1.head().get_waitingTime()
                            longestWaitCustomer = b1.head().get_number()
                        b1.dequeue()
                        if not wait.isEmpty():
                            b1.enqueue(wait.dequeue())
            elif not b1.isEmpty() and not b2.isEmpty():
                if b1.head().get_number() < b2.head().get_number():
                    if b1.head().get_duration() == 0:
                        print(f"Time {time} customer {b1.head().get_number()} get coffee")
                        #check wait time
                        if b1.head().get_waitingTime() >= longestTime:
                            longestTime = b1.head().get_waitingTime()
                            longestWaitCustomer = b1.head().get_number()
                        b1.dequeue()
                        if not wait.isEmpty():
                            b1.enqueue(wait.dequeue())

                    if b2.head().get_duration() == 0:
                        print(f"Time {time} customer {b2.head().get_number()} get coffee")
                        #check wait time
                        if b2.head().get_waitingTime() >= longestTime:
                            longestTime = b2.head().get_waitingTime()
                            longestWaitCustomer = b2.head().get_number()
                        b2.dequeue()
                        if not wait.isEmpty():
                            b2.enqueue(wait.dequeue())
                elif b1.head().get_number() > b2.head().get_number():
                    if b2.head().get_duration() == 0:
                        print(f"Time {time} customer {b2.head().get_number()} get coffee")
                        #check wait time
                        if b2.head().get_waitingTime() >= longestTime:
                            longestTime = b2.head().get_waitingTime()
                            longestWaitCustomer = b2.head().get_number()
                        b2.dequeue()
                        if not wait.isEmpty():
                            b2.enqueue(wait.dequeue())

                    if b1.head().get_duration() == 0:
                        print(f"Time {time} customer {b1.head().get_number()} get coffee")
                        #check wait time
                        if b1.head().get_waitingTime() >= longestTime:
                            longestTime = b1.head().get_waitingTime()
                            longestWaitCustomer = b1.head().get_number()
                        b1.dequeue()
                        if not wait.isEmpty():
                            b1.enqueue(wait.dequeue())

        arriveList = checkArrive(logList,time)
        allCus -= len(arriveList)
        if arriveList != []:
            for i in arriveList:
                if b1.isEmpty():
                    b1.enqueue(i)
                elif b2.isEmpty():
                    b2.enqueue(i)
                else :
                    wait.enqueue(i)

        if b1.isEmpty() and b2.isEmpty() and wait.isEmpty() and allCus == 0:
            break

        time += 1

    if longestTime != 0 :
            print(f"The customer who waited the longest is : {longestWaitCustomer}")
            print(f"The customer waited for {longestTime} minutes")
    else :
        print("No waiting")

main()