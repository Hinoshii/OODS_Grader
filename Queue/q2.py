class Queue:
    def __init__(self) -> None:
        self.data = []
    def __str__(self) -> str:
        return f"{self.data}"
    def replace(self,new):
        self.data = new
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

def main():
    qmain = Queue()
    q1 = Queue()
    q2 = Queue()
    q2time = 0
    inp,time = input("Enter people and time : ").split()
    qmain.replace(list(inp))
    for i in range(int(time)):
        if (i)%3 == 0 and not q1.isEmpty():
            q1.dequeue()
        if (q2time)%2 == 0 and not q2.isEmpty() and q2time != 0:
            q2.dequeue()
        if int(q1.size())<5 and not qmain.isEmpty():
            q1.enqueue(qmain.dequeue())
        elif int(q2.size())<5 and not qmain.isEmpty(): 
            q2.enqueue(qmain.dequeue())
        if not q2.isEmpty():
            q2time +=1
        else :
            q2time = 0
        print(f"{i+1} {qmain} {q1} {q2}")
main()