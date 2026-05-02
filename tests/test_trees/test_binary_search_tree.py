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
    