from quick_sort import quickSort
import pytest


def test_import():
    """ This tests that import works
    """
    assert quickSort


def test_quick_sort():
    """ This tests the sort with a small set of known values.
    """
    testsort = quickSort([42, 14, 1, 36])
    assert testsort == [1, 14, 36, 42]


def test_quick_sort_negatives():
    """ This tests known values with negative figures to check if still works
    """
    testsort = quickSort([-42, -14, -1, -36])
    assert testsort == [-42, -36, -14, -1]


def test_quick_sort_empty():
    """ Checks to see if passing an empty to function will cause an error
    """
    testsort = quickSort([])
    assert testsort == []


def test_quick_sort_one_figure():
    """ Checks to see if passing a list with just one value will cause error
    """
    testsort = quickSort([1])
    assert testsort == [1]


def test_quick_sort_text():
    """ this check to see if an function works with an array of text
    """
    testsort = quickSort(['C', 'h', 'e', 'c', 'k'])
    assert testsort == ['C', 'c', 'e', 'h', 'k']


def test_to_see_if_type_is_enforced_string():
    """ this test makes sure that errors are raised when 1) wrong type is used
    """
    with pytest.raises(TypeError):
        quickSort(" ")
