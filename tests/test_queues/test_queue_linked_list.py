import pytest
from src.queues.queue_linked_list import Queue

def test_enqueue():
    queue: Queue = Queue()
    assert queue.length == 0
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    assert queue.length == 3