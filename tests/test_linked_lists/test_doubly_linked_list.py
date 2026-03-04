from src.linked_lists.doubly_linked_list import DoublyLinkedList, DoublyNode

def test_double_linked_list_creation():
    node: DoublyNode = DoublyNode(10)

    assert node.value == 10
    assert node.next is None
    assert node.prev is None

    dll: DoublyLinkedList = DoublyLinkedList()
    assert dll.head is None
    assert dll.length == 0