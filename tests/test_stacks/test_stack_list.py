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

def test_peek():
    stack: Stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    top_element = stack.peek()

    assert top_element == 30
    assert stack.length == 3

def test_size():
    stack: Stack = Stack()
    empty_stack: Stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    assert stack.size() == 3
    assert empty_stack.size() == 0

def test_is_empty():
    stack: Stack = Stack()
    empty_stack: Stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    assert stack.is_empty() is False
    assert empty_stack.is_empty() is True

def test_clear():
    stack: Stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    assert stack.size() == 3
    stack.clear()
    assert stack.size() == 0