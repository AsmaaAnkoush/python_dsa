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

def test_front():
    queue: Queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    assert queue.length == 3
    assert queue.front() == 10
    queue.dequeue()
    assert queue.length == 2
    assert queue.front() == 20

def test_size():
    queue: Queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    assert queue.size() == 3
    queue.dequeue()
    assert queue.size() == 2

def test_clear():
    queue: Queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    assert queue.size() == 3
    queue.clear()
    assert queue.size() == 0