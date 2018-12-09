from node import Node


class Queue(object):
    """
    """
    def __init__(self, iterable=None):
        self.front = None
        self.back = None
        self.queue_size = 0

        if iterable is None:
            iterable = []

        if type(iterable) is not list:
            raise TypeError('iterable must be of type list')

        for val in iterable:
            self.enqueue(val)

    def __len__(self):
        """ This method gets the length of a queue instance
        """
        return self.queue_size

    def __repr__(self):
        """ This method provides info about the Queue object
        """
        return f'<Queue Front: { self.front }> <<Queue back: { self.back }>'

    def __str__(self):
        """ This method provides info about the Queue object
        """
        return f'<Queue Front: { self.front }>'

    def enqueue(self, value):
        """  This method takes the value and adds it to the rear of the queue object
        For the queue when he first node is added the first node will be front and back
        After the first the new nodes add to the back and point to the next node
        size is incremented by 1
        """
        node = Node(value)

        if self.front is None and self.back is None:
            self.back = node
            self.front = node
        else:
            self.back._next = node
            self.back = node

        self.queue_size += 1

    def dequeue(self):
        """ dequeue does not take an argument - Dequeue removes the node at the front postion.
        """
        temp = self.front
        self.front = self.front.next
        temp.next = None
        self.queue_size -= 1
        return temp
