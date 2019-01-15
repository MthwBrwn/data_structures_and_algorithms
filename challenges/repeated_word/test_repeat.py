from repeated_word import find_first_repeat, get_words_from_string
import pytest

def test_existence():
    """ This test checks to see if import works.
    """
    assert find_first_repeat

def test_component_of_repeat():
    """
    """
    test = find_first_repeat('try this one')
    assert test == ('try', 'this', 'one')
