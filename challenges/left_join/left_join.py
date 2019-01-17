

def left_join(hashmapA, hashmapB):
    """ This function takes two hashmaps and inserts the data for the 2nd and adds to the 1st

    """
#  create a list to store data - list_join
    list_join = []
# for all items in hashmapA append hashmap[0] into list_join
    for item in hashmapA:
        list_join.append(item)
        list_join.append(hashmapA.get(item))
        list_join.append(hashmapB.get(item))
# [hashmapA[item]]
# for length of list join get hashmapB[listjoin[i]] and append to list_join
# if no value append "null"
    # for i in range(len(list_join)):
    #     if hashmapB[list_join[i]][1]:
    #         list_join[i].append(hashmapB[list_join[i]][1])
    #     else:
    #         list_join[i] = 'null'
#
# return list_join
    return list_join
