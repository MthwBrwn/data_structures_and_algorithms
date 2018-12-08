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

def test_module_exists():
    """ This test to see if the module is Stack properly imported """
    assert Stack


# def test_repr_():
#     assert

def test_size_of_stack_zero(zero_test_stack):
    """
    """
    assert len(zero_test_stack) == 0


def test_size_of_stack_small(small_test_stack):
    """
    """
    assert len(small_test_stack) == 4


def test_for_known_value_zero(zero_test_stack):
    """
    """
    assert zero_test_stack.top is None


def test_for_known_value(small_test_stack):
    """
    """
    assert (small_test_stack).top.value == 7


