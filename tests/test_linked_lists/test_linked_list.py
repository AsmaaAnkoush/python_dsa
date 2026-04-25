from src.linked_lists.linked_list import LinkedList, Node
import pytest

def double_func(x):
    return x * 2

def get_even(x):
    return x % 2 == 0


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

def test_contains():
    ll = LinkedList()
    ll.append_end("a")
    ll.append_end("b")

    assert ll.contains("a") is True
    assert ll.contains("z") is False

def test_index_of():
    ll = LinkedList()
    ll.append_end(5)
    ll.append_end(10)

    assert ll.index_of(10) == 1
    assert ll.index_of(999) == -1

def test_for_each():
    ll = LinkedList()
    ll.append_end(1)
    ll.append_end(2)
    ll.append_end(3)

    ll.for_each(double_func)
    assert ll.contains(6) is True
    assert ll.contains(1) is False
    assert ll.contains(2) is True

def test_map():
    ll = LinkedList()
    ll.append_end(1)
    ll.append_end(2)
    ll.append_end(3)

    new_list = ll.map(double_func)

    assert new_list.index_of(2) is 0
    assert new_list.index_of(4) is 1
    assert new_list.index_of(6) is 2

def test_where():
    ll = LinkedList()
    ll.append_end(1)
    ll.append_end(2)
    ll.append_end(3)
    ll.append_end(4)

    evens = ll.where(get_even)

    assert evens.length == 2
    assert evens.index_of(2) == 0
    assert evens.index_of(4) == 1

def test_where_at():
    ll = LinkedList()
    ll.append_end(1)
    ll.append_end(2)
    ll.append_end(3)
    ll.append_end(4)

    assert ll.where_at(0).value == 1
    assert ll.where_at(1).value == 2
    assert ll.where_at(2).value == 3
    assert ll.where_at(3).value == 4
    with pytest.raises(IndexError):
        ll.where_at(-5).value == 4

def test_str_representation():
    ll = LinkedList()
    ll.append_end(1)
    ll.append_end(2)

    assert str(ll)

def test_find_middle():
    ll = LinkedList()
    ll.append_end(1)
    ll.append_end(2)
    ll.append_end(3)
    ll.append_end(4)
    ll.append_end(5)

    assert ll.find_middle().value == 3

def test_insert_sorted():
    ll = LinkedList()
    ll.append_end(1)
    ll.append_end(2)
    ll.append_end(3)
    ll.append_end(7)
    ll.append_end(15)
    assert ll.length == 5
    ll.insert_sorted(10)
    assert ll.length == 6 
    ll.index_of(4) == 10
