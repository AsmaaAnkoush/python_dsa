from src.queues.queue import Queue , Node
import pytest

def test_queue_node_creation():
    node: Node = Node(10)

    assert node.value == 10
    assert node.next is None

    queue: Queue = Queue()
    assert queue.head is None
    assert queue.tail is None
    assert queue.length == 0

def test_enqueue():
    queue: Queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    assert queue.head.value == 10
    assert queue.tail.value == 30
    assert queue.length == 3

def test_dequeue():
    queue: Queue = Queue()
    empty_queue: Queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    assert queue.length == 3
    queue.dequeue()
    assert queue.length == 2
    with pytest.raises(IndexError):
        empty_queue.dequeue()