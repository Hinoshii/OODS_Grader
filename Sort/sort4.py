class Monkey:
    def __init__(self, name, strength, intelligence, agility, id):
        self.name = name
        self.str = strength
        self.int = intelligence
        self.agi = agility
        self.id = id
    
    def __repr__(self) -> str:
        return str(self.id) + "-" + str(self.name)

class MinHeap:  
    def __init__(self):  
        self.heap = []
        
    def __len__(self):  
        return len(self.heap)  

    def parent(self, i):  
        return (i - 1) // 2  
    def left_child(self, i):  
        return 2 * i + 1  
    def right_child(self, i):  
        return 2 * i + 2  
    
    def insert(self, value):  
        self.heap.append(value)  
        i = len(self.heap) - 1 
        # value format : (str, agi, id) > (str, agi, id)
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            #swap node if child lessthan parent 
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]  
            i = self.parent(i)

    def get_min(self):  
        if len(self.heap) > 0:  
            return self.heap[0]  
        else:  
            return None  
        
    def extract_min(self):  
        if len(self.heap) == 0:  
            return None  
        min_val = self.heap[0]  
        self.heap[0] = self.heap[-1]  
        self.heap.pop()  
        i = 0  
        while (self.left_child(i) < len(self.heap)):  
            child_index = self.left_child(i)  
            if self.right_child(i) < len(self.heap) and self.heap[self.right_child(i)] < self.heap[self.left_child(i)]:  
                child_index = self.right_child(i)  
            if self.heap[i] > self.heap[child_index]:  
                self.heap[i], self.heap[child_index] = self.heap[child_index], self.heap[i]  
                i = child_index  
            else:  
                break  
        return min_val  
  
    #init heap
    def build_heap(self, input_list):
        for i in input_list:
            self.insert(i)  

class MaxHeap:  
    def __init__(self):  
        self.heap = []
        
    def __len__(self):  
        return len(self.heap)  

    def parent(self, i):  
        return (i - 1) // 2  
    def left_child(self, i):  
        return 2 * i + 1  
    def right_child(self, i):  
        return 2 * i + 2  
    
    def insert(self, value):  
        self.heap.append(value)  
        i = len(self.heap) - 1  
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            #swap node if child morethan parent 
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]  
            i = self.parent(i)

    def get_max(self):  
        if len(self.heap) > 0:  
            return self.heap[0]  
        else:  
            return None  
        
    def extract_max(self):  
        if len(self.heap) == 0:  
            return None  
        max_val = self.heap[0]  
        self.heap[0] = self.heap[-1]  
        self.heap.pop()  
        i = 0  
        while (self.left_child(i) < len(self.heap)):  
            child_index = self.left_child(i)  
            if self.right_child(i) < len(self.heap) and self.heap[self.right_child(i)] > self.heap[self.left_child(i)]:  
                child_index = self.right_child(i)  
            if self.heap[i] < self.heap[child_index]:  
                self.heap[i], self.heap[child_index] = self.heap[child_index], self.heap[i]  
                i = child_index  
            else:  
                break  
        return max_val  
  
    #init heap
    def build_heap(self, input_list):
        for i in input_list:
            self.insert(i)

#inp D/str,int,agi/caesar 100 10 100,kla 20 110 20,ton 20 111 10,non 20 110 20
monkelist = []
order,priority,monke = input("Enter Input : ").split("/")
priority = priority.split(",")
monke = monke.split(",")
ids = 0
for i in monke:
    i = i.split()
    m = Monkey(i[0],int(i[1]),int(i[2]),int(i[3]),ids) #name, strength, name, agility, id
    ids +=1
    monkelist.append(m)

item = []
for i in monkelist:
    temp = []
    for p in priority:
        if p == 'str':
            temp.append(i.str)
        elif p == 'name':
            temp.append(i.name)
        elif p == 'int':
            temp.append(i.int)
        elif p == 'agi':
            temp.append(i.agi)
    temp.append(i.id)
    temp = tuple(temp)
    item.append(temp)

if order == 'D':
    heap = MaxHeap()
elif order == 'A':
    heap = MinHeap()
heap.build_heap(item)

for i in range(len(monkelist)):
    if order == 'A':
        temp = heap.extract_min()
        print(temp)
    if order == 'D':
        temp = heap.extract_max()
        print(temp)