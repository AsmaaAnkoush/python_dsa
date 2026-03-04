from ..linked_lists.linked_list import LinkedList

class Queue:
    def __init__(self):
        self.elments: LinkedList = LinkedList()
        self.length: int = 0
    