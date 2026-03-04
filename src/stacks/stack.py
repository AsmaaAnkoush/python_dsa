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