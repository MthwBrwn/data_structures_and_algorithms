from repeated_word import find_first_repeat, get_words_from_string
import pytest

def test_existence():
    """ This test checks to see if import works.
    """
    assert find_first_repeat


def test_component_of_repeat_get_word():
    """this tests to see if the split is working as needed
    """
    test = get_words_from_string('try this. it is one of one')
    assert test == ['try', 'this.', 'it', 'is', 'one', 'of', 'one']

def test_
