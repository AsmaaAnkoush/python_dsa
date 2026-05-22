from src.heaps.heap_list import MinHeap
def double_func(x):
    return x * 2

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

def test_delete():
    heap = MinHeap()
    heap.insert(34)
    heap.insert(8)
    heap.insert(12)
    heap.insert(6)
    heap.insert(9)
    heap.insert(11)
    heap.insert(1)

    heap.delete(8)
    assert heap.index_of(1) == 0
    assert heap.index_of(9) == 1
    assert heap.index_of(6) == 2
    assert heap.index_of(34) == 3
    assert heap.index_of(11) == 4
    assert heap.index_of(12) == 5
    assert heap.index_of(8) == -1

def test_for_each():
    heap = MinHeap()
    heap.insert(34)
    heap.insert(8)
    heap.insert(12)
    heap.insert(4)
    heap.for_each(double_func)
    assert heap.index_of(16) == 1
    assert heap.index_of(12) == -1
    assert heap.index_of(8) == 0