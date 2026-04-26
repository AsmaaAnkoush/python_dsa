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
        # Time Complexity = O(n)
        # Space Complexity = O(1)
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

    def delete(self, data) -> bool:
        '''This method deletes a node from the circular linked list and returns True if the deletion is successful, or False otherwise'''
        # Time Complexity = O(n)
        # Space Complexity = O(1)
        if self.head == None:
            return False
        current: CircularNode = self.head
        prev = None
        # if the the list contain one element and the data in it
        if self.head.next == self.head and self.head.data == data:
            self.head = None
            self.length -= 1
            return True
        # if the data in the head 
        if self.head.data == data:
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            self.length -= 1
            return True
        # if the data not the head 
        prev = self.head
        current = self.head.next 
        while current != self.head:
            if current.data == data:
                prev.next = current.next
                self.length -= 1
                return True
            prev = current
            current = current.next
        return False

    def containes(self, data) -> bool:
        '''This method checks whether data exists in the circular linked list'''
        # Time Complexity = O(n)
        # Space Complexity = O(1)
        if self.head == None:
            return False
        current: CircularNode = self.head
        if current.data == data:
            current = current.next
            return True
        else:
            current = current.next
        while current != self.head:
            if current.data == data:
                return True
            else:
                pass
            current = current.next
        return False
    
    def get_at(self, index):
        '''This function returns the data at the given index'''
        # Time complexity = O(n)
        # Space complexity = O(1)
        if index >= self.length or index < 0 :
            raise IndexError("Index Out Of Range")
        else:
            current:CircularNode = self.head
            for _ in range (index):
                current = current.next
            return current.data
    
    def size(self) -> int:
        '''This method returns length of circular linked list'''
        # Time complexity = O(1)
        # Space complexity = O(1)
        return self.length
    
    def print_list(self):
        '''This method for human-readable representation'''
        if self.head == None:
            return "Empty List"
        string: str = "head -> "
        current: CircularNode = self.head
        string = string + f"{current.data} -> "
        while current.next != self.head:
                current = current.next
                string = string + f"{current.data} -> "
        string = string + "head" 
        print (string)
    
    def rotate(self, k: int):
        '''this method shift starting point of cirular linked list by k'''
        # Time complexity = O(n)
        # Space complexity = O(1)
        current: CircularNode = self.head
        for _ in range(0, k):
            current = current.next
        self.head = current.next

