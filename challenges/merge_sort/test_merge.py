from merge_sort import mergesort
import pytest


def test_import():
    """ This tests that import works
    """
    assert mergesort


def test_merge_sort():
    """ This tests the sort with a small set of know values.
    """
    testsort = mergesort([42, 14, 1, 36])
    assert testsort == [1, 14, 36, 42]


def test_merge_sort_negatives():
    """
    """
    testsort = mergesort([-42, -14, -1, -36])
    assert testsort == [-42, -36, -14, -1]


def test_merge_sort_empty():
    """
    """
    testsort = mergesort([])
    assert testsort == []


def test_merge_sort_text():
    """ this check to see if an function works with an array of text
    """
    testsort = mergesort(['C', 'h', 'e', 'c', 'k'])
    assert testsort == ['C', 'c', 'e', 'h', 'k']


def test_to_see_if_type_is_enforced_string():
    """ this test makes sure that errors are raised when 1) wrong type is used
    """
    with pytest.raises(TypeError):
        mergesort(" ")


def test_to_see_if_type_is_enforced_int():
    """ this test makes sure that errors are raised when 1) wrong type is used and 2) lists do not trigger typeError
    """
    with pytest.raises(TypeError):
        mergesort(1234)


