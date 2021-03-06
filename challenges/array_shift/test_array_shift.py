from array_shift import insert_shift_array

def test_assert_true():
    """ using this to check test working fine
    """
    assert True is True


def does_module_exist():
    assert insert_shift_array


def test_array_shift():

    actual = [1, 2, 3, 4]
    insert_val = 5
    expected = [1, 2, 5, 3, 4]
    assert insert_shift_array(actual, insert_val) == expected


def test_array_shift_with_odd():
    actual = [1,2,3,4,5]
    insert_val = 6
    expected = [1,2,3,6,4,5]
    assert insert_shift_array(actual, insert_val) == expected


def test_array_shift_with_strings():
    actual = ['','','','']
    insert_val = 'add'
    expected = ['','','add','','']
    assert insert_shift_array(actual, insert_val) == expected


