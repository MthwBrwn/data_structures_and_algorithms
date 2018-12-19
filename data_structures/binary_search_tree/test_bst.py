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


def test_for_the_iteratble():
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
