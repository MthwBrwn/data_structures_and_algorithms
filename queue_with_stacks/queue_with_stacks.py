class Node(object):
    """This is the class Node

    """
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class Stack(object):
    """This class is used to build stack objects. Each object has a top and a size when instantiated
    """
    def __init__(self):
        self.top = None

    def push(self, value):
        """Push is used to insert a node at the top of the the stack .
        """
        node = Node(value)
        node.next_node = self.top
        self.top = node
        return self

    def pop(self):
        """The pop method creates a node and inserts that node into the top of the tack (First in First out)
        """
        old_top = self.top
        self .top = old_top.next_node

        old_top.next_node = Node
        return (old_top).value

    def peek(self):
        """The peek allows a view of the top of the stack so that a pop is not performed on an empty stack
        """
        return self.top


class PseudoQueue(object):
    """This class instantiates two stacks in order to mimic the
    functionality of a queue
    """
    def __init__(self):
        self.stack_a = Stack()
        self.stack_b = Stack()

    def enqueue(self, value):
        """ enqueue is a method for the pseudoQueue class that is made up of Stack methods
        """
        while stack_b.top is not None:
            popval = stack_b.pop()
            stack_a.push(popval)

        stack_a.pop(value)
        return stack_a.top.value


    def dequeue(self):
        """
        """
        if stack_a.self.top is None and stack_b.self.top is None:
            ValueError('There ar')
