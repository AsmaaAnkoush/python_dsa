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
        # Time complexity = O(1)
        # Space complexity = O(1)
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
        # Time complexity = O(n)
        # Space complexity = O(1)
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

    def containes(self, data) -> bool:
        '''This method checks whether a value exists in the doubly linked list'''
        # Time complexity = O(n)
        # Space complexity = O(1)
        current: DoublyNode = self.head
        if self.length == 0:
            return False
        else:
            while current:
                if current.value == data:
                    return True
                current = current.next
            return False

    def get_at(self, index):
        '''This method returns the value of the given index'''
        # Time complexity = O(n)
        # Space complexity = O(1)
        if self.length <= index or index < 0:
            raise IndexError("Index Out Of Range")
        else:
            current: DoublyNode = self.head
            i: int = 0 
            while i < index :
                current = current.next
                i += 1
            else:
                return current.value

    def delete(self, value) -> bool:
        '''This method deletes a value from the doubly linked list and returns True if the deletion is successful, or False if the value is not in the list'''
        # Time complexity = O(n)
        # Space complexity = O(1)
        current: DoublyNode = self.head
        if self.length == 0:
            return False
        else:
            while current:
                if current.value == value:
                    # delete head
                    if current == self.head:
                        self.head = current.next
                        # double linked list not empty
                        if self.head:
                            self.head.prev = None
                        # double linked list empty
                        else:
                            self.tail = None
                    # delete tail
                    elif current == self.tail:
                        self.tail = current.prev
                        self.tail.next = None
                    else:
                        current.prev.next = current.next
                        current.next.prev = current.prev
                    self.length -= 1
                    return True
                current = current.next
        return False
    
    def remove_at(self, index: int):
        '''This method removes the node in specific index'''
        # Time complexity = O(n)
        # Space complexity = O(1)
        if self.length <= index or index < 0:
            raise IndexError("Index Out Of Range")
        # if DLL is contained 1 element only
        if index == 0 and self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return
        elif index == 0 and self.length > 1:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return
        else:
            current: DoublyNode = self.head
            prev: DoublyNode = None
            current_index = 0
            while current:
                if current_index == index:
                    # Remove Node
                    prev.next = current.next
                    current.prev = prev
                    self.length -= 1
                    return 
                else:
                    prev = current
                    current = current.next
                    current_index += 1

    def map(self, transform_func) -> DoublyLinkedList:
        '''this method returns a new Double Linked List with transform function applied to all values, leaving the original list unchanged'''
        # Time complexity = O(n)
        # Space complexity = O(n)
        current: DoublyNode = self.head
        new_double_linked_list: DoublyLinkedList = DoublyLinkedList()
        while current:
            new_value = (transform_func)(current.value)
            new_double_linked_list.insert_at_tail(new_value)
            current = current.next
        return new_double_linked_list

    def print_forward(self):
        '''This method prints doubly linked list from head to tail'''
        # Time complexity = O(1)
        # Space complexity = O(1)
        current: DoublyNode = self.head
        string: str = "head -> "
        while current:
            string = string + f"{current.value} -> "
            current = current.next
        string = string + "tail"
        print(string)
     
    def print_backward(self):
        '''This method prints doubly linked list from tail to head'''
        # Time complexity = O(1)
        # Space complexity = O(1)
        current: DoublyNode = self.tail
        string: str = "tail <- "
        while current:
            string = string + f"{current.value} <- "
            current = current.prev
        string = string + "head"
        print(string)