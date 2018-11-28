import math

def insert_shift_array(old_list, y):
    new_list = []
    cut = math.ceil(len(old_list)/2)
    for i in range(cut):
        new_list.append(old_list[i])
    new_list.append(y)
    for i in range(cut,len(old_list)):
        new_list.append(old_list[i])

    return new_list
