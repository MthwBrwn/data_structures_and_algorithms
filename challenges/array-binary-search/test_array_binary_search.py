from array_binary_search import binary_search
""""
"""


def test_assert_true():
    """ using this to check test working fine
    """
    binary_search('sadf', 'asdf')
    assert True is True


def test_sample1(actual, check_val):
    """" checks first sample from lab """
    actual = [4, 8, 15, 16, 23, 42]
    check_val = 15
    expected = 2
    assert binary_search(actual, check_val) == expected

# def test_sample1(a, b):,
#     actual = [4,8,15,16,23,42]
#     b_testnum = 15
#     expected = 2
#     assert insert_shift_array(actual, insert_val) == expected



