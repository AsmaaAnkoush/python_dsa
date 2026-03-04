class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, data):
        '''This method inserts a value at the end of the circular linked list'''
        #Time Complexity = O(n)
        #Space Complexity = O(1)
        node: CircularNode = CircularNode(data)

        if self.head == None:
            self.head = node
            node.next = self.head
            self.length += 1
        else:
            current: CircularNode = self.head
            while current.next != self.head:
                current = current.next
            current.next = node
            node.next = self.head
            self.length += 1