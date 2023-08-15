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
    inp = input("input : ").split(',')
    q= Queue()
    errorDeque = 0
    errorInput = 0
    rear = 0
    for i in inp:
        print(f"Step : {i}")
        mode = i[0]
        if mode == 'E':
            for i in range(int(i[1:])):
                item = '*' + str(rear)
                q.enqueue(item)
                item = ""
                rear+=1
            print(f"Enqueue : {q}")
        elif mode == 'D':
            for i in range(int(i[1:])):
                if q.dequeue() == -1:
                    errorDeque += 1
            print(f"Dequeue : {q}")
        else :
            print(f"{q}")
            errorInput += 1
        print(f'Error Dequeue : {errorDeque}')
        print(f'Error input : {errorInput}')
        print(f'--------------------')
main()