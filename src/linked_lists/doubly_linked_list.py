class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def insert_at_head(self,data):
        '''This method adds a value to the beginning of the doubly linked list'''
        #Time complexity = O(1)
        #Space complexity = O(1)
        node: DoublyNode = DoublyNode(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1
    
    def insert_at_tail(self, data):
        '''this method adds the value to the end of doubly linked list'''
        #Time complexity = O(1)
        #Space complexity = O(1)
        node: DoublyNode = DoublyNode(data)
        if self.head is None:
            self.head = node 
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

    def insert_at(self, index, data):
        '''This method adds a value at a specific index in the doubly linked list'''
        #Time complexity = O(n)
        #Space complexity = O(1)
        node: DoublyNode = DoublyNode(data)
        if self.length < index or index < 0:
            raise IndexError("Index Out Of Range")
        elif index == 0:
            self.insert_at_head(data)
        elif index == self.length:
            self.insert_at_tail(data)
        else:
            current: DoublyNode = self.head
            i: int = 0 
            while i < index - 1:
                current = current.next
                i += 1
            node.next = current.next
            current.next = node
            self.length += 1