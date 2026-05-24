from typing import Optional

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next: Optional["Node"] = None
    
class HashTable:
    def __init__(self, capacity = 16):
        self.capacity = capacity
        self.size = 0
        self.load_factore_threshold = 0.75
        self.array = [None] * capacity

    def put (self, key, value):
        '''This function will insert key, value to hash table'''
        index_of_key = self.hash_key(key)
        # if the key already exists
        current: Node = self.array[index_of_key]
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next
        
        # insert node and treat with collision using separate chaining
        if self.array[index_of_key] is None:
            new_node: Node = Node(key, value)
            self.array[index_of_key] = new_node
            self.size += 1
        else:
            new_node: Node = Node(key, value)
            new_node.next = self.array[index_of_key]
            self.array[index_of_key] = new_node
            self.size += 1
        
        # check if resize_nedded
        if self.size / self.capacity > self.load_factore_threshold:
            self.resize()

    def hash_key(self, key) -> int:
        '''This function returns the index that the key should insert in it'''
        return hash(key) % self.capacity
    
    def resize(self):
        '''This function resize the hash table if the size/capacity exceed the load factore thresold'''
        old_array = self.array
        self.capacity *= 2
        self.array = [None] * self.capacity
        old_size = self.size
        self.size = 0

        for i in old_array:
            current: Node = i
            while current:
                self.put(current.key, current.value)
                current = current.next
        print(f"the old size {old_size} and the new size {self.size} and must be equals")
    
    def get(self, key):
        '''This method return the value of the given key'''
        key_index = self.hash_key(key)
        current = self.array[key_index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return "key not found"

    def remove(self, key):
        '''This method will romove the key and its value from the hashTable'''
        key_index = self.hash_key(key)
        current = self.array[key_index]
        prev = None
        while current:
            if current.key == key:
                if prev == None:
                    # just one key -> value in this index
                    self.array[key_index] = None
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next
        return "key not found"

    def search(self, key) -> bool:
        '''This function return if the key exsists in hashTable'''
        key_index = self.hash_key(key)
        current = self.array[key_index]
        while current:
            if current.key == key:
                return True
            current = current.next
        return False
    
    def keys(self) -> list:
        '''This function returns all keys in Hash Table'''
        result: list = []
        for i in self.array:
            current = i
            while current:
                result.append(current.key)
                current = current.next
        return result

