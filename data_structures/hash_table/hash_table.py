class Hashtable:
    """
    """

    def __init__(self):
        self.size = 64
        self.bucket = [None] * self.size

    def __repr__(self):
        return f'bucket size : {self.size}'

    def __str__(self):
        return f'bucket size : {self.size}'

# A hash table should support at least the following methods:
# hash key value
    def sum_hash(self, key):
        """ This hashing function takes the key and sums the ASCII values (ord)
        of the key and then uses mod in order to obtain the
        """
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.size

    # .put(key, value) - store a value with the given key
    def put(self, key, value):
        """ put takes in two arguments key and value and hashes
        the key to an index int and assigns the value to that int
        """
        hash = self.sum_hash(key)
        key_value = [key, value]

        if self.bucket[hash] is None:
            self.bucket[hash] = list([key_value])
            return True
        else:
            for pair in self.bucket[hash]:
                if pair[0] == key:
                    pair[1] == value
                    return True
        self.buckets[hash].append(key_value)
        return True

    # .get(key) - get the value associated with the given key
    def get(self, key):
        """ get takes the key, and returns the value associated with that key
        """
        hash = self.sum_hash(key)
        if self.bucket[hash] is not None:
            for pair in self.bucket[hash]:
                if pair[0] == key:
                    return pair[1]

    # .remove(key) - delete a value associated with a key
    def remove(self, key):
        """ This method searches for the key given and if key is located in bucket
        will pop contents from bucket.
        """
        hash = self.sum_hash(key)
        if self.bucket[hash]is None:
            return False
        for i in range(len(self.bucket[hash])):
            if self.bucket[hash][i][0] == key:
                self.bucket[hash].pop(i)
                return True

    # .keys() - return a collection of all the keys
    def keys(self):
        """ This is a simple print method for every item in bucket.
        """
        for item in self.bucket:
            if item is not None:
                print(item)
