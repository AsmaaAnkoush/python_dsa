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
ll= LinkedList()
ll.add_first(5)
ll.append_end(30)
ll.insert(1, 15)
print(ll)

print("*" * 50)
q = Queue()
q.enqueue(10)
q.enqueue(15)
q.enqueue(20)
q.dequeue()
print(q)

print("*" * 50)
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s)
s.pop()
print(s)

print("*" * 50)
dll = DoublyLinkedList()
dll.insert_at_head(10)
dll.insert_at_tail(15)
dll.insert_at(1,12)
dll.print_forward()

print("*" * 50)
cll: CircularLinkedList = CircularLinkedList()
cll.insert(10)
cll.print_list()
print(cll.containes(10))
print(cll.size())