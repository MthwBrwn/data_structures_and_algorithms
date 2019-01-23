def quickSort(_list):
    quickSortRunner(_list, 0, len(_list)-1)

    return _list


# Quicksort sets up the initial state of the sort
# quicksort runner will recursively come up with the split point
# after the initial reun through
def quickSortRunner(_list, first, last):
    if first < last:

        splitpoint = find_splitpnt(_list, first, last)

        quickSortRunner(_list, first, splitpoint-1)
        quickSortRunner(_list, splitpoint+1, last)


# this is the code that swaps the left side figure greater than pivot with the right side figure less than figure
def find_splitpnt(_list, first, last):
    pivotvalue = _list[first]

    left_point = first+1
    right_point = last

    done = False
    while not done:

        while left_point <= right_point and _list[left_point] <= pivotvalue:
            left_point = left_point + 1

        while _list[right_point] >= pivotvalue and right_point >= left_point:
            right_point = right_point - 1

        if right_point < left_point:
            done = True
        else:
            _list[left_point], _list[right_point] = _list[right_point], _list[left_point]

    _list[first], _list[right_point] = _list[right_point], _list[first]

    return right_point
