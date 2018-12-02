from .node import Node


class LinkedList(object):
    """ This class should be aware of the len of the list,
    which represents the count of Nodes in the list at any time  """
    def __init__(self, iterable=None):
        self.head = None
        self._size = 0

        if iterable is None:
            iterable = []

        if type(iterable) is not list:
            raise TypeError('iterable must be of type list')

        for val in iterable:
            self.insert(val)

    def __str__(self):
        """this returns user level information when called
        """
        output = f'Linked List: Head val - { self.head }'
        return output

    def __repr__(self):
        """this will provide technical information when called
        """
        output = f'<LinkedList: head - { self.head } size - {self._size}>'
        return output

    def __len__(self):
        """This returns the list length
        """
        return self._size

    def insert(self, value):
        """This function takes an argument when the method is called
        and inserts the value into the list
        """
        # node = Node(value)
        # node._next = self.head
        # self.head = node
        self.head = Node(value, self.head)
        self._size += 1

    def _includes(self, num):
        """In this method the check variable is the node set by head and in=s the iterator
       check passes values down the linked list and stops when
        None which would indicate the tail of the list
        """

        check = self.head
        while check and check._next is not None:
            if check.val == num:
                return True
            check = check._next

        return False


