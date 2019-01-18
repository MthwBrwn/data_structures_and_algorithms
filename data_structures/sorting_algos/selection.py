# function takes in array and sorts the array using selection
def selection_sort(_array):
    """ This function sets a variable a as the index i, similarly it sets another variable
    b as the next in the array. For each i, the remaining figures are iterated over
    if a > b then
    """
    if _array is not type(list):
        raise TypeError

    else:
        for i in range(len(_array)):
            smaller_index = i
            for j in range(i+1, len(_array)):
                if _array[smaller_index] > _array[j]:
                    smaller_index = j
    #  this does a swap
            _array[i], _array[smaller_index] = _array[smaller_index], _array[i]

        return _array
#
