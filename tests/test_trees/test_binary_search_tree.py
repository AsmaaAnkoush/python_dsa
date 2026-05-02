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
