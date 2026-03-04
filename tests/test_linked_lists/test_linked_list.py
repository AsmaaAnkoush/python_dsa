from src.linked_lists.linked_list import LinkedList, Node

def test_linked_test_creation():
    node: Node = Node(10)

    assert node.value == 10
    assert node.next is None

    ll:LinkedList = LinkedList()
    assert ll.head is None
    assert ll.length == 0

def test_add_first_and_length():
    ll = LinkedList()
    ll.add_first(10)
    ll.add_first(20)
    ll.add_first(30)

    assert ll.length == 3