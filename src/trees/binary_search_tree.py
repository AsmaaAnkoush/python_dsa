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
        '''This method prints tree'''
        if node:
            self.print_bst(node.right, level + 1, "R-> ")
            print("    " * level + nodeType + str(node.value))
            self.print_bst(node.left, level + 1, "L-> ")
    
    def find_minimum(self, root):
        '''This method returns the minimum value in subtree'''
        while root.left:
            root = root.left
        return root

    def remove(self, root, value):
        '''This method removes value from tree using successor logic'''
        # if the tree was ended without find the value -> return Non
        if not root:
            return root
        
        # search to the value
        if value > root.value:
            root.right = self.remove(root.right, value)
        
        elif value < root.value:
            root.left = self.remove(root.left, value)
        # find the node we want to delete it 
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                successor = self.find_minimum(root.right)
                root.value = successor.value
                root.right = self.remove(root.right, successor.value)
        return root
    
    def search(self, root, value) -> bool:
        '''This function search if specific value is exists in BST'''
        if not root:
            return False
        
        # search to the value
        if value > root.value:
            return self.search(root.right, value)
        
        elif value < root.value:
            return self.search(root.left, value)
        # find the node we want to delete it 
        else:
            return True




