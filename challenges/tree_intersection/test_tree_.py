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


def test_simple_bst_with_three_match():
    """this uses strings to determine if there are intersecting nodes on the BSTs
    """
    tree_one = BST(['4', '5', '6'])
    tree_two = BST(['4', '5', '6'])
    testrun = tree_intersection(tree_one, tree_two)
    assert '4' in testrun
    assert '5' in testrun
    assert '6' in testrun
    assert '1' not in testrun


def test_simple_bst_with_one_match():
    """this uses strings to determine if there are intersecting nodes on the BSTs
    """
    tree_one = BST(['4', '5', '6'])
    tree_two = BST(['1', '2', '6'])
    testrun = tree_intersection(tree_one, tree_two)
    assert '6' in testrun
    assert '5' not in testrun
    assert '1' not in testrun


def test_simple_bst_with_three_match_ints():
    """this uses strings to determine if there are intersecting nodes on the BSTs
    """
    tree_one = BST([4, 5, 6])
    tree_two = BST([4, 5, 6])
    testrun = tree_intersection(tree_one, tree_two)
    assert 4 in testrun


def test_an_empty():
    """ Tihs tests an empty set while the second has values
    """
    tree_one = BST([])
    tree_two = BST([4, 5, 6])
    testrun = tree_intersection(tree_one, tree_two)
    assert testrun == []
