from ..linked_lists.linked_list import LinkedList
from ..queues.queue import Queue
from ..linked_lists.doubly_linked_list import DoublyLinkedList
from ..stacks.stack import Stack
from ..linked_lists.circular_linked_list import CircularLinkedList
from ..trees.binary_search_tree import BST
from ..trees.avl_tree import AVL
from ..heaps.heap import MinHeap


# to run the code 
'''
go to this E:\work\python\02_projects\python_dsa
then run -> python -m python_dsa.src.utils.sample
'''
print("Linked List")
ll= LinkedList()
ll.append_end(1)
ll.append_end(2)
ll.append_end(3)
ll.append_end(7)
ll.append_end(15)
ll.insert_sorted(20)
print(ll)

print("*" * 50)
print("Queue")
q = Queue()
q.enqueue(10)
q.enqueue(15)
q.enqueue(20)
q.dequeue()
print(q)

print("*" * 50)
print("Stack")
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s)
s.pop()
print(s)

print("*" * 50)
print("Double Linked List")
dll = DoublyLinkedList()
dll.insert_at_head(10)
dll.remove_at(0)
dll.print_forward()
dll.insert_at_tail(15)
dll.insert_at(1,12)
dll.print_forward()
dll.insert_at_tail(20)
dll.insert_at_tail(40)
dll.insert_at_tail(60)
dll.insert_at_tail(80)
print("DLL")
dll.print_forward()
first_dll, second_dll = dll.split_at(5)
print("First DLL")
first_dll.print_forward()
print("Second DLL")
second_dll.print_forward()

print("*" * 50)
print("Circular Linked List")
cll: CircularLinkedList = CircularLinkedList()
cll.insert(10)
cll.insert(20)
cll.insert(30)
cll.insert(40)
cll.insert(50)
cll.print_list()
print(cll.containes(10))
print(cll.size())
cll.rotate(2)
cll.print_list()
cll2: CircularLinkedList = CircularLinkedList()
cll2.insert(15)
cll2.insert(25)
cll.insert(cll2)
cll.print_list()
cll.flatten()
cll.insert(60)
cll.print_list()



def tra_fun(x):
    return x*2

def combine_func(initial, value):
        return initial + value

def is_even(value):
      return value % 2 == 0

print("*" * 50)
print("Binary Search Tree")
bst: BST = BST()
bst.insert(10)
bst.insert(20)
bst.insert(5)
bst.insert(7)
bst.insert(25)
bst.insert(18)
bst.insert(6)


bst.print_bst(bst.root)
bst.remove(bst.root, 5)
print("-" * 50)
bst.print_bst(bst.root)
print(bst.search(bst.root, 30))
print(bst.search(bst.root, 0))
print(bst.search(bst.root, 5))
new_bst = bst.map_bst(bst.root, tra_fun)
# new_bst.print_bst(new_bst.root)
bst.print_bst(bst.root)
print(bst.fold(bst.root, combine_func, 0))
linked_list: LinkedList = LinkedList()
bst.in_order(bst.root, linked_list)
print(linked_list)
pre_order_list: LinkedList = LinkedList()
bst.pre_order(bst.root, pre_order_list)
print(pre_order_list)
bst.print_bst(bst.root)
print (f"the height of tree is {bst.get_height(bst.root)}")

filtered_list: LinkedList = LinkedList() 
bst.filter(bst.root, is_even, filtered_list)
print(filtered_list)

print("**" * 50)

avl = AVL()
print("AVL TREE")

avl.root = avl.insert(avl.root, 10)
avl.print_avl(avl.root)
print("-" * 50)

avl.root = avl.insert(avl.root, 20)
avl.print_avl(avl.root)
print("-" * 50)

avl.root = avl.insert(avl.root, 30)
avl.print_avl(avl.root)
print("-" * 50)

avl.root = avl.insert(avl.root, 40)
avl.print_avl(avl.root)
print("-" * 50)

avl.root = avl.insert(avl.root, 12)
avl.print_avl(avl.root)
print("-" * 50)
avl.root = avl.insert(avl.root, 25)
avl.print_avl(avl.root)
print("-" * 50)

avl.root = avl.remove(avl.root, 30)
avl.print_avl(avl.root)
print("-" * 50)
avl.root = avl.remove(avl.root, 10)
avl.print_avl(avl.root)
print("-" * 50)

print(avl.get_height(avl.root))

print("**" * 50)
print("HEAP")
# heap = MinHeap()
# heap.insert(34)
# heap.print_heap()
# heap.insert(8)
# heap.print_heap()
# heap.insert(12)
# heap.print_heap()
# heap2 = MinHeap()
# heap2.insert(34)
# heap2.print_heap()
# heap2.insert(8)
# heap2.print_heap()
# heap2.insert(12)
# heap2.print_heap()
# heap2.insert(6)
# heap2.print_heap()
# heap2.insert(9)
# heap2.print_heap()
# heap2.insert(11)
# heap2.print_heap()
# heap2.insert(1)
# heap2.print_heap()

# heap2.delete(1)
# heap2.print_heap()

# print("**" * 50)
# print("HEAP From Scratch")
# heap = MinHeap()
# heap.insert(34)
# heap.insert(8)
# heap.insert(12)
# heap.insert(6)
# heap.insert(9)
# heap.print_heap(heap.root)
# print("-" * 50)
heap2 = MinHeap()
heap2.insert(34)
heap2.print_heap(heap2.root)
print("-" * 20)

heap2.insert(8)
heap2.print_heap(heap2.root)
print("-" * 20)

heap2.insert(12)
heap2.print_heap(heap2.root)
print("-" * 20)

heap2.insert(6)
heap2.print_heap(heap2.root)
print("-" * 20)

heap2.insert(9)
heap2.print_heap(heap2.root)
print("-" * 20)

heap2.insert(11)
heap2.print_heap(heap2.root)
print("-" * 20)

heap2.insert(1)
heap2.print_heap(heap2.root)
print("-" * 20)

heap2.print_heap(heap2.root)
print("-" * 20)

heap2.print_heap(heap2.root)
heap2.delete(1)
print("-" * 50)
heap2.print_heap(heap2.root)



