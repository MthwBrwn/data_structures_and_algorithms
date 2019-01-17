from left_join import left_join


def test_hash_join():
    """
    """
    hashmapA = {'red': 1, 'orange': 2, 'yellow': 3}
    hashmapB = {'red': 4, 'orange': 5, 'yellow': 6}
    testAB = left_join(hashmapA, hashmapB)
    assert testAB == ['red', 1, 4, 'orange', 2, 5, 'yellow', 3, 6]
