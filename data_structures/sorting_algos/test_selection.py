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



