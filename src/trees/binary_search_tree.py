class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
    
class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        '''This Method inserts the node in true position of BST'''
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
                self.insert_at_true_position (current.right, value)
            else:
                current.right = Node(value)
    
    def print_bst(self, node, level = 0, nodeType = "Root: "):
        '''this method prints tree'''
        if node:
            self.print_bst(node.right, level + 1, "-> ")
            print("    " * level + nodeType + str(node.value))
            self.print_bst(node.left, level + 1, "-> ")
