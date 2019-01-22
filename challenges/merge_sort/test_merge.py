from merge_sort import mergesort
import pytest


def test_import():
    """ This tests that import works and
    """
    assert mergesort


def test_merge_sort():
    """ This tests the sort with a small set of know values.
    """
    testsort = mergesort([42, 14, 1, 36])
    assert testsort == [1, 14, 36, 42]


