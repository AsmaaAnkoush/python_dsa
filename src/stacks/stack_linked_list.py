from ..linked_lists.linked_list import LinkedList

class Stack:
    def __init__(self):
        self.elments: LinkedList = LinkedList()
    
    def push(self, data):
        '''This method pushes a new element onto the stack'''
        #Time Complexity is O(n)
        #Space complexity is o(1)
        self.elments.append_end(data)