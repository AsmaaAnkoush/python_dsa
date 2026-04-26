from ..linked_lists.linked_list import LinkedList
from ..queues.queue import Queue
from ..linked_lists.doubly_linked_list import DoublyLinkedList
from ..stacks.stack import Stack
from ..linked_lists.circular_linked_list import CircularLinkedList


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
