from src.linked_lists.linked_list import LinkedList
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

    def insert_at_true_position(self, root , value):
        if value < root.value:
            # insert left 
            if root.left:
                self.insert_at_true_position(root.left, value)
            else:
                root.left = Node(value)
        else:
            # insert right
            if root.right:
                self.insert_at_true_position (root.right, value)
            else:
                root.right = Node(value)

    def insert_bst(self, root, value):
        '''This Method inserts the node in true position of BST'''
        if not root:
            self.root = Node(value)
        else: 
            if value < root.value:
                if root.left:
                    self.insert_bst(root.left, value)
                else:
                    root.left = Node(value)
            else:
                if root.right:
                    self.insert_bst(root.right, value)
                else:
                    root.right = Node(value)
    
    def print_bst(self, root, level = 0, node_type = "Root: "):
        '''This method prints tree'''
        if root:
            self.print_bst(root.right, level + 1, "R-> ")
            print("    " * level + node_type + str(root.value))
            self.print_bst(root.left, level + 1, "L-> ")
    
    def find_minimum(self, root):
        '''This method returns the minimum value in subtree'''
        while root.left:
            root = root.left
        return root

    def remove(self, root, value) -> BST:
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
    
    def map_bst(self, root, transform_function) -> BST:
        '''This function creates a new tree of the same shape but with transformed data'''
        if root is None:
            return None

        # create new tree
        maped_tree: BST = BST()
        maped_tree.root = Node(transform_function(root.value))

        left_tree = self.map_bst(root.left, transform_function)
        if left_tree:
            maped_tree.root.left = left_tree.root

        right_tree = self.map_bst(root.right, transform_function)
        if right_tree:
            maped_tree.root.right = right_tree.root

        return maped_tree
    
    def combine_func(self, initial, value):
        return initial + value

    def fold(self, root, combine_func, initial):
        '''this function aggregate all tree values into a single result '''
        if root is None:
            return initial
        result = combine_func(initial, root.value)
        result = self.fold(root.left, combine_func, result)
        result = self.fold(root.right, combine_func, result)
        return result
    
    def filter(self, root, predicate_func, filtered_list):
        if root is None:
            return 
        if predicate_func(root.value) is True:
            filtered_list.append_end(root.value)
        self.filter(root.left, predicate_func, filtered_list)
        self.filter(root.right, predicate_func, filtered_list)

    def in_order(self, root, linked_list):
        '''this function to traverse tree (left - root - right)'''
        if root is None:
            return
        self.in_order(root.left, linked_list)
        linked_list.append_end(root.value)
        self.in_order(root.right, linked_list)
    
    def pre_order(self, root, linked_list):
        '''this function to traverse tree (root - left - right)'''
        if root is None:
            return
        linked_list.append_end(root.value)
        self.pre_order(root.left, linked_list)
        self.pre_order(root.right, linked_list)

    def post_order(self, root, linked_list):
        '''this function to traverse tree (left - right - root)'''
        if root is None:
            return
        self.post_order(root.left, linked_list)
        self.post_order(root.right, linked_list)
        linked_list.append_end(root.value)



