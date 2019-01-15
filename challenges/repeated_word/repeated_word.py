
def find_first_repeat(string):
    """ This function finds the first word that is repeated in a string
    and returns the first repeated word.
    """
    bucket = []
    size = 64
    split_list = [get_words_from_string(string)]

    for i in range(len(split_list)):
        hash = sum_hash(split_list[i])
        if bucket[hash] == (split_list[i], 1):
            return split_list[i]
        else:
            bucket[hash] = (split_list[i], 1)

# get word from string
    split_list = get_words_from_string(string)
# hash key
    sum_hash(key)

#check value - if value is 1 , return key

# - else insert key:value to hash table -- value is +=1


def sum_hash(key):
    """ This function hashes the key by character ASCII value and returns the index value
    """
    hash = 0
    for char in key:
        hash += ord(char)
    return hash % size


def get_words_from_string(input):
    """
    """
    return (‘’.join((char if char.isalpha() else ” “) for char in input).split())



