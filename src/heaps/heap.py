class MinHeap:
    def __init__(self):
        self.heap: list = []
    
    def parent (self, i) -> int:
        return (i - 1) // 2
    
    def left_child_index(self, i) -> int:
        return 2 * i + 1
    
    def right_child_index(self, i) -> int:
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[j], self.heap[i] = self.heap[i], self.heap[j]
    
    def insert(self, value):
        self.heap.append(value)
        self.compare_with_parent(len(self.heap) - 1)

    def compare_with_parent(self, index):
        while index > 0:
            if self.heap[index] < self.heap [self.parent(index)]:
                self.swap(index, self.parent(index))
                index = self.parent(index)
            else:
                break
    
    def print_heap(self):
        for i in range(0,len(self.heap)):
            print(f" {self.heap[i]} ", end = " ")
        print(end="\n")
    
    def search(self, value) -> bool:
        if not self.heap:
            raise IndexError("Heap is Empty")
        for i in self.heap:
            if i == value:
                return True
        return False

    def index_of(self, value) -> int:
        if self.search(value) is True:
            for i in range(len(self.heap)):
                if self.heap[i] == value:
                    return i
        return -1
    
    def delete(self, value):
        index_of_value = self.index_of(value)
        if index_of_value == -1:
            raise IndexError("value not exsist in the heap")
        else:
            # first step swap between last value and the value want to removw then remove the value 
            last_index  = len(self.heap) - 1
            self.swap(index_of_value, last_index )
            self.heap.pop()
        if index_of_value < len(self.heap):
            self.compare_with_parent(index_of_value)
            self.compare_with_childs(index_of_value)

    def compare_with_childs(self, index):
        while True:
            smallest = index
            left = self.left_child_index(index)
            right = self.right_child_index(index)
            if len(self.heap) > left and self.heap[smallest] > self.heap[left] :
                smallest = left
            if len(self.heap) > right and self.heap[smallest] > self.heap[right] :
                smallest = right
            if smallest == index:
                break
            self.swap(index, smallest)
            index = smallest

    def peek(self):
        if not self.heap:
            raise IndexError("Heap is Empty")
        return self.heap[0]