from src.heaps.heap import MinHeap

def test_insert():
    heap = MinHeap()
    heap.insert(34)
    heap.insert(8)
    heap.insert(12)
    heap.insert(4)

    assert heap.heap[0] == 4
    assert heap.heap[1] == 8
    assert heap.heap[2] == 12
    assert heap.heap[3] == 34

def test_search():
    heap = MinHeap()
    heap.insert(34)
    heap.insert(8)
    heap.insert(12)
    heap.insert(4)

    assert heap.search(12) is True
    assert heap.search(10) is False

def test_index_of():
    heap = MinHeap()
    heap.insert(34)
    heap.insert(8)
    heap.insert(12)
    heap.insert(4)

    assert heap.index_of(8) == 1
    assert heap.index_of(10) == -1
    assert heap.index_of(4) == 0