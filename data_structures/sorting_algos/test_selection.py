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
