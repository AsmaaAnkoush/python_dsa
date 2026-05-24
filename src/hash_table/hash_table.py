from typing import Optional
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = Optional[Node] = None
    
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size()
        self.load_factore_threshold = 0.75
        self.array = [None] * capacity