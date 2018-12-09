from .node import Node


class Stack(object):
    """This class is used to build stack objects. Each object has a top and a size when instantiated
    """
    def __init__(self, iterable=None):
        self.top = None
        self.stack_size = 0

        if iterable is None:
            iterable = []

        if type(iterable) is not list:
            raise TypeError('iterable must be of type list')

        for val in iterable:
            self.push(val)

    def __repr__(self):
        """repr returns back information about the stack
        """
        return f'<STACK Top: { self.top }>'

    def __len__(self):
        """ This magic method returns back the number of nodes in the stack
        """
        return self.stack_size

    def push(self, value):
        """Push is used to insert a node at the top of the the stack .
        """
        node = Node(value)
        node.next_node = self.top
        self.top = node
        self.stack_size += 1
        return self.top.value

    def pop(self):
        """The pop method creates a node and inserts that node into the top of the tack (First in First out)
        """
        if len(self) <= 0:
            return ("No element(s) in the stack")
        else:

            old_top = self.top
            self .top = old_top.next_node

            old_top.next_node = Node
            self.stack_size -= 1
            return (old_top).value

    def peek(self):
        """The peek allows a view of the top of the stack so that a pop is not performed on an empty stack
        """
        return self.top

