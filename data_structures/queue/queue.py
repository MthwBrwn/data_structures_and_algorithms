from node import Node


class Queue(object):
    """
    """
    def __init__(self, iterable=None):
        self.top = None
        self.back = None
        self.queue_size = 0

        if iterable is None:
            iterable = []

        # if type(iterable) is not list:
        #     raise TypeError('iterable must be of type list')

        # for val in iterable:
        #     self.enqueue(val)

    def __len__(self):
        """ This creates a method in order to get the length of a queue instance
        """
        return self.queue_size
