
_size = 64

# function will need to take in two values
def tree_intersection(tree1, tree2):
    """
    """


# traverse tree #1, hashing each node value and placing into a list_1 (hash table)
# traverse tree #2, at each node, if hashed value of node is in list_1, then  value of node is placed in list_2

#  return list_2



def sum_hash(key):
    """ This function hashes the key by character ASCII value and returns the index value
    """
    hash = 0
    for char in key:
        hash += ord(char)
    return hash % _size


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
