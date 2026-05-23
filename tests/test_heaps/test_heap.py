from src.heaps.heap import MinHeap
from src.heaps.heap import Node

def test_insert():
    heap = MinHeap()
    heap.insert(34)
    heap.insert(8)
    heap.insert(12)
    heap.insert(6)
    heap.insert(9)
    assert heap.root.value == 6
    assert heap.root.left.value == 8
    assert heap.root.right.value == 12
    assert heap.root.left.left.value == 34
    assert heap.root.left.right.value == 9

def test_search():
    heap = MinHeap()
    heap.insert(34)
    heap.insert(8)
    heap.insert(12)
    heap.insert(6)
    heap.insert(9)

    assert heap.search(heap.root, 8) is True
    assert heap.search(heap.root, 12) is True
    assert heap.search(heap.root, 10) is False

def test_index_of():
    heap = MinHeap()
    heap.insert(34)
    heap.insert(8)
    heap.insert(12)
    heap.insert(6)
    heap.insert(9)

    assert heap.index_of(heap.root, 6) == 0
    assert heap.index_of(heap.root, 8) == 1
    assert heap.index_of(heap.root, 12) == 2
    assert heap.index_of(heap.root, 34) == 3
    assert heap.index_of(heap.root, 9) == 4

def test_find_node():
    heap = MinHeap()
    heap.insert(34)
    heap.insert(8)
    heap.insert(12)
    heap.insert(6)
    heap.insert(9)

    heap.find_node(heap.root, 34) == Node(34)
    heap.find_node(heap.root, 8).left.value == 9

def test_last_node():
    heap = MinHeap()
    heap.insert(34)
    heap.insert(8)
    heap.insert(12)
    heap.insert(6)
    heap.insert(9)

    assert heap.find_last_node(heap.root).value == 34

