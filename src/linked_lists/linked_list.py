class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def add_first(self, value):
        '''this method add the value to the first of linked list'''
        #Time complexity = O(1)
        #Space complexity = O(1)
        node: Node = Node(value)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def append_end(self, value):
        '''this method add the value to the end of linked list'''
        #Time complexity = O(n)
        #Space complexity = O(1)
        node: Node = Node(value)
        if self.head is None:
            self.head = node 
        else:
            current: Node = self.head
            while current.next:
                current = current.next
            current.next = node
        self.length += 1