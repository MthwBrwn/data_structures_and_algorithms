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


