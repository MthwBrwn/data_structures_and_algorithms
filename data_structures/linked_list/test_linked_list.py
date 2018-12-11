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
def small_double_rev_linklist():
    """this is a fixture for testing conditions when
    the list is a four node list """
    ll = LinkedList()
    ll.insert(8)
    ll.insert(6)
    ll.insert(4)
    ll.insert(2)
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
    empty_ll.insert(1)
    assert empty_ll.head.val == 1


def testrandom_ll(random_ll):
    """ This tests a larger number of nodes and sets values at random"""
    assert len(random_ll) == 100


def test_includes_is_True(small_linklist):
    """ this tests the condition of including 3 which is known
    in our small list"""
    assert small_linklist.includes(3) is True


def test_includes_is_False(small_linklist):
    """ This tests false know to be false in the linked list"""
    assert small_linklist.includes(6) is False


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


def test_for_insert_before_no_nodes():
    ll = LinkedList()
    with pytest.raises(ValueError) as e:
        ll.insert_before(1, 1)
        assert "There aren't any nodes in linkedlist" in str(e.value)

#test for not found
def test_for_insert_before_not_found():
    ll = LinkedList([1, 2])
    with pytest.raises(ValueError) as e:
        ll.insert_before(4, 1)
    assert "A node did not match your find value" in str(e.value)


def test_for_insert_before_head_is_find_val():
    ll = LinkedList([1])
    assert len(ll) == 1
    ll.insert_before(1, 3)
    assert len(ll) == 2
    assert ll.includes(1) is True
    assert ll.includes(3) is True
    assert ll.head.val == 3


def test_for_insert_before_small_list_known_values():
    ll = LinkedList([2, 4, 6, 8])
    ll.insert_before(6, 5)
    assert ll.includes(5) is True
    assert ll.kth_from_end(3) == 5


def test_kth_from_end_k_is(small_linklist):
    """ Test to determine if k of different figures gives us known value"""
    assert small_linklist.kth_from_end(0) == 1
    assert small_linklist.kth_from_end(1) == 2
    assert small_linklist.kth_from_end(5) == "Exception, k is longer than list"
    # assert small_linklist.kth_from_end(-2) == 'Exception, your k is not a positive integer'
    # assert small_linklist.kth_from_end('five') == 'Exception, your k is not a positive integer'


def test_kth_from_end_k_double_(small_double_rev_linklist):
    """ Test to determine if k of different figures gives us known value"""
    assert small_double_rev_linklist.kth_from_end(0) == 8
    assert small_double_rev_linklist.kth_from_end(1) == 6
    assert small_double_rev_linklist.kth_from_end(10) == "Exception, k is longer than list"


