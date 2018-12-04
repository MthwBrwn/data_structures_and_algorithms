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
    """this is a fixture for testing conditions when
    the list is a four node list """
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    return ll


@pytest.fixture
def random_ll():
    """ this is a fixture for testing conditions when the list is empty"""
    from random import randint
    ll = LinkedList()
    for num in range(100):
        ll.insert(randint(0, 100))
    return ll

# tests


def test_module_exists():
    """ This test to see if the module linkedlist is properly imported """
    assert LinkedList


def test_ll_instance_none_value(empty_ll):
    """ tests to see when fixture is set to no value"""
    assert empty_ll.head is None


def test_ll_str_method(empty_ll):
    """ this checks that the str method works """
    assert str(empty_ll) == f'Linked List: Head val - { empty_ll.head }'


def test_size_of_empty(empty_ll):
    """ this tests that the length of the empty list is 0"""
    assert len(empty_ll) == 0


def test_size_of_small_linklist(small_linklist):
    """ this tests the length of the link list """
    assert len(small_linklist) == 4


def test_insert_new_node_into_empty_list(empty_ll):
    """ this checks that empty linked lists have a head of None"""
    assert empty_ll.head is None
    # empty_ll.insert(1)
    # assert empty_ll.head.val == 1


def testrandom_ll(random_ll):
    """ This tests a larger number of nodes and sets values at random"""
    assert len(random_ll) == 100


# def test_includes_is_True(small_linklist):
#     """ this tests the condition of including 3 which is known
#     in our small list"""
#     assert small_linklist.includes(3) == True


# def test_includes_is_False(small_linklist):
#     """ This tests false know to be false in the linked list"""
#     assert small_linklist.includes(6) == False


def test_includes_None(empty_ll):
    """ This checks to see if a linked list with no iterable returns false"""
    assert empty_ll.includes(None) is False


def test_append_test_for_empty(empty_ll):
    """ tests to see if node appended to empty"""
    assert len(empty_ll) == 0
    empty_ll.append(1)
    assert len(empty_ll) == 1


def test_append_test_for_small(small_linklist):
    """ tests to see if node appended to small group"""
    assert len(small_linklist) == 4
    small_linklist.append(1)
    assert len(small_linklist) == 5


def test_insert_before(small_linklist):
    assert len(small_linklist) == 4
    # small_linklist.insert_before(3, 7)
    # assert len(small_linklist) == 5
