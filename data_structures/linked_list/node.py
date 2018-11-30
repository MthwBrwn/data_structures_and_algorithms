class Node (object):
    """ Class node creates node objects. Val is a required argument. If no argument is given for _next, next will be None
    """
    def __init__(self, val, _next = None):
        self.val = self
        self._next = next

    def __str__(self):
        output = f'{self.val}'
        return output

    def __repr__(self):
        output = f'{self.val}, {_next}'
        return output
