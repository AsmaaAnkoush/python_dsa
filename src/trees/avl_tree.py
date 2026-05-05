class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None
    
    def get_height(self, root) -> int:
        if not root:
            return 0
        return root.height

    def get_max(self, num1, num2) -> int:
        if num1 > num2:
            return num1 
        return num2
    
    def get_balance(self, root) -> int:
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
    
    def right_rotate(self, prev_root):
        new_root = prev_root.left
        sub_tree_to_new_root = new_root.right
        new_root.right = prev_root
        prev_root.left = sub_tree_to_new_root
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        prev_root.height = 1 + max(self.get_height(prev_root.left), self.get_height(prev_root.right))

        return new_root
    
    def left_rotate(self, prev_root):
        new_root = prev_root.right
        sub_tree_to_new_root = new_root.left
        new_root.left = prev_root
        prev_root.right = sub_tree_to_new_root
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        prev_root.height = 1 + max(self.get_height(prev_root.left), self.get_height(prev_root.right))

        return new_root

    def insert(self, root, value):
        '''this function inserts the value in AVL tree'''
        if not root:
            return Node(value)

        if value < root.value:
            root.left = self.insert(root.left, value)
        elif value > root.value:
            root.right = self.insert(root.right, value)
        else:
            return root
        # update height
        root.height = 1 + self.get_max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # LL
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # LR
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RR
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # RL
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
    
    def print_avl(self, root, level = 0, node_type = "Root: "):
        '''This method prints tree'''
        if root:
            self.print_avl(root.right, level + 1, "R-> ")
            print("    " * level + node_type + str(root.value))
            self.print_avl(root.left, level + 1, "L-> ")
        




