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


        