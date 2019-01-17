from left_join import left_join
import pytest


def test_hash_join():
    """ checks to make sure the join function works
    """
    hashmapA = {'red': 1, 'orange': 2, 'yellow': 3}
    hashmapB = {'red': 4, 'orange': 5, 'yellow': 6}
    testAB = left_join(hashmapA, hashmapB)
    assert testAB == ['red', 1, 4, 'orange', 2, 5, 'yellow', 3, 6]


def test_hash_join_extra_B():
    """ checks to make sure the join function works when hash map B has
    keys not found in A
    """
    hashmapA = {'red': 1, 'orange': 2, 'yellow': 3}
    hashmapB = {'red': 4, 'orange': 5, 'yellow': 6, 'green': 0}
    testAB = left_join(hashmapA, hashmapB)
    assert testAB == ['red', 1, 4, 'orange', 2, 5, 'yellow', 3, 6]


def test_hash_join_null_A():
    """ checks to make sure the join function works when A has a key that
    hashmapB does not -- SHOULD SHOW 'NULL'
    """
    hashmapA = {'red': 1, 'orange': 2, 'yellow': 3, 'blue': 9}
    hashmapB = {'red': 4, 'orange': 5, 'yellow': 6}
    testAB = left_join(hashmapA, hashmapB)
    assert testAB == ['red', 1, 4, 'orange', 2, 5, 'yellow', 3, 6, 'blue', 9, 'null']


def test_hash_join_emptyA():
    """ checks to make sure the join function works when hash map B has
    keys not found in A - A is empty
    """
    hashmapA = {}
    hashmapB = {'red': 4, 'orange': 5, 'yellow': 6, 'green': 0}
    testAB = left_join(hashmapA, hashmapB)
    assert testAB == []


def test_hash_join_emptyB():
    """ checks to make sure the join function works
    when hashmapB is empty
    """
    hashmapA = {'red': 1, 'orange': 2, 'yellow': 3}
    hashmapB = {}
    testAB = left_join(hashmapA, hashmapB)
    assert testAB == ['red', 1, 'null', 'orange', 2, 'null', 'yellow', 3, 'null']


def test_wrong_type_given():
    """ checks to make sure that errors are handled with wrong data types
    """
    hashmapA = ['red', 1, 'orange', 2, 'yellow', 3]
    hashmapB = {'red': 4, 'orange': 5, 'yellow': 6}
    with pytest.raises(TypeError):
        left_join(hashmapA, hashmapB)


