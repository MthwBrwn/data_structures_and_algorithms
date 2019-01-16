from tree_intersection import tree_intersection, BST
import pytest


def test_import():
    """quick test to assert imports
    """
    assert tree_intersection
    assert BST


def test_for_the_iterable():
    """ This tests the ability to create trees through the iterable feature of class BST
    """
    new_tree = BST([4, 5, 6])
    assert new_tree.root.val == 4
    assert new_tree.root.right.val == 5


def test_simple_bst():
    """
    """
    tree_one = BST([4, 5, 6])
    tree_two = BST([4, 5, 6])
    testrun = tree_intersection(tree_one, tree_two)
    assert 4 in testrun
