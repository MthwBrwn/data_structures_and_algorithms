""" """
from .linkedlist import LinkedList

import pytest


def test_module_exists():
    """ """
    assert LinkedList

@pytest.fixture
def empty_ll():
    """ This creates a fixture where no value for link exists
    """
    return LinkedList()


def test_ll_instance_none_value(empty_ll):
    """ tests to see when fixture is set to no value"""
    assert empty_ll.head is None


def test_ll_str_method(empty_ll):
    assert str(empty_ll) == f'Linked List: Head val - { empty_ll.head }'


