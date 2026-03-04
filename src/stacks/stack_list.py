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
    
    def pop(self):
        '''This method pops the top element from the stack, and returns the removed value'''
        #Time Complexity is O(1).
        #Space complexity is o(1).
        if self.elements == []:
            raise IndexError ("The Stack is Empty")
        else:
            poped_element = self.elements[-1]
            self.elements.remove(self.elements[-1])
            self.length -= 1
            return poped_element
    
    def peek(self):
        '''This method returns the value of top element in the stack without removing it from the stack'''
        #Time Complexity is O(1)
        #Space complexity is o(1)
        return self.elements[-1]

    def size(self) -> int:
        '''This method returns the size of the stack'''
        #Time Complexity is O(1)
        #Space complexity is o(1)
        return self.length

    def is_empty(self) -> bool:
        '''This method checks if the stack is empty or not'''
        #Time Complexity is O(1)
        #Space complexity is o(1)
        if self.length == 0:
            return True
        else:
            return False
    
    def clear(self):
        '''This method empties the stack'''
        #Time Complexity is O(1)
        #Space complexity is o(1)
        self.length = 0
        self.elements = []
    
    def __str__(self):
        '''This method for human-readable representation'''
        #Time Complexity is O(1)
        #Space complexity is o(1)
        string: str = ""
        for i in range(len(self.elements)-1,-1,-1):
            string = string + "^\n"
            string = string + f"{self.elements[i]}\n"
        return string