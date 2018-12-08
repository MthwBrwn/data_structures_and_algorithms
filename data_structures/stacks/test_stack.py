from .stack import Stack
import pytest

# fixtures



@pytest.fixture
def zero_test_stack():
    """fixture for testing known figures with methods.
    This is just the object at zero
    """
    stack_obj = Stack()
    return stack_obj


@pytest.fixture
def small_test_stack():
    """fixture for testing known figures with methods.
    """
    stack_obj = Stack()
    stack_obj.push(1)
    stack_obj.push(3)
    stack_obj.push(5)
    stack_obj.push(7)
    return stack_obj


@pytest.fixture
def defined_stack():
    """fixture for testing known figures with methods.
    This is just the object at zero
    """
    stack_obj = Stack([2, 4, 6, 8])
    return stack_obj


def test_module_exists():
    """ This test to see if the module is Stack properly imported """
    assert Stack


def test_size_of_stack_zero(zero_test_stack):
    """
    This test show that he length of the instantiated object has a size of zero

    """
    assert len(zero_test_stack) == 0


def test_size_of_stack_small(small_test_stack):
    """
    this shows that the size is working with push method
    """
    assert len(small_test_stack) == 4


def test_for_known_value_zero(zero_test_stack):
    """
    This tests the top value of the empty set
    """
    assert zero_test_stack.top is None


def test_for_known_value(small_test_stack):
    """
    This tests the known value of a short set of push commands
    """
    assert (small_test_stack).top.value == 7


def test__repr_on_empty():
    """This tests the _repr_ responses for the stack objects
    """
    testastack = Stack()
    assert str(testastack) == "<STACK Top: None>"


def test_repr_on_iter_stack():
    """  This tests the _repr_ for the iterated stack from list
    """
    testastack = Stack([2, 4, 6, 8])
    assert str(testastack) == "<STACK Top: 8>"

def test_pop_on_iter_stack():
    """  This tests the _repr_ for the iterated stack from list
    """
    testastack = Stack([2, 4, 6, 8])
    assert Stack.pop(testastack) == 8


def test_peek_at_empty():
    """
    This tests that a message is displayed when a peek is done on a
    """
    testastack = Stack()
    assert Stack.peek(testastack) == "No element(s) in the stack"


def test_pop_at_empty():
    """
    This tests that a message is displayed when a pop is done on an empty node.
    This prevents an error
    """
    testastack = Stack()
    assert Stack.pop(testastack) == "No element(s) in the stack"
