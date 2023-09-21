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
        while i > 0 and (self.heap[i][0] < self.heap[self.parent(i)][0] or (self.heap[i][0] == self.heap[self.parent(i)][0] and self.heap[i][1] < self.heap[self.parent(i)][1])):
            #swap node if child lessday than parent or equal day but lower Van no
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
            if self.heap[i][0] > self.heap[child_index][0] or (self.heap[child_index][0] == self.heap[i][0] and self.heap[child_index][1] < self.heap[i][1]):  
                self.heap[i], self.heap[child_index] = self.heap[child_index], self.heap[i]  
                i = child_index  
            else:  
                break  
        return min_val  
  
    #init heap
    def build_heap(self, vans):
        for i in range(1,int(vans)+1):
            self.insert((0,int(i))) ##(days,No.Van)

inp,queueing = input("Enter Input : ").split("/")
queueing = queueing.split()
min_heap = MinHeap()
min_heap.build_heap(inp)
cus_no = 0
for i in queueing:
    cus_no +=1
    van = min_heap.extract_min()
    print(f"Customer {cus_no} Booking Van {van[1]} | {i} day(s)")
    min_heap.insert((van[0]+int(i),van[1]))