from ..linked_lists.linked_list import LinkedList

class Stack:
    def __init__(self):
        self.elments: LinkedList = LinkedList()
    
    def push(self, data):
        '''This method pushes a new element onto the stack'''
        #Time Complexity is O(n)
        #Space complexity is o(1)
        self.elments.append_end(data)
    
    def pop(self):
        '''This method pops the top element from the stack, and returns the removed value'''
        #Time Complexity is O(n).
        #Space complexity is o(1).
        return self.elments.remove_at(self.elments.length-1)
    
    def peek(self):
        '''This method returns the value of top element in the stack without removing it from the stack'''
        #Time Complexity is O(n)
        #Space complexity is o(1)
        element = self.elments.remove_at(self.elments.length-1)
        self.elments.append_end(element)
        return element