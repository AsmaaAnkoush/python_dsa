from src.heaps.heap import MinHeap
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