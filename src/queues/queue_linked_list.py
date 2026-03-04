from ..linked_lists.linked_list import LinkedList

class Queue:
    def __init__(self):
        self.elments: LinkedList = LinkedList()
        self.length: int = 0
    
    def enqueue(self, data):
        '''This method adds data to the end of queue'''
        #Time Complexity O(n)
        #Space complexity O(1)
        self.elments.append_end(data)
        self.length += 1

