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

        

def main():
    q = Queue()
    inp = input("Enter Input : ").split(",")
    for i in inp:
        j = i.split()
        if j[0] == 'E':
            a = q.enqueue(j[1])
            print(f"Add {j[1]} index is {q.data.index(j[1])}")
        elif j[0] == 'D':
            a = q.dequeue()
            if a == -1:
                print(-1)
            else:
                print(f"Pop {a} size in queue is {q.size()}")
    if q.isEmpty():
        print("Empty")
    else:
        print(f"Number in Queue is :  {q}")
main()