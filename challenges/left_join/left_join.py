

def left_join(hashmapA, hashmapB):
    """ This function takes two hashmaps and inserts the data for the 2nd and adds to the 1st

    """
    if type(hashmapA) == dict and type(hashmapB) == dict:
#  create a list to store data - list_join
        list_join = []
    # for all items in hashmapA append hashmap[0] into list_join
        for item in hashmapA:
            list_join.append(item)
            list_join.append(hashmapA.get(item))
            if hashmapB.get(item):
                list_join.append(hashmapB.get(item))
            else:
                list_join.append('null')

    else:
        raise TypeError('You need to enter two dictionary items as arguments')

#
# return list_join
    return list_join
