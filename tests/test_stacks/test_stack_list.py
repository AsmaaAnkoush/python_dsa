import pytest
from src.stacks.stack_list import Stack

def test_push():
    stack: Stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    assert stack.length == 3

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