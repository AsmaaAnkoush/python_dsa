class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.length: int = 0
    
    def push(self, data):
        '''This method pushes a new element onto the stack'''
        #Time Complexity is O(1)
        #Space complexity is o(1)
        node: Node = Node (data)
        node.next = self.top
        self.top = node
        self.length += 1
    
    def pop (self):
        '''This method pops the top element from the stack, and returns the removed value'''
        #Time Complexity is O(1)
        #Space complexity is o(1)
        if self.top == None:
            raise IndexError ("The Stack is Empty")
        else:
            poped_data = self.top.value
            self.top = self.top.next
            self.length -= 1
            return poped_data
    
    def peek(self):
        '''This method returns the value of top element in the stack without removing it from the stack'''
        #Time Complexity is O(1)
        #Space complexity is o(1)
        if self.top == None:
            raise IndexError ("The Stack is Empty")
        else:
            peeked_data = self.top.value
            return peeked_data

    def is_empty(self) -> bool:
        '''This method checks if the stack is empty or not'''
        #Time Complexity is O(1)
        #Space complexity is O(1)
        if self.top == None:
            return True
        else:
            return False

    def size(self) -> int:
        '''This method returns the size of the stack'''
        #Time Complexity is O(1)
        #Space complexity is O(1)
        return self.length

    def clear(self):
        '''This method empties the stack'''
        #Time Complexity is O(1)
        #Space complexity is o(1)
        self.length = 0
        self.top = None