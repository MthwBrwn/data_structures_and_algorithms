# Create a Class for a Node which is aware of the value as val and left and right children
# as left and right respectively

class Node (object):
    """ Class node s aware of the value as val and left and right children as left and right
    """
    def __init__(self, val)
    self.val = val
    self.right = None
    self.left = None

# Ensure that you have a __repr__ and __str__ method defined to return
# appropriate representations of the node

    def __repr__(self):
        """ The repr offers all the attributes of the class for reference
        """
        return (f'val : {self.val} ; right : {self.right} ; left : {self.left} ')

    def __str__(self):
        """ The string provides the value of the node
        """
        return (f' The value of the node is {self.val}')

# Create a Class for a BST, which is aware of the root of the tree as root
# This class should accept an iterable as an argument when initialized,
# such as [20, 18, 12, 19, 11, 14, 40, 31, 22, 33], which creates a tree from that argument


class BST (object):
    """ BST is a class that is aware of the root as root
    """
    def __init__(self, iterable=None):
        self.root = None

    if iterable is None:
            iterable = []
    if type (iterable) is not list:
        raise TypeError('iterable must be of type list')
    for val in iterable:
        self.insert(val)
# Ensure that you have a __repr__ and __str__ method defined to
# return appropriate representations of the tree

    def __repr__(self):
        """repr returns back the root
        """
        return (f' {root}')

    def __str__(self):
        """str returns back the value of root
        """
        return (f' {root.value}')

# This class should be aware of depth-first traversal methods for
# in_order, pre_order, and post_order traversals
    def pre_order(self, node=None, operation):
        if node is None:
            return
    operation(node)

    if node.left_child is not None:
        pre_order(node.left_child)
    if node.right_child is not None:
        pre_order(node.right_child)

    def post_order(self, node=None, operation):
    if Node is None:
        return
    if node.left_child is not None:
        pre_order(node.left_child)
    if node.right_child is not None:
        pre_order(node.right_child)

    operation(node)

    def in_order(self, node=None, operation):
    if node.left_child is not None:
        pre_order(node.left_child)

    operation(node)

    if node.right_child is not None:
        pre_order(node.right_child)

# This class should have the ability to insert a new node into the tree.
# Your insertion should follow an O(log n) search solution to find the
# correct place for inserting the new node.
