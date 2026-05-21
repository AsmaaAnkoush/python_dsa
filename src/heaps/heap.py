class MinHeap:
    def __init__(self):
        self.heap: list = []
    
    def parent (self, i) -> int:
        return (i - 1) // 2
    
    def left_child(self, i) -> int:
        return 2 * i + 1
    
    def right_child(self, i) -> int:
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
