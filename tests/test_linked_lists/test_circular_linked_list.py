from src.linked_lists.circular_linked_list import CircularLinkedList, CircularNode

def test_circular_linked_list_creation():
    node: CircularNode = CircularNode(10)

    assert node.data == 10
    assert node.next is None

    cll:CircularLinkedList = CircularLinkedList()
    assert cll.head is None
    assert cll.length == 0