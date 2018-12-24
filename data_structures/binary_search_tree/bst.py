# Create a Class for a Node which is aware of the value as val and left and
#  right children as left and right respectively


class Node (object):
    """ Class node s aware of the value as val and left and right children
    as left and right
    """
    def __init__(self, val):
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
        if type(iterable) is not list:
            raise TypeError('iterable must be of type list')
        for val in iterable:
            self.insert_node(val)
    # Ensure that you have a __repr__ and __str__ method defined to
    # return appropriate representations of the tree

    def __repr__(self):
        """repr returns back the root
        """
        return (f' {self.root}')

    def __str__(self):
        """str returns back the value of root
        """
        return (f' {self.root.val}')

    # This class should have the ability to insert a new node into the tree.
    # Your insertion should follow an O(log n) search solution to find the
    # correct place for inserting the new node.
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

    # This class should be aware of depth-first traversal methods for
    # in_order, pre_order, and post_order traversals
    def in_order(self, operation):
        """in order traverses in the fashion of Left, Root, Right
        """
        def _traverse(root):
        # base case
            if root is None:
                return

            _traverse(root.left)
            operation(root)
            _traverse(root.right)

        _traverse(self.root)

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

    def post_order(self, operation):
        """post order traverses in the fashion of Left, Right , Root
        """
        def _traverse(root):
            if root is None:
                return

            _traverse(root.left)
            _traverse(root.right)

            operation(root)

        _traverse(self.root)

    def find_maximum_value(self):
        if self.root is None:
            return
        maxVal = self.root.val

        def _find_maximum_value(node):
                """this method utilizes a preorder method to traverse through the tree.
                If the node.val is greater, the max val is assigned
                """
                if node is None:
                    return
                nonlocal maxVal
                if node.val > maxVal:
                    maxVal = node.val

                _find_maximum_value(node.left)

                _find_maximum_value(node.right)

        _find_maximum_value(self.root)
        return maxVal


def fizz_buzz(tree):
    """ Fiz buzz takes a tree as argument, and returns a tree where
    multiples of 3 are returned as 'fizz' and multiples of 5 are returned
    as 'buzz'
    """
    def fizz_buzz_operation(node):
        # if node.val % 3 == 0 and node.val % 5 == 0:
        #     node.val = 'fizzbuzz'
        # elif node.val % 3 == 0:
        #     node.val = 'fizz'
        # elif node.val % 5 == 0:
        #     node.val = 'buzz'
        # else:
        #     pass

        val = ''
        if node.val % 3 == 0:
            val += 'fizz'
        if node.val % 5 == 0:
            val += 'buzz'

        node.val = val or node.val

    tree.in_order(fizz_buzz_operation)
    return tree

