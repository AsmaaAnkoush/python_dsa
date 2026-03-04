class Stack:
    def __init__(self):
        self.elements = []
        self.length = 0
    
    def push(self, data):
        '''This method pushes a new element onto the stack list'''
        #Time Complexity is O(1), o(n) if list resized
        #Space complexity is o(1),, o(n) if list resized
        self.elements.append(data)
        self.length += 1