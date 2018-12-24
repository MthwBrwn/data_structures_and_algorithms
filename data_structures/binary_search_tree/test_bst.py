from .bst import Node
from .bst import BST
import pytest


# @pytest fixture


def test_for_imports():
    """this tests that imports work
    """
    assert BST


def test_for_None_node():
    """ Initial test to show that Starting node is none
    """
    new_node = Node("2")
    assert new_node.right is None
    assert new_node.left is None


def test_for_none_BST():
    """This checks the staring state of the object make form class BST
    """
    new_tree = BST()
    assert new_tree.root is None
    new_tree.insert_node(3)
    assert new_tree.root.val == 3


def test_insert_for_node():
    """This tests the ability to insert a node is the BST
    """
    new_tree = BST([2])
    new_tree.insert_node(3)
    assert new_tree.root.val == 2
    assert new_tree.root.right.val == 3
    assert new_tree.root.left is None
    new_tree.insert_node(4)
    assert new_tree.root.right.right.val == 4


def test_for_the_iterable():
    """ This tests the ability to create trees through the iterable feature of class BST
    """
    new_tree = BST([4, 5, 6])
    assert new_tree.root.val == 4
    assert new_tree.root.right.val == 5


# def test_for_error_exception():
#     """ This check to see if passing a not list item causes exception
#     """
#     new_tree = BST():

def test_for_left_left():
    """  This tests for the placement of a new node
    to the left of the root and confirms the right is None
    """
    new_tree = BST([6, 5, 4])
    assert new_tree.root.val == 6
    assert new_tree.root.left.val == 5
    assert new_tree.root.left.left.val == 4
    assert new_tree.root.right is None

# def test_in_order():
#     """
#     """
#     new_tree = BST([5, 1, 7])
#     assert new_tree.pre_order() == "1 5 7"


def test_maximum_value():
    """The tests the function of the find max method against known values
    """
    new_tree = BST([4, 5, 6])
    assert new_tree.root.val == 4
    assert new_tree.find_maximum_value() == 6


def test_find_maximum_val_empty():
    """This tests that a BST with no nodes will return as none
    """
    new_tree = BST()
    assert new_tree.find_maximum_value() is None


def test_find_maximum_val_empty_add1():
    """This test determines if the none value will return as a value after an insert
    """
    new_tree = BST()
    new_tree.insert_node(1)
    assert new_tree.find_maximum_value() == 1


def test pre_order()
