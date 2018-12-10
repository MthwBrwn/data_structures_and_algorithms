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

    def insert(self, val):
        """This function takes an argument when the method is called
        and inserts the value into the list
        """
        node = Node(val)
        node._next = self.head
        self.head = node
        # self.head = Node(val, self.head)
        self._size += 1

    def includes(self, val):
        """In this method the check variable is the node set by head and in=s the iterator
       check passes values down the linked list and stops when
        None which would indicate the tail of the list
        """
        current = self.head
        while current:
            if current.val == val:
                return True
            else:
                current = current._next
        return False

    def append(self, val):
        """ this is a method to add a node to the end of the linked list
        """
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        current = self.head
        while current._next:
            current = current._next
        current._next = new_node
        current._next._next = None
        self._size += 1
        return

    def insert_before(self, find_val, new_val):
        """ in this method the node with the find val is located
        and then the new_val is appended in front of it"""
        new_node = Node(new_val)
        current = self.head
        previous = None
        # # #if head is None
        if current is None:
            raise ValueError("There aren't any nodes in linkedlist")
        # find_val is equal to head.val
        if current.val == find_val:
            new_node._next = current
            self.head = new_node
            self._size += 1
            return self
        while current:
            if current.val == find_val:
                new_node._next = current
                previous._next = new_node
                self._size += 1
                return self
            previous = current
            current = current._next
        # find = False ??

        raise ValueError("A node did not match your find value")
        return


    def kth_from_end(self, k):
        """This method uses a k value to establish a point k from the head
        through traversing set to the variable outpoint. The head is set to another variable,
        current. both current and outpoint traverse the list and when outpoint reaches None,
        the current value will be returned """
        # edges : k < 0 or k is not int
        # k is greater than linked list
        # if k is not type(int) or k < 0:
        #     return "Exception, your k is not a positive integer"
        outpoint = self.head
        current = self.head

        for i in range(k):
            outpoint = outpoint._next
            if outpoint._next is None:
                return "Exception, k is longer than list"

        while outpoint._next:
            current = current._next
            outpoint = outpoint._next

        return current.val

