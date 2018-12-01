""" """
from .linkedlist import LinkedList

import pytest

# fixtures

@pytest.fixture
def empty_ll():
    """ This creates a fixture where no value for link exists
    """
    return LinkedList()


@pytest.fixture
def small_linklist():
    """ """
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    return ll


@pytest.fixture
def random_ll():
    """ """
    from random import randint
    ll = LinkedList()
    for num in range(100):
        ll.insert(randint(0, 100))
    return ll

# tests


def test_module_exists():
    """ """
    assert LinkedList


def test_ll_instance_none_value(empty_ll):
    """ tests to see when fixture is set to no value"""
    assert empty_ll.head is None


def test_ll_str_method(empty_ll):
    """ """
    assert str(empty_ll) == f'Linked List: Head val - { empty_ll.head }'


def test_size_of_empty(empty_ll):
    """ """
    assert len(empty_ll) == 0


def test_size_of_small_linklist(small_linklist):
    """ """
    assert len(small_linklist) == 4


def test_insert_new_node_into_empty_list(empty_ll):
    """ """
    assert empty_ll.head is None
    # empty_ll.insert(1)
    # assert empty_ll.head.val == 1


def testrandom_ll(random_ll):
    """ """
    assert len(random_ll) == 100


def test_includes(small_linklist):
    """ """
    actual = 3
    # assertFalse (small_linklist._includes() = actual)
    assert small_linklist._includes(4) == True
