from .node import Node


class AnimalShelter(object):
    """ Animal is a node class who will provide the methods for Cat Dog queues
    """

    def __init__(self, iterable=None):
        self.loader= Queue()
        self.rejects= Queue()

        if iterable is None:
            iterable = []

        if type(iterable) is not list:
            raise TypeError('iterable must be of type list')

        for val in iterable:
            self.enqueue(val)

    #this could work with a
    def enqueue(self, animal):
        """ enqueue only inserts into the loader queue
        """
        node = Node(animal)

        if self.front is None and self.back is None:
            self.loader.back = node
            self.loader.front = node
        else:
            self.loader.back._next = node
            self.loader.back = node


    def dequeue(self, pref):
        """ Dequeue has to determine if pref == or != type of rejects. All rejects will be of same type,
        so if type is cat and rejects.front is dog all nodes in rejects is dog. Check loader for cat and dequeue /enqueue to rejects

        """
        if pref ==
        if peek(self.value) is None:
            raise AttributeError('cannot dequeue an empty queue')
        if
        temp == self.front
        if temp:  #using falsy logic
            self.front = self.front.next
            temp.next = None

            return temp
        else: #self.front is None
            return temp


