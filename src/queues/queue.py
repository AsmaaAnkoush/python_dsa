class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length: int = 0
    
    def enqueue(self, data):
        '''This method adds data to the end of queue'''
        #Time Complexity O(1)
        #Space complexity O(1)
        node: Node = Node(data)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def dequeue(self):
        '''This method removes a node from the front of the queue'''
        #Time Complexity O(1)
        #Space complexity O(1)
        if self.head == None:
            raise IndexError ("The Queue is Empty")
        else:
            self.head = self.head.next
            self.length -= 1
        if self.head is None:
            self.tail = None

    def front(self):
        '''This method returns the value of element at the head of the queue without removing it'''
        #Time Complexity O(1)
        #Space complexity O(1)
        if self.head == None:
            raise IndexError ("The Queue is Empty")
        return self.head.value
    
    def size(self) -> int:
        '''This method returns the size of queue'''
        #Time Complexity is O(1)
        #Space complexity is o(1)
        return self.length

    def clear(self):
        '''This method empties the queue'''
        #Time Complexity is O(1)
        #Space complexity is o(1)
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        '''This method for human-readable representation'''
        #Time Complexity O(n)
        #Space complexity O(1)
        current_head = self.head
        string: str = "head "
        while current_head:
            string = string + " -> "
            string = string + f"{current_head.value}"
            current_head = current_head.next
        string = string + " <- tail"
        return string