from .linkedlist import LinkedList
import pytest

@pytest.fixture
def firstcond(list1, list2):
    """this is a fixture for testing conditions when
    the list is a four node list """
    ll = LinkedList()
    ll.insert(1, 5)
    ll.insert(3, 9)
    ll.insert(2, 4)
    return ll

def test_module_exists():
    """ This test to see if the module linkedlist is properly imported """
    assert LinkedList
