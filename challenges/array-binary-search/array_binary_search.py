
def binary_search(list, key):
    our_index = len(list)//2
    ans_index = our_index
    while our_index > 0:
        if list[our_index] < key:
            list = list[0:our_index]
            our_index = len(list)//2
            ans_index -= our_index
        else:
            list = list[our_index:len(list)]
            our_index = len(list)//2
            ans_index += our_index
    if list[0] == key:
        return ans_index
    if list[0] != key:
        return -1


