""" DOCSTRING
"""
from .node import Node



class LinkedList(object):
    """ This class should be aware of the len of the list,
    which represents the count of Nodes in the list at any time  """
    def __init__(self, iterable=None):
        self.head = None
        self.size = 0

        if iterable is None:
            iterable = []

        if type(iterable) is not list:
            raise TypeError('iterable must be of type list')

        for val in iterable:
            self.insert(val)

    # def
