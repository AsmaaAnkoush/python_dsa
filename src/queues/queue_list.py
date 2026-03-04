class Queue:
    def __init__(self):
        self.elements = []
        self.length = 0
    
    def enqueue(self, data):
        '''This method adds data to the end of queue'''
        #Time Complexity is O(1), o(n) if list resized
        #Space complexity is o(1), o(n) if list resized
        self.elements.append(data)
        self.length += 1
    
    def dequeue(self):
        '''This method removes a node from the front of the queue'''
        #Time Complexity O(1)
        #Space complexity O(1)
        if self.elements == []:
            raise IndexError ("The Stack is Empty")
        else:
            self.elements.pop(0)
            self.length -= 1
    
    def front(self):
        '''This method returns the value of element at the head of the queue without removing it'''
        #Time Complexity O(1)
        #Space complexity O(1)
        if self.length == 0:
            raise IndexError ("The Queue is Empty")
        return self.elements[0]

    def size(self) -> int:
        '''This method returns the size of queue'''
        #Time Complexity is O(1)
        #Space complexity is o(1)
        return self.length

    def clear(self):
        '''This method empties the queue'''
        #Time Complexity is O(1)
        #Space complexity is o(1)
        self.elements = []
        self.length = 0