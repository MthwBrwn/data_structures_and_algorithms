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


def test_insert_for_node():
    """This tests the ability to insert a node is the BST
    """
    new_tree = BST([2])
    new_tree.insert_node(3)
    assert new_tree.root.val == 2
    # assert new_tree.root.right.val == 3
