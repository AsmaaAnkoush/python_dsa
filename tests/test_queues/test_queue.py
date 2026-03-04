from src.queues.queue import Queue , Node

def test_queue_node_creation():
    node: Node = Node(10)

    assert node.value == 10
    assert node.next is None

    queue: Queue = Queue()
    assert queue.head is None
    assert queue.tail is None
    assert queue.length == 0