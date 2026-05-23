class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class MinHeap:
    def __init__(self):
        self.root = None

    def insert(self, value) -> MinHeap:
        '''This function will fill the tree level by level and then make sure that the condition of heap'''
        node: Node = Node(value)
        if self.root is None:
            self.root = node
            return
        self.insert_node(self.root, node)
        self.compare_with_parent(node)
        
    def insert_node(self, current: Node, node: Node):
        '''This function finds the correct position to insert the node'''
        if current.left is None:
            current.left = node
            node.parent = current
            return
        if current.right is None:
            current.right = node
            node.parent = current
            return
        
        if self.get_height_min(current.left) == self.get_height_min(current.right) or (current.left.left == None or current.left.right == None ):
            self.insert_node(current.left, node)
        else:
            self.insert_node(current.right, node)

    def compare_with_parent(self, node: Node):
        '''This function used after insert the node , must check the condition of min heap(minimum is parent)'''
        while node.parent and node.parent.value > node.value:
            # swap
            node.value, node.parent.value = (node.parent.value, node.value)
            node = node.parent

    def print_heap(self, root: Node, level = 0, node_type = "Root: "):
        '''This method for human-readable representation'''
        if root:
            self.print_heap(root.right, level + 1, "R-> ")
            print("    " * level + node_type + str(root.value))
            self.print_heap(root.left, level + 1, "L-> ")
    
    def search(self, root, value) -> bool:
        '''This function checks if value exist in heap'''
        if root is None:
            return False
        if root.value == value:
                return True
        return(self.search(root.left, value) or self.search(root.right, value))

    def index_of(self, root: Node, value, index = 0) -> int:
        '''This function returns the index of the value in heap'''
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
    
    def find_node(self, root: Node, value):
        '''This function returns the full node that have the given value'''
        if root is None:
            return None
        if root.value == value:
            return root
        left_result = self.find_node(root.left, value)
        if left_result:
            return left_result
        right_result = self.find_node(root.right, value)
        if right_result:
            return right_result
    
    def get_height(self, root: Node) -> int:
        '''This function returns the height of the heap(tree)'''
        if root is None:
            return 0
        return 1 + max(self.get_height(root.left), self.get_height(root.right))
    
    def get_height_min(self, root: Node) -> int:
        if root is None:
            return 0
        return 1 + min(self.get_height(root.left), self.get_height(root.right))

    def find_last_node(self, root: Node):
        '''This function returns the last node in the heap'''
        if root is None:
            return None
        last_node = root
        if root.right and self.get_height(root.right) >= self.get_height(root.left):
            last_node = self.find_last_node(root.right)
        elif root.left:
            last_node = self.find_last_node(root.left)
        return last_node
    
    def delete(self, value) -> MinHeap:
        '''This function deletes the value from the heap'''
        target_node = self.find_node(self.root, value)
        if target_node is None:
            print("Value not found")
            return
        last_node = self.find_last_node(self.root)
        print(f"the Last Node is {last_node.value}")
        target_node.value = last_node.value

        last_node_parent = last_node.parent
        if last_node_parent:
            if last_node_parent.left == last_node.value:
                last_node_parent.left = None
            elif last_node_parent.right == last_node.value:
                last_node_parent.right = None
        self.compare_with_parent(target_node)
        self.compare_with_childs(target_node)

    def compare_with_childs(self, node: Node):
        while node:
            smallest = node
            if node.left and node.left.value < smallest.value:
                smallest = node.left
            if node.right and node.right.value < smallest.value:
                smallest = node.right
            if smallest == node:
                break
            node.value, smallest.value = (smallest.value, node.value)
            node = smallest
    
    def for_each(self, root: Node, action):
        '''This function applies the action to the element of the heap'''
        if root:
            root.value = (action(root.value))
            self.for_each(root.right, action)
            self.for_each(root.left, action)
    
    def convert_array_to_heap(self, array: list) ->MinHeap:
        '''This function converts list to heap'''
        heap: MinHeap = MinHeap()
        for i in array:
            heap.insert(i)
        return heap
            
