from src.trees.avl_tree import AVL

def test_insert_avl():
    avl = AVL()
    avl.root = avl.insert(avl.root, 10)
    avl.root = avl.insert(avl.root, 20)
    avl.root = avl.insert(avl.root, 30)
    avl.root = avl.insert(avl.root, 40)
    avl.root = avl.insert(avl.root, 12)
    assert avl.root.value == 20 
    assert avl.root.right.value == 30
    assert avl.root.left.value == 10
    assert avl.root.right.right.value == 40 
    assert avl.root.left.right.value == 12

def test_remove_avl():
    avl = AVL()
    avl.root = avl.insert(avl.root, 10)
    avl.root = avl.insert(avl.root, 20)
    avl.root = avl.insert(avl.root, 30)
    avl.root = avl.insert(avl.root, 40)
    avl.root = avl.insert(avl.root, 12)
    avl.root = avl.insert(avl.root, 25)

    avl.root = avl.remove(avl.root, 30)
    avl.root = avl.remove(avl.root, 10)
    assert avl.root.value == 20 
    assert avl.root.right.value == 40
    assert avl.root.left.value == 12
    assert avl.root.right.left.value == 25

def test_search_avl():
    avl: AVL = AVL()
    avl.root = avl.insert(avl.root, 10)
    avl.root = avl.insert(avl.root, 20)
    avl.root = avl.insert(avl.root, 30)
    avl.root = avl.insert(avl.root, 40)
    avl.root = avl.insert(avl.root, 12)
    avl.root = avl.insert(avl.root, 25)
    
    assert avl.search(avl.root, 10) is True
    assert avl.search(avl.root, 20) is True
    assert avl.search(avl.root, 50) is False
    assert avl.search(avl.root, 25) is True
    assert avl.search(avl.root, 100) is False

def combine_func(initial, value):
        return initial + value

def test_fold_avl():
    avl: AVL = AVL()
    avl.root = avl.insert(avl.root, 10)
    avl.root = avl.insert(avl.root, 20)
    avl.root = avl.insert(avl.root, 30)
    avl.root = avl.insert(avl.root, 40)
    avl.root = avl.insert(avl.root, 12)
    avl.root = avl.insert(avl.root, 25)
    assert avl.fold_avl(avl.root, combine_func, 0) == 137

