class Node(object):
    """This is the class Node

    """
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return f'{ self.value }'

    def __repr__(self):
        return f'<NODE: { self.value }>'


class Stack(object):
    """This class is used to build stack objects
    """
    def __init__(self):
        self.top = None
        self.stack_size = 0

        if iterable is None:
            iterable = []

        if type(iterable) is not list:
            raise TypeError('iterable must be of type list')

        for val in iterable:
            self.push(val)

    def __repr__(self):
        return f'<STACK { self.top }>'

    # def

    def __len__(self):
        return self.stack_size

    def push(self, value):
        """Push is used to insert a node at the top of the the stack .
        """
        node = Node(value)
        node.next_node = self.top
        self.top = node
        return self

    def pop(self):
        """
        """
        old_top = self.top
        self .top = old_top.next_node

        old_top.next_node = Node

        return old_top.value

    def peek(self):
        """
        """
        return self.top  # or self.top.value

