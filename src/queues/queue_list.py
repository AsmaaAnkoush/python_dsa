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