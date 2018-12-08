class Node(object):
    """  Class node instantiates node objects when called . The class has two arguements value and a next.
    Value is required and if no argument is made for _next, it defaults to None
    """
    def __init__(self, value, _next=None):
        """
        """
        self.value = value
        self.next = _next

    def __repr__(self):
        """ This method for node returns the value for node when called
        """
        output = f'<Node: {self.value}>'
        return output
