from src.trees.binary_search_tree import Node, BST

def test_insert():
    bst: BST = BST()
    bst.insert(10)
    bst.insert(20)
    bst.insert(5)
    bst.insert(0)
    assert bst.root.value == 10
    assert bst.root.right.value == 20
    assert bst.root.left.value == 5
    assert bst.root.left.left.value == 0

def test_remove():
    bst: BST = BST()
    bst.insert(10)
    bst.insert(20)
    bst.insert(5)
    bst.insert(0)
    bst.insert(7)
    bst.insert(25)
    bst.insert(18)
    bst.insert(6)

    assert bst.root.value == 10
    assert bst.root.right.value == 20
    assert bst.root.right.right.value == 25
    assert bst.root.right.left.value == 18
    assert bst.root.left.value == 5
    assert bst.root.left.right.value == 7
    assert bst.root.left.right.left.value == 6
    assert bst.root.left.left.value == 0
    bst.remove(bst.root, 5)
    assert bst.root.value == 10
    assert bst.root.right.value == 20
    assert bst.root.right.right.value == 25
    assert bst.root.right.left.value == 18
    assert bst.root.left.value == 6
    assert bst.root.left.right.value == 7
    assert bst.root.left.left.value == 0
    
def test_search():
    bst: BST = BST()
    bst.insert(10)
    bst.insert(20)
    bst.insert(5)
    bst.insert(0)
    bst.insert(7)
    bst.insert(25)
    bst.insert(18)
    bst.insert(6)

    assert bst.search(bst.root, 10) is True
    assert bst.search(bst.root, 0) is True
    assert bst.search(bst.root, 100) is False
    assert bst.search(bst.root, 18) is True
    assert bst.search(bst.root, 9) is False

def tra_fun(x):
    return x*2

def test_map_bst():
    bst: BST = BST()
    bst.insert(10)
    bst.insert(20)
    bst.insert(5)
    bst.insert(0)
    bst.insert(7)
    new_bst = bst.map_bst(bst.root, tra_fun)
    assert new_bst.root.value == 20
    assert new_bst.root.right.value == 40
    assert new_bst.root.left.value == 10
    assert new_bst.root.left.right.value == 14
    assert new_bst.root.left.left.value == 0