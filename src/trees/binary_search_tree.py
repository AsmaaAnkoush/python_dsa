class Node:
    def __init__(self, value):
        self.value = value
        self.rigth = None
        self.left = None
    
class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self.insert_at_true_position(self.root, value)
    
    def insert_at_true_position(self, current: Node, value):
        if value < current.value:
            # insert left 
            if current.left:
                self.insert_at_true_position(current.left, value)
            else:
                current.left = Node(value)
        else:
            # insert right
            if current.right:
                self.insert_at_true_position (current.rigth, value)
            else:
                current.rigth = Node(value)