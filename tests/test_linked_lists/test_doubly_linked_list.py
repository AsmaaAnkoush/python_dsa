from src.linked_lists.doubly_linked_list import DoublyLinkedList, DoublyNode

def test_double_linked_list_creation():
    node: DoublyNode = DoublyNode(10)

    assert node.value == 10
    assert node.next is None
    assert node.prev is None

    dll: DoublyLinkedList = DoublyLinkedList()
    assert dll.head is None
    assert dll.length == 0

def test_insert_at_head():
    dll: DoublyLinkedList = DoublyLinkedList()
    dll.insert_at_head(10)
    dll.insert_at_head(5)

    assert dll.head.value is 5
    assert dll.length == 2

def test_insert_at_tail():
    dll: DoublyLinkedList = DoublyLinkedList()
    dll.insert_at_head(10)
    dll.insert_at_head(5)
    assert dll.tail.value is 10
    dll.insert_at_tail(20)
    assert dll.tail.value is 20
    assert dll.length == 3

def test_insert_at():
    dll: DoublyLinkedList = DoublyLinkedList()
    dll.insert_at_head(10)
    dll.insert_at_head(5)
    assert dll.tail.value is 10
    assert dll.head.value is 5
    assert dll.length == 2
    dll.insert_at(0, 2)
    assert dll.tail.value is 10
    assert dll.head.value is 2
    assert dll.length == 3
    dll.insert_at(3, 20)
    assert dll.tail.value is 20
    assert dll.head.value is 2
    assert dll.length == 4
    dll.insert_at(2, 15)
    assert dll.tail.value is 20
    assert dll.head.value is 2
    assert dll.length == 5

def test_containes():
    dll: DoublyLinkedList = DoublyLinkedList()
    dll.insert_at_head(10)
    dll.insert_at_head(5)
    assert dll.containes(5) is True
    assert dll.containes(15) is False
    dll.insert_at(2, 15)
    assert dll.containes(15) is True

def test_get_at():
    dll: DoublyLinkedList = DoublyLinkedList()
    dll.insert_at_head(10)
    dll.insert_at_head(5)
    assert dll.get_at(1) is 10
    dll.insert_at(1, 15)
    assert dll.get_at(1) is 15

def test_delete():
    dll: DoublyLinkedList = DoublyLinkedList()
    dll.insert_at_head(10)
    dll.insert_at_head(5)
    dll.insert_at_tail(20)
    assert dll.delete(20) is True
    assert dll.delete(50) is False