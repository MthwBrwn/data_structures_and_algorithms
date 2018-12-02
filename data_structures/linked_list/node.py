class Node (object):
    """ Class node creates node objects. val is a required argument.
    If no argument is given for _next, next will be None
    """
    def __init__(self, val, _next =  None):
        self.val = self
        self._next = _next

    def __str__(self):
        output = f'{self.val}'
        return output


