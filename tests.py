from main import AVLTree


def test_insert_int():
    tree = AVLTree()
    tree.insert(3)
    tree.insert(1)
    tree.insert(5)
    assert tree.height() is 2

    tree.insert(7)
    assert tree.height() is 3

    tree.insert(3)
    assert tree.height() is 3


def test_insert_str():
    tree = AVLTree()
    tree.insert("clang")
    tree.insert("gcc")
    tree.insert("icc")
    assert tree.height() is 2

    tree.insert("g++")
    assert tree.height() is 3

    tree.insert("clang")
    assert tree.height() is 3


def test_contains():
    tree = AVLTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(5)

    assert 2 in tree
    assert 19 not in tree


def test_height():
    tree = AVLTree()
    assert tree.height() is 0

    tree.insert("yo")
    assert tree.height() is 1


def test_rebalance():
    tree = AVLTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)

    assert tree.height() is 3