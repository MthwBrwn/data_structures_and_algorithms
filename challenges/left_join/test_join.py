from left_join import left_join


def test_hash_join():
    """
    """
    hashA = {'red': 1, 'orange': 2, 'yellow': 3}
    hashB = {'red': 4, 'orange': 5, 'yellow': 6 }
    testAB = left_join(hashA, hashB)
    assert testAB == [['red', 1, 4], ['orange', 2, 5], ['yellow', 3, 6]]
