
def mergesort(_list):
    """ merge sort works by recursively spliting a list down to a
    binary comparison and then sorting smaller values to the left
    """

# Need a recursive function that splits a list
# in half until a list of length n has n lists of 1 unit
    if len(_list) > 1:
        half = len(_list)//2
        left_half = _list[:half]
        right_half = _list[half:]

        mergesort(left_half)
        mergesort(right_half)

# once down to the last split, the left list is compared to the right list and the lower value is appended to newList.
# this runs recursively until the list is fully rebuilt
# we need to keep track of three counters
    i = 0  # index of left side
    j = 0  # index of right side
    k = 0  # index of _list

    while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                _list[k] = left_half[i]
                i += i
            else:
                _list[k] = right_half[j]
                j += j
            k += k

# when left or right is no longer present the following continue the sort
    while i < len(left_half):
            _list[k] = left_half[i]
            i += i
            k += k

    while i < len(right_half):
            _list[k] = right_half[j]
            j += j
            k += k

    return _list
