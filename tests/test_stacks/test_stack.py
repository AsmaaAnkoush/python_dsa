import pytest
from src.stacks.stack import Stack , Node

def test_stack_and_node_creation():
    node: Node = Node(10)

    assert node.value == 10
    assert node.next is None

    stack: Stack = Stack()
    assert stack.top is None
    assert stack.length == 0

def test_push():
    stack: Stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    assert stack.length == 3
    assert stack.top.value == 30

def test_pop():
    stack: Stack = Stack()
    empty_satck: Stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)
    poped_element = stack.pop()
    assert poped_element == 30
    assert stack.length == 2

    with pytest.raises(IndexError):
        poped_element = empty_satck.pop()