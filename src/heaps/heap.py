class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class MinHeap:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return
        self.insert_node(self.root, node)
        self.compare_with_parent(node)
        
    def insert_node(self, current, node):
        if current.left is None:
            current.left = node
            node.parent = current
            return
        if current.right is None:
            current.right = node
            node.parent = current
            return
        self.insert_node(current.left, node)

    def compare_with_parent(self, node):
        while node.parent and node.parent.value > node.value:
            # swap
            node.value, node.parent.value = (node.parent.value, node.value)
            node = node.parent

    def print_heap(self, root, level = 0, node_type = "Root: "):
        if root:
            self.print_heap(root.right, level + 1, "R-> ")
            print("    " * level + node_type + str(root.value))
            self.print_heap(root.left, level + 1, "L-> ")
    
    def search(self, root, value) -> bool:
        if root is None:
            return False
        if root.value == value:
                return True
        return(self.search(root.left, value) or self.search(root.right, value))

    def index_of(self, root, value, index = 0) -> int:
        if root is None:
            return -1
        if root.value == value:
            return index
        left_result = self.index_of(root.left, value, (2*index+1))
        if left_result != -1:
            return left_result
        right_result = self.index_of(root.right, value, (2*index+2))
        if right_result != -1:
            return right_result
        return -1