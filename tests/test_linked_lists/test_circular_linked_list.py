from src.linked_lists.circular_linked_list import CircularLinkedList, CircularNode

def test_circular_linked_list_creation():
    node: CircularNode = CircularNode(10)

    assert node.data == 10
    assert node.next is None

    cll:CircularLinkedList = CircularLinkedList()
    assert cll.head is None
    assert cll.length == 0

def test_insert():
    cll = CircularLinkedList()
    cll.insert(10)
    assert cll.length == 1
    cll.insert(12)
    assert cll.length == 2
    cll.insert(15)
    assert cll.length == 3

def test_delete():
    cll = CircularLinkedList()
    cll.insert(10)
    cll.insert(15)
    cll.insert(20)
    assert cll.delete(11) is False
    assert cll.delete(10) is True
    assert cll.delete(15) is True
    assert cll.length is 1

def test_containes():
    cll = CircularLinkedList()
    cll.insert(10)
    cll.insert(15)
    cll.insert(20)
    assert cll.containes(11) is False
    assert cll.containes(10) is True
    assert cll.containes(15) is True
    assert cll.containes(20) is True

