import pytest
from src.queues.queue_linked_list import Queue

def test_enqueue():
    queue: Queue = Queue()
    assert queue.elments.length == 0
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    assert queue.elments.length == 3

def test_dequeue():
    queue: Queue = Queue()
    empty_queue: Queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    assert queue.elments.length == 3
    queue.dequeue()
    assert queue.elments.length == 2
    with pytest.raises(IndexError):
        empty_queue.dequeue()