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
        self.compare(len(self.heap) - 1)

    def compare(self, index):
        while index > 0:
            if self.heap[index] < self.heap [self.parent(index)]:
                self.swap(index, self.parent(index))
                index = self.parent(index)
            else:
                break