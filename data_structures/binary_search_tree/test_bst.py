from .bst import Node, BST, fizz_buzz
import pytest
import sys


@pytest.fixture
def starter_tree():
    """

           10
        8      12
      4
    """
    return BST([10, 8, 12, 6])


@pytest.fixture
def empty_tree():
    """
    This BST is empty and tests that methods still work at edges
    """
    return BST([])


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


def test_in_order():
    """ This tests the in_ order method with a known set of numbers
    """
    new_tree = BST([5, 1, 7, 10])
    report = ''

    def operation(node):
        nonlocal report
        report += str(node.val) + " "
    new_tree.in_order(operation)
    assert report == "1 5 7 10 "


def test_in_order_zero(empty_tree):
    """ This tests to see if the method works with an empty tree
    """
    report = ''

    def operation(node):
        nonlocal report
        report += str(node.val) + " "
    empty_tree.in_order(operation)
    assert report == ""


def test_in_order_negatives():
    """ This tests to see if the method works with a tree made of negtives
    """
    new_tree = BST([-5, -1, -7, -10])
    report = ''

    def operation(node):
        nonlocal report
        report += str(node.val) + " "
    new_tree.in_order(operation)
    assert report == "-10 -7 -5 -1 "


def test_pre_order():
    """ This tests the pre_ order method with a known set of numbers
    """
    new_tree = BST([5, 1, 7, 10])
    report = ''

    def operation(node):
        nonlocal report
        report += str(node.val) + " "

    new_tree.pre_order(operation)
    assert report == "5 1 7 10 "


def test_pre_order_zero(empty_tree):
    """ This tests the pre_ order method with an empty tree
    """
    new_tree = BST([])
    report = ''

    def operation(node):
        nonlocal report
        report += str(node.val) + " "

    new_tree.pre_order(operation)
    assert report == ""


def test_pre_order_negatives():
    """ This tests to see if the pre_order method works with a tree made of negatives
    """
    new_tree = BST([-5, -1, -7, -10])
    report = ''

    def operation(node):
        nonlocal report
        report += str(node.val) + " "
    new_tree.pre_order(operation)
    assert report == "-5 -7 -10 -1 "


def test_post_order():
    """ This tests the post_ order method with a known set of numbers
    """
    new_tree = BST([5, 1, 7, 10])
    report = ''

    def operation(node):
        nonlocal report
        report += str(node.val) + " "

    new_tree.post_order(operation)
    assert report == "1 10 7 5 "


def test_post_order_zero(empty_tree):
    """ This tests the post_ order method with an empty tree
    """
    new_tree = BST([])
    report = ''

    def operation(node):
        nonlocal report
        report += str(node.val) + " "

    new_tree.post_order(operation)
    assert report == ""


def test_post_order_negatives():
    """ This tests to see if the post _order method works with a tree made of negatives
    """
    new_tree = BST([-5, -1, -7, -10])
    report = ''

    def operation(node):
        nonlocal report
        report += str(node.val) + " "
    new_tree.post_order(operation)
    assert report == "-10 -7 -1 -5 "


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


def test_fizz_buzz():
    """This tests the new class fizz buzz with known values
    """
    new_tree = BST([5, 3, 7, 15])
    fizz_buzz(new_tree)

    assert new_tree.root.val == "buzz"
    # assert new_tree.root.left.value == "fizz"
    # assert new_tree.root.right.value == "buzz"
    # assert new_tree.root.right.right.value == "fizzbuzz"


