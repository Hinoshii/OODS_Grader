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

inp =   list(map(int,input("Enter Input: ").split())) 
min_cost = []
max_cost = []  

min_heap = MinHeap()
max_heap = MaxHeap()
min_heap.build_heap(inp)
max_heap.build_heap(inp)  

length = len(min_heap) 
for i in range(length-1):
    min1 = min_heap.extract_min()
    min2 = min_heap.extract_min()
    cost = min1+min2
    min_cost.append(cost)
    min_heap.insert(cost)
for i in range(length-1):
    max1 = max_heap.extract_max()
    max2 = max_heap.extract_max()
    cost = max1+max2
    max_cost.append(cost)
    max_heap.insert(cost)

print("Min cost:",sum(min_cost))
print("Max cost:",sum(max_cost))