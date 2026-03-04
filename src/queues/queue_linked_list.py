from ..linked_lists.linked_list import LinkedList

class Queue:
    def __init__(self):
        self.elments: LinkedList = LinkedList()
    
    def enqueue(self, data):
        '''This method adds data to the end of queue'''
        #Time Complexity O(n)
        #Space complexity O(1)
        self.elments.append_end(data)
    
    def dequeue(self):
        '''This method removes a node from the front of the queue'''
        #Time Complexity O(n)
        #Space complexity O(1)
        return self.elments.remove_at(0)
    
    def front(self):
        '''This method returnes the element in the head of queue'''
        #Time Complexity O(n)
        #Space complexity O(1)
        element = self.elments.remove_at(0)
        self.elments.add_first(element)
        return element

    def size(self) -> int:
        '''This method returns the size of queue'''
        #Time Complexity is O(1)
        #Space complexity is o(1)
        return self.elments.length

    def clear(self):
        '''This method removes all element in queue'''
        #Time Complexity is O(1)
        #Space complexity is o(1)
        self.elments.clear()
