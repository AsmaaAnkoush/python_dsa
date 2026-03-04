from src.linked_lists.linked_list import LinkedList, Node
import pytest


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

def test_append_end_and_length():
    ll = LinkedList()
    ll.append_end(10)
    ll.append_end(20)
    ll.append_end(30)

    assert ll.length == 3

def test_insert():
    ll = LinkedList()

    with pytest.raises(IndexError):
        ll.insert(5, 100)
        ll.insert(0, 5)
        assert ll.length == 1

def test_remove_at():
    ll = LinkedList()
    ll.append_end(1)
    ll.append_end(2)
    ll.append_end(3)

    removed = ll.remove_at(1)

    assert removed == 2
    assert ll.length == 2

def test_clear():
    ll = LinkedList()
    ll.append_end(1)
    ll.append_end(2)
    ll.clear()

    assert ll.length == 0
    assert ll.head is None