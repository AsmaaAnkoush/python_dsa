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