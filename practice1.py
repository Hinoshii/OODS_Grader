class Stack:
    def __init__(self) -> None:
        self.data = []
    def __str__(self) -> str:
        return f"{self.data}"
    def push(self,item):
        self.data.append(item)
    def pop(self):
        pass
    def top(self):
        if self.isEmpty():
            return 404
        return self.data[-1]
    def isEmpty(self):
        if self.data == []:
            return True
        
def main():
    stack = Stack()
    a = 10
    stack.push(a)
    print(stack+a)


def main2():
    print([875]*[1])

main2()