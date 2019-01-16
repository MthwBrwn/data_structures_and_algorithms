

# function will need to take in two values
def tree_intersection(tree1, tree2):
    """
    """
    list_1 = Hashtable()
    list_2 = []

    # setting up helper for traversal operation
    def _add_to_list_1():
        list_1.put(node.val, 1)
        return

    def _add_to_list_2():
        if list_1.get(node.val):
            list_2.append(node.val)
            return
# traverse tree #1, hashing each node value and placing into a list_1 (hash table)
# traverse tree #2, at each node, if hashed value of node is in list_1, then  value of node is placed in list_2

    tree1.pre_order(_add_to_list_1)
    tree2.pre_order(_add_to_list_2)

#  return list_2
    return list_2


class Node (object):
    """ Class node s aware of the value as val and left and right children
    as left and right
    """
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class BST (object):
    """ BST is a class that is aware of the root as root
    """
    def __init__(self, iterable=None):
        self.root = None

        if iterable is None:
            iterable = []
        if type(iterable) is not list:
            raise TypeError('iterable must be of type list')
        for val in iterable:
            self.insert_node(val)

    def pre_order(self, operation):
        """pre order traverses through the tree in a root, left, right fashion
        """
        def _traverse(root):
            if root is None:
                return

            operation(root)
            _traverse(root.left)
            _traverse(root.right)

        _traverse(self.root)

    def insert_node(self, val):
        """This function is used to insert a node at a specific point
        """
        new_node = Node(val)
        current = self.root
        if self.root is None:
            self.root = new_node
            return new_node

        while current:
            if val < current.val:
                if current.left is not None:
                    current = current.left
                else:
                    current.left = new_node
                    break

            if val >= current.val:
                if current.right is not None:
                    current = current.right
                else:
                    current.right = new_node
                    break


class Hashtable:
    """hash table takes is a class that creates objects which have the methods
    put, get and hash in order to create hs tables
    """

    def __init__(self):
        self.size = 64
        self.bucket = [None] * self.size

    def __repr__(self):
        return f'bucket size : {self.size}'

    def sum_hash(self, key):
        """ This hashing function takes the key and sums the ASCII values (ord)
        of the key and then uses mod in order to obtain the
        """
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.size

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

    def get(self, key):
        """ get takes the key, and returns the value associated with that key
        """
        hash = self.sum_hash(key)
        if self.bucket[hash] is not None:
            for pair in self.bucket[hash]:
                if pair[0] == key:
                    return pair[1]
