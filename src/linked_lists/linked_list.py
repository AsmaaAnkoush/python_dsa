class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def add_first(self, value):
        '''this method add the value to the first of linked list'''
        #Time complexity = O(1)
        #Space complexity = O(1)
        node: Node = Node(value)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def append_end(self, value):
        '''this method add the value to the end of linked list'''
        #Time complexity = O(n)
        #Space complexity = O(1)
        node: Node = Node(value)
        if self.head is None:
            self.head = node 
        else:
            current: Node = self.head
            while current.next:
                current = current.next
            current.next = node
        self.length += 1

    def insert(self, index, value):
        '''This method adds a value at a specific index in the linked list'''
        #Time complexity = O(n)
        #Space complexity = O(1)
        node: Node = Node(value)
        if self.length < index or index < 0:
            raise IndexError("Index Out Of Range")
        elif index == 0:
            node.next = self.head
            self.head = node
            self.length += 1
        else:
            current: Node = self.head
            i: int = 0 
            while i < index - 1:
                current = current.next
                i += 1
            node.next = current.next
            current.next = node
            self.length += 1

    def remove_at(self, index: int) -> int:
        '''this method removes a value at a specific index in the linked list'''
        #Time complexity = O(n)
        #Space complexity = O(1)
        removed: int
        if self.length <= index or index < 0:
            raise IndexError("Index Out Of Range")
        elif index == 0:
            removed = self.head.value
            self.head = self.head.next
            self.length -= 1
            return removed
        else:
            current: Node = self.head
            i: int = 0 
            while i < index - 1:
                prev = current
                current = current.next
                i += 1
            removed = current.next.value
            current.next = current.next.next
            self.length -= 1
            return removed
    
    def clear(self):
        '''This method empties the linked list'''
        #Time complexity = O(1)
        #Space complexity = O(1)
        self.head = None
        self.length = 0

    def contains(self, value) -> bool:
        '''this method checks if the linked list contains a specific value'''
        #Time complexity = O(n)
        #Space complexity = O(1)
        current: Node = self.head
        if self.length == 0:
            return False
        else:
            while current:
                if current.value == value:
                    return True
                current = current.next
            return False

    def index_of(self, value) -> int:
        '''this method returns the index of a specific value in the linked list, if it exists'''
        #Time complexity = O(n)
        #Space complexity = O(1)
        current: Node = self.head
        index: int = 0
        if self.length == 0:
            return -1
        else:
            while current:
                if current.value == value:
                    return index
                index += 1
                current = current.next
            return -1

    def for_each(self, action):
        '''this method applies the given action function to all values in the linked list'''
        #Time complexity = O(n)
        #Space complexity = O(1)
        current: Node = self.head
        while current:
            current.value = (action)(current.value)
            current = current.next
