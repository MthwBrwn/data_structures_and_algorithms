from .selection import selection_sort
import pytest


def test_import():
    """ This tests that import works and
    """
    assert selection_sort


def test_selection_sort():
    """
    """
    testsort = selection_sort([42, 14, 1, 36])
    assert testsort == [1, 14, 36, 42]

# def test_to_see_if_type_is_enforced_string():
#     pass
#     """ this test makes sure that errors are raised when 1) wrong type is used and 2) lists do not trigger typeError
#     """
#     with pytest.raises(TypeError):def test_to_see_if_type_is_enforced_string():
#     """ this test makes sure that errors are raised when 1) wrong type is used and 2) lists do not trigger typeError
#     """
#     with pytest.raises(TypeError):
#         selection_sort('test')
#         selection_sort('test')


def test_selection_sort_negatives():
    """
    """
    testsort = selection_sort([-42, -14, -1, -36])
    assert testsort == [-42, -36, -14, -1]


def test_selection_sort_empty():
    """
    """
    testsort = selection_sort([])
    assert testsort == []


def test_selection_sort_text():
    """ this check to see if an function works with an array of text
    """
    testsort = selection_sort(['C', 'h', 'e', 'c', 'k'])
    assert testsort == ['C', 'c', 'e', 'h', 'k']


def test_to_see_if_type_is_enforced_string():
    """ this test makes sure that errors are raised when 1) wrong type is used
    """
    with pytest.raises(TypeError):
        selection_sort(" ")


def test_to_see_if_type_is_enforced_int():
    """ this test makes sure that errors are raised when 1) wrong type is used and 2) lists do not trigger typeError
    """
    with pytest.raises(TypeError):
        selection_sort(1234)


