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
            self.insert(val)# set new function that merges two new lists

    def traversal(val):
        """ this is the function to find the count for each list
        """
        node = Node(val)
        node._next = self.head
        self.head = node
        # self.head = Node(val, self.head)
        self._size += 1



    def get_node():
        countA = traversal(list1)
        countB = traversal(list2)

    def merge-lists(list1, list2):
        """ This function requires the link list to be fully traversed
        in order to get a list count .
        """


        while countA > 0 and countB > 0:
            if countA is > countB:
                for i in range(countA)

                # insert countA

        else:

# traverse - get numbers
# get node - go that number get val
# append node - attach got number
#

